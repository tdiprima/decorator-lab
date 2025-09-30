# This script customizes fields to exclude from repr and compare.

from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: int
    password: str = field(repr=False, compare=False)
    ssn: str = field(repr=False, compare=False)


p = Person(name="Daniela", age=25, password="secret", ssn="123-45-6789")
print(p)  # Person(name='Daniela', age=25)
# Note: password and ssn are excluded from the repr output.
# They are also excluded from comparison operations.
p2 = Person(name="Paulina", age=23, password="different", ssn="987-65-4321")
print(p == p2)  # True, because password and ssn are excluded from comparison
