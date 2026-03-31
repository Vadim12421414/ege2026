from sys import setrecursionlimit
from functools import lru_cache


@lru_cache(None)
def f(n):
    return 3 * (g(n - 2) + 5)


@lru_cache(None)
def g(n):
    if n < 8:
        return 3 * n
    else:
        return g(n - 3) + 2


print(f(12345))
