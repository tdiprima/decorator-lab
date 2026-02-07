"""
Demonstrates a basic dataclass, automatically generating __init__, __repr__,
__eq__, and other methods without boilerplate.
"""

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    active: bool = True


if __name__ == "__main__":
    # There's a new girl in town, and she's looking good... 🎵
    person = Person("alice", 25)
    print(person)
