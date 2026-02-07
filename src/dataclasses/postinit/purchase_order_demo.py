"""
Dataclass combining field(default_factory=...) for timestamps with __post_init__
validation on ID, using modern UTC timestamp.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class Purchase:
    order_id: int
    created: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self):
        if self.order_id <= 0:
            raise ValueError("Order ID must be greater than zero")

if __name__ == "__main__":
    purchase = Purchase(1001)
    print(purchase)
    print(f"Created at: {purchase.created}")
    try:
        invalid = Purchase(0)
    except ValueError as e:
        print(f"Validation error: {e}")
