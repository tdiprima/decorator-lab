"""
Demonstrates stacking multiple decorators on a single function.
Shows the order of execution when decorators are applied in sequence.
"""

from functools import wraps


def decorator_a(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("A before")
        result = fn(*args, **kwargs)
        print("A after")
        return result

    return wrapper


def decorator_b(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("B before")
        result = fn(*args, **kwargs)
        print("B after")
        return result

    return wrapper


@decorator_a
@decorator_b
def fn():
    print("core function")


fn()
# Output:
# A before
# B before
# core function
# B after
# A after
