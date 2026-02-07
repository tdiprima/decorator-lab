"""
Dataclass example using __post_init__ for field validation, ensuring price is non-negative.
"""

from dataclasses import dataclass

@dataclass
class InventoryItem:
    description: str
    unit_price: float
    available: bool = True

    def __post_init__(self):
        if self.unit_price < 0:
            raise ValueError("Unit price must be non-negative")

if __name__ == "__main__":
    item = InventoryItem("Laptop", 999.99)
    print(item)
    try:
        invalid = InventoryItem("Mouse", -10.0)
    except ValueError as e:
        print(f"Validation error: {e}")
