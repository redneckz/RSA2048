import asyncio
import atexit
from dask.distributed import Client

from state import load_state, dump_state
from config import TARGET, CHUNK_SIZE, JOB_COUNT
from private_key_decomposition_job import private_key_decomposition_job

CHUNK_COUNT = ((TARGET + 1) // 2 + CHUNK_SIZE - 1) // CHUNK_SIZE

try:
    load_state()
except Exception:
    print("NO INIT STATE")

atexit.register(dump_state)

# cluster = LocalCluster()

print(f"TARGET {TARGET}")
print(f"CHUNK_COUNT {CHUNK_COUNT}")
print(f"JOB_COUNT {JOB_COUNT}")
print("================================================================")


async def main():
    client = await Client(asynchronous=True)
    result = None

    for batch_index in range((CHUNK_COUNT + JOB_COUNT - 1) // JOB_COUNT):
        print(f"CHUNKS {batch_index * JOB_COUNT}-{(batch_index + 1) * JOB_COUNT}")

        futures = client.map(
            private_key_decomposition_job(TARGET, CHUNK_SIZE),
            (
                chunk_index
                for chunk_index in range(
                    batch_index * JOB_COUNT, (batch_index + 1) * JOB_COUNT
                )
                if chunk_index < CHUNK_COUNT
            ),
        )
        possible_results = await client.gather(futures, asynchronous=True)
        print("RR", possible_results)
        result = next((r for r in possible_results[0] if r is not None), None)

        if result is not None:
            break

    print(f"RESULT: {result}")

    with open(f"results/{TARGET}.txt", "w", encoding="UTF-8") as result_file:
        print(result, file=result_file)


asyncio.run(main())
