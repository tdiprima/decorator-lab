# Python Decorators Examples

This directory contains examples demonstrating Python decorators, from basic concepts to advanced patterns.

## Files (in recommended learning order)

| File | Description |
|------|-------------|
| `simple_example.py` | Demonstrates the fundamental structure of a Python decorator with before/after execution pattern. |
| `logged_decorator_with_wraps.py` | Shows proper use of @wraps to preserve original function metadata when decorating. |
| `timing_decorator.py` | Measures and reports function execution time using high-precision timing. |
| `class-based_decorator_count_calls.py` | Implements a decorator as a class using __call__ to count function invocations. |
| `stacking_decorators.py` | Demonstrates applying multiple decorators to a single function and their execution order. |
| `parameterized_decorator_rate_limiter.py` | Creates a decorator factory that accepts parameters to implement rate limiting. |
| `caching_with_lru_cache.py` | Uses @lru_cache to memoize Fibonacci calculations for improved performance. |
| `fibonacci_cache.py` | Alternative Fibonacci implementation using @cache decorator with cache statistics. |
| `lru_cache_weather.py` | Applies LRU caching to API calls to avoid redundant requests. |
| `cached_property_weather.py` | Uses @cached_property for one-time computation of expensive class attributes. |
| `retry_decorator_with_backoff.py` | Implements automatic retry logic with exponential backoff for handling failures. |
| `tenacity_example.py` | Shows retry functionality using the tenacity library as an alternative approach. |
| `contextmanager_example.py` | Demonstrates using @contextmanager as an alternative to decorators for timing. |
| `pytest_checks.py` | Test suite verifying that decorators properly preserve function metadata with @wraps. |

## Running the Examples

Each file can be run independently:
```bash
python simple_example.py
python timing_decorator.py
# etc.
```

Run tests:
```bash
pytest pytest_checks.py
```
