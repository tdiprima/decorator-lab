# Dataclass equivalent of the Class-Based Decorator example
from dataclasses import dataclass
from functools import wraps


@dataclass
class CountCalls:
    fn: callable
    calls: int = 0

    def __post_init__(self):
        wraps(self.fn)(self)

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"call {self.calls} to {self.fn.__name__}")
        return self.fn(*args, **kwargs)


@CountCalls
def greet(name):
    return f"hey {name}"
