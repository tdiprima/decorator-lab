# Creates an immutable dataclass that raises an error on attribute changes.
from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name: str
    age: int


p = Person(name="Bear", age=45)
p.age = 50  # Raises FrozenInstanceError
