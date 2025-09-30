"""
Retry decorator with exponential backoff for handling transient failures.
Automatically retries failed function calls with increasing delays between attempts.
"""
import time
from functools import wraps


def retry(times=3, delay=0.5):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            attempt = 0
            while True:
                try:
                    return fn(*args, **kwargs)
                except Exception:
                    attempt += 1
                    if attempt >= times:
                        raise
                    time.sleep(delay * attempt)

        return wrapper

    return decorator


@retry(times=3, delay=0.5)
def flaky_func():
    raise ValueError("Fail!")  # Will retry


flaky_func()  # Uncomment to test; will raise after 3 tries
