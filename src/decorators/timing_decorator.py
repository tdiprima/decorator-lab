"""
Performance timing decorator that measures function execution time.
Uses perf_counter() for high-precision timing measurements and reports results.
"""
import time
from functools import wraps


def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{fn.__name__} took {elapsed:.4f} seconds")
        return value

    return wrapper


@timeit
def example_func():
    time.sleep(1)  # Simulate work
    return "done"


print(example_func())
# example_func took 1.0049 seconds
# done
