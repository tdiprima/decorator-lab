"""
Example of a traditional Python class requiring manual implementation of __init__
and __repr__, illustrating the boilerplate reduced by dataclasses.
"""


class Person:
    def __init__(self, name: str, age: int, active: bool = True):
        self.name = name
        self.age = age
        self.active = active

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age}, active={self.active})"


if __name__ == "__main__":
    # I used to be sad, I used to be shy... 🎵
    person = Person("alice", 25)
    print(person)
