"""
Parameterized decorator that implements rate limiting for function calls.
Enforces a maximum number of calls per second by adding delays between invocations.
"""
import time
from functools import wraps


def rate_limit(calls_per_second):
    def decorator(fn):
        last_call = {"time": 0.0}
        interval = 1.0 / calls_per_second

        @wraps(fn)
        def wrapper(*args, **kwargs):
            now = time.time()
            elapsed = now - last_call["time"]
            if elapsed < interval:
                time.sleep(interval - elapsed)
            last_call["time"] = time.time()
            return fn(*args, **kwargs)

        return wrapper

    return decorator


@rate_limit(2)
def ping():
    return "pong"


print(ping())  # "pong", with rate limiting if called rapidly
