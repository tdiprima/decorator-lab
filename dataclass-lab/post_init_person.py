# This script uses __post_init__ for validation after initialization, with a random family example.
from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: int
    favorite_tv_show: str
    language: list[str] = field(default_factory=list)

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")


# Example usage (simplified; full in article)
p = Person(name="Bear Bear", age=45, favorite_tv_show="Sabrina the Teenage Witch")
print(f"{p.name} is {p.age} & likes watching {p.favorite_tv_show}.")
