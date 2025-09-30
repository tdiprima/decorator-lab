# This script uses default_factory with UUID for unique dynamic defaults.

import uuid
from dataclasses import dataclass, field


@dataclass
class GuitarPlayers:
    name: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))


p = GuitarPlayers(name="Daniela")
print(p)  # GuitarPlayers(name='Daniela', id='some-uuid')
