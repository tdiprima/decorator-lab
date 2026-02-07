"""
Test suite for verifying that decorators preserve function metadata.
Ensures @wraps properly maintains __name__ and __doc__ attributes.
Run with: pytest pytest_checks.py
"""

from functools import wraps


# Define a decorated function with docstring
def logged(fn):  # From earlier example
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


@logged
def greet(name):
    """say hello"""  # Docstring
    return f"hello {name}"


def test_logged_preserves_name_and_doc():
    assert greet.__name__ == "greet"
    assert "say hello" in greet.__doc__
