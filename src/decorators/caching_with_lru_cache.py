"""
Demonstrates caching with @lru_cache decorator for memoizing function results.
Implements a Fibonacci function that caches intermediate calculations to improve performance.
"""

from functools import lru_cache


@lru_cache(maxsize=1024)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(10))  # Outputs 55, caches intermediate results
