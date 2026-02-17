#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: str, age: str) -> None:
        """Initializing the variables."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> int:
        """Growing the plant by 1 cm."""
        self.height += 1

    def ft_age(self) -> int:
        """Aging the plant by 1 cm."""
        self.age += 1

    def __repr__(self) -> str:
        """Returning information in f-string format."""
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def get_info(self) -> None:
        """Printing this information."""
        print(self)


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    rose_init_height = rose.height
    print("=== Day 1 ===")
    rose.get_info()
    for day in range(1, 7):
        rose.grow()
        rose.ft_age()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose.height - rose_init_height}cm")
