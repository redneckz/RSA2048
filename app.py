import atexit

from random import Random
from dask.distributed import Client

from config import SCHEDULER, CHUNK_SIZE, JOB_COUNT, TARGET
from private_key_decomposition_job import private_key_decomposition_job
from state import dump_state, load_state

CHUNK_COUNT = ((TARGET + 1) // 2 + CHUNK_SIZE - 1) // CHUNK_SIZE

try:
    load_state()
except Exception:
    print("NO INIT STATE")

atexit.register(dump_state)


print(f"TARGET {TARGET}")
print(f"CHUNK_COUNT {CHUNK_COUNT}")
print(f"JOB_COUNT {JOB_COUNT}")
print("================================================================")


client = Client(SCHEDULER)
client.upload_file("private_key_decomposition_candidates.py")
client.upload_file("private_key_decomposition_job.py")

try:
    batch_index_rnd = Random(1234567890)
    result = None

    while result is None:
        batch_index = batch_index_rnd.randrange(
            0, (CHUNK_COUNT + JOB_COUNT - 1) // JOB_COUNT
        )

        print(f"CHUNKS {batch_index * JOB_COUNT}-{(batch_index + 1) * JOB_COUNT}")

        futures = [
            client.submit(
                private_key_decomposition_job(TARGET, CHUNK_SIZE), chunk_index
            )
            for chunk_index in range(
                batch_index * JOB_COUNT, (batch_index + 1) * JOB_COUNT
            )
            if chunk_index < CHUNK_COUNT
        ]
        possible_results = client.gather(futures)
        result = next((r for r in possible_results if r is not None), None)

    print(f"RESULT: {result}")

    with open(f"results/{TARGET}.txt", "w", encoding="UTF-8") as result_file:
        print(result, file=result_file)
finally:
    client.close()
