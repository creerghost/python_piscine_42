#!/usr/bin/env python3

class Plant:
    """Plant class. Easy."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializing the variables."""
        self.name = name
        self.height = height
        self.age = age

    def __repr__(self):
        """Returning information about the plant as f-string."""
        return F"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry")
    print(rose)
    print(sunflower)
    print(cactus)
