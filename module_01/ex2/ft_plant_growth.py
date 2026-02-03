#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def ft_age(self):
        self.age += 1

    def __repr__(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def get_info(self):
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
