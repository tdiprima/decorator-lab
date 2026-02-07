"""
Dataclass with __post_init__ generating a derived email field if not provided.
"""

from dataclasses import dataclass


@dataclass
class StaffMember:
    given_name: str
    family_name: str
    email: str = ""

    def __post_init__(self):
        if not self.email:
            self.email = (
                f"{self.given_name.lower()}.{self.family_name.lower()}@firm.org"
            )


if __name__ == "__main__":
    staff1 = StaffMember("John", "Doe")
    print(f"{staff1.given_name} {staff1.family_name}: {staff1.email}")
    staff2 = StaffMember("Jane", "Smith", "jane@external.com")
    print(f"{staff2.given_name} {staff2.family_name}: {staff2.email}")
