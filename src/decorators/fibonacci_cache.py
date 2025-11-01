# pyinstrument my_functools1.py
# Here is a standard example of using lru_cache for the Fibonacci sequence:
# from functools import lru_cache
from functools import cache


# @lru_cache(maxsize=None)
@cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# Example usage
print([fib(n) for n in range(16)])
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

# View cache statistics
print(fib.cache_info())
# Output: CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)
