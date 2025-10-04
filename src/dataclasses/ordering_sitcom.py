# Enables ordering in a dataclass for comparisons based on field order.
from dataclasses import dataclass


@dataclass(order=True)
class SitcomCharacter:
    name: str
    age: int


chr1 = SitcomCharacter(name="Salem", age=800)
chr2 = SitcomCharacter(name="Sabrina", age=18)
print(chr1 > chr2)  # True
