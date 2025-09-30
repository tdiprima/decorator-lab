# This script shows dataclass inheritance from another dataclass.

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


@dataclass
class Employee(Person):
    job_title: str
    salary: float


e = Employee(name="John", age=45, job_title="Web Developer", salary=4000)
print(e)
# Outputs: Employee(name='John', age=45, job_title='Web Developer', salary=4000)
