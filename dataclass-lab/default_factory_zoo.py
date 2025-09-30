# This script uses default_factory for mutable defaults like lists in a dataclass.

from dataclasses import dataclass, field


@dataclass
class Zoo:
    name: str
    animals: list[str] = field(default_factory=list)


z = Zoo(name="Nica National Zoo")
z.animals.append("Lion")
print(z)  # Outputs: Zoo(name='Nica National Zoo', animals=['Lion'])
