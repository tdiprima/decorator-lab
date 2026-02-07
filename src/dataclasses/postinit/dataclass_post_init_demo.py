"""
Shows dataclass with __post_init__ for post-construction validation and
normalization, preserving auto-generated __init__.
"""

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    active: bool = True

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        self.name = self.name.title()


if __name__ == "__main__":
    person = Person("alice", 25)
    print(person)
    try:
        invalid = Person("bob", -3)
    except ValueError as e:
        print(f"Validation error: {e}")
