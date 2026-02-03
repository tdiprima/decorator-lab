## functools in Python (ADHD-friendly)

### What it is
- `functools` is a **built-in Python module** with tools for working with **functions that operate on other functions**.
- Main goal: **less repeated code (DRY)**, cleaner structure, and sometimes **big speed boosts**.

## 1) `@lru_cache` = "Stop recalculating the same thing"
**Use when:** a function gets called repeatedly with the same inputs (especially **recursive** ones like Fibonacci).

- It **remembers** results from previous calls.
- Next time you call it with the same arguments, it returns instantly from the cache.
- "LRU" = *Least Recently Used* (old cache entries get dropped if the cache has a limit).

```py
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

## 2) `@wraps` = "Don't break the function's name/docs"
**Use when:** you write **decorators**.

Problem: decorators can make `func.__name__` and docstrings turn into `"wrapper"` and lose useful info (bad for debugging and `help()`).

Fix: add `@wraps(func)` inside your decorator.

```py
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

Rule of thumb: **if you write a decorator, use `@wraps`.**

## 3) `partial` = "Pre-fill some arguments now, call it easier later"
**Use when:** you want a customized version of a function without rewriting it.

```py
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

square(5)  # 25
cube(2)    # 8
```

Great for callbacks, APIs, event handlers, `map()`, etc.

## 4) `reduce` = "Fold a list down into one value"
**Use when:** you want to combine items cumulatively into a single result.

```py
from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)  # 10
```

Note: often clearer to use `sum()`, loops, etc. `reduce` is better for **custom combining logic**.

# Quick cheat sheet
- **Speed up repeated calls:** `@lru_cache`
- **Write decorators safely:** `@wraps`
- **Make "preset" functions:** `partial`
- **Collapse a sequence into one value:** `reduce` (use sparingly)

<br>
