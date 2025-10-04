# Shows default values in a dataclass and how to create an instance using them.

from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    species: str = "Carnivorous"
    age: int = 0


a = Animal(name="Tyrannosaurus Rex")
print(a)  # Outputs: Animal(name='Tyrannosaurus Rex', species='Carnivorous', age=0)
print(a.name)  # Tyrannosaurus Rex
print(a.species)  # Carnivorous
print(a.age)  # 0
