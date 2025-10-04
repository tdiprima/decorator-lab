# Demonstrates utility functions like asdict, astuple, and replace.
from dataclasses import asdict, astuple, dataclass, replace


@dataclass
class Person:
    name: str
    age: int


p = Person(name="Alejandra", age=20)
print(asdict(p))  # {'name': 'Alejandra', 'age': 20}
print(astuple(p))  # ('Alejandra', 20)
p2 = replace(p, age=21)
print(p2)  # Person(name='Alejandra', age=21)
