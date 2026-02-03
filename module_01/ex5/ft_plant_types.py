#!/usr/bin/env python3

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name)
        super().__init__(height)
        super().__init__(age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beatifully!")

    def get_info(self):
        print(f"{self.name} ({Flower.__name__}: {self.height}cm, {self.age}"
              f" age, {self.color} color")
        self.bloom()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name)
        super().__init__(height)
        super().__init__(age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Oak provides {self.height} of shade")

    def get_info(self):
        print(f"{self.name} ({Flower.__name__}): {self.height}cm, {self.age}"
              f" age, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name)
        super().__init__(height)
        super().__init__(age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    