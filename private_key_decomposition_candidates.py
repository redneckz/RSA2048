import sympy


def private_key_decomposition_candidates(chunk_index: int, chunk_size: int):
    return sympy.primerange(chunk_index * chunk_size, (chunk_index + 1) * chunk_size)


def is_private_key_decomposed(priv_key: int, a: int) -> bool:
    return priv_key % a == 0 and is_prime(priv_key // a)


def is_prime(n: int) -> bool:
    return sympy.isprime(n)
