"""
Dataclass using __post_init__ to normalize phone numbers by removing dashes and spaces.
"""

from dataclasses import dataclass

@dataclass
class Contact:
    telephone: str
    region: str = "US"

    def __post_init__(self):
        self.telephone = self.telephone.replace("-", "").replace(" ", "")

if __name__ == "__main__":
    contact = Contact("+1-123-456-7890")
    print(contact.telephone)
    contact2 = Contact(" 987 654 3210 ")
    print(contact2.telephone)
