# This script shows memory optimization with slots=True (Python 3.10+). Made this one up as a simple demo since article's was basic.

from dataclasses import dataclass


@dataclass(slots=True)
class Person:
    name: str
    age: int


p = Person(name="Paulina", age=23)
print(p)  # Person(name='Paulina', age=23)

# Bonus: Try accessing p.__dict__ – it won't exist, saving memory! Uncomment below to test.
print(p.__dict__)  # Raises AttributeError
