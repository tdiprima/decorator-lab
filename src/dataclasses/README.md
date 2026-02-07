# Python Dataclasses Learning Guide

This directory contains examples demonstrating various features of Python's `@dataclass` decorator, organized from basic to advanced concepts.

## Learning Path

Work through these examples in order to progressively build your understanding of dataclasses:

| # | File | Concept | Description |
|---|------|---------|-------------|
| 1 | `basic_person.py` | **Basics** | Introduction to dataclasses with auto-generated `__init__`, `__repr__`, and `__eq__` methods |
| 2 | `defaults_animal.py` | **Default Values** | Using simple default values for dataclass fields |
| 3 | `default_factory_zoo.py` | **Mutable Defaults** | Using `default_factory` for mutable defaults like lists |
| 4 | `dynamic_uuid_guitar.py` | **Dynamic Defaults** | Using `default_factory` with lambda for dynamic values (UUID generation) |
| 5 | `field_custom_person.py` | **Field Customization** | Controlling field behavior with `repr=False` and `compare=False` |
| 6 | `post_init_person.py` | **Post-Init Processing** | Using `__post_init__` for validation and additional initialization logic |
| 7 | `immutable_person.py` | **Immutability** | Creating frozen/immutable dataclasses with `frozen=True` |
| 8 | `ordering_sitcom.py` | **Ordering** | Enabling comparison operations with `order=True` |
| 9 | `inheritance_employee.py` | **Inheritance** | Creating dataclasses that inherit from other dataclasses |
| 10 | `slots_person.py` | **Memory Optimization** | Using `slots=True` for reduced memory footprint (Python 3.10+) |
| 11 | `utils_person.py` | **Utility Functions** | Working with `asdict()`, `astuple()`, and `replace()` helper functions |

## Quick Start

Run any example file directly:

```bash
python basic_person.py
python defaults_animal.py
# ... etc
```

## Key Concepts Summary

- **@dataclass decorator**: Automatically generates boilerplate code for data-holding classes
- **field()**: Provides fine-grained control over individual fields
- **default_factory**: Safely handles mutable default values
- **__post_init__**: Runs custom logic after initialization
- **frozen=True**: Makes instances immutable
- **order=True**: Enables ordering/comparison operators
- **slots=True**: Reduces memory usage by preventing dynamic attributes

## Requirements

- Python 3.7+ (for basic dataclass support)
- Python 3.10+ (for `slots=True` parameter)

## Additional Resources

- [PEP 557 - Data Classes](https://www.python.org/dev/peps/pep-0557/)
- [Python dataclasses documentation](https://docs.python.org/3/library/dataclasses.html)

<br>
