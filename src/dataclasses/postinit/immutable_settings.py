"""
Frozen (immutable) dataclass using __post_init__ for validation before locking the object.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AppSettings:
    environment: str
    logging_enabled: bool

    def __post_init__(self):
        valid_envs = {"development", "staging", "production"}
        if self.environment not in valid_envs:
            raise ValueError(f"Environment must be one of {valid_envs}")


if __name__ == "__main__":
    settings = AppSettings("development", True)
    print(settings)
    try:
        invalid = AppSettings("invalid", False)
    except ValueError as e:
        print(f"Validation error: {e}")
