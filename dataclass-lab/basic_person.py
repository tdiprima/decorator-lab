# This script demonstrates a basic dataclass for a Person with auto-generated methods like __init__ and __repr__.
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    email: str


p = Person(name="Bear", age=45, email="bear@python.com")
print(p)  # Person(name='Bear', age=45, email='bear@python.com')
print(p.name)  # Bear
print(p.age)  # 45
print(p.email)  # bear@python.com
p.age += 1
print(p.age)  # 46
print(repr(p))  # Person(name='Bear', age=46, email='bear@python.com')
# The @dataclass decorator automatically adds special methods to the class, such as __init__(), __repr__(), and __eq__().
# This reduces boilerplate code and makes it easier to create classes that primarily store data.
