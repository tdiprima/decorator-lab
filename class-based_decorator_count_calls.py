from functools import wraps


class CountCalls:
    def __init__(self, fn):
        wraps(fn)(self)  # Note: This applies wraps to the instance
        self.fn = fn
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"call {self.calls} to {self.fn.__name__}")
        return self.fn(*args, **kwargs)


@CountCalls
def greet(name):
    return f"hey {name}"


print(greet("mama"))  # Prints "call 1 to greet" then "hey mama"
print(greet("bear"))  # Prints "call 2 to greet" then "hey bear"
