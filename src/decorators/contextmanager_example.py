# Context Manager equivalent of the Timing Decorator example
import time
from contextlib import contextmanager


@contextmanager
def timeit(name=None):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        func_name = name or "operation"
        print(f"{func_name} took {elapsed:.4f} seconds")


def example_func():
    with timeit("example_func"):
        time.sleep(1)  # Simulate work
        return "done"


result = example_func()
print(result)
