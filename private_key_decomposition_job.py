import dask

from private_key_decomposition_candidates import (
    private_key_decomposition_candidates,
    is_private_key_decomposed,
)


def private_key_decomposition_job(target: int, chunk_size: int):
    @dask.delayed
    def result(chunk_index: int):
        for a in private_key_decomposition_candidates(chunk_index, chunk_size):
            if is_private_key_decomposed(target, a):
                return (a, target // a)
        return None
    return result
