from functools import wraps


def logged(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"calling {fn.__name__}")
        return fn(*args, **kwargs)

    return wrapper


@logged
def greet(name):
    return f"hello {name}"


print(greet("bear"))  # Prints "calling greet" then "hello bear"
