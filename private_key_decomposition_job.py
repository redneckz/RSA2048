from private_key_decomposition_candidates import (
    is_private_key_decomposed, private_key_decomposition_candidates)


def private_key_decomposition_job(target: int, chunk_size: int):
    def result(chunk_index: int):
        for a in private_key_decomposition_candidates(chunk_index, chunk_size):
            if is_private_key_decomposed(target, a):
                return (a, target // a)
        return None
    return result
