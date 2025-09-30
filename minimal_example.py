def simple_decorator(fn):
    def wrapper(*args, **kwargs):
        print("before")
        result = fn(*args, **kwargs)
        print("after")
        return result

    return wrapper


@simple_decorator
def greet(name):
    return f"hello {name}"


print(greet("bear"))
# Output:
# before
# after
# hello bear
