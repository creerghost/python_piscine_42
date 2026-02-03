#!/usr/bin/env python3

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beatifully!")

    def get_info(self):
        print(f"{self.name} ({Flower.__name__}): {self.height}cm, {self.age}"
              f" age, {self.color} color")
        self.bloom()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade_area} square meters"
              f" of shade")

    def get_info(self):
        print(f"{self.name} ({Flower.__name__}): {self.height}cm, {self.age}"
              f" days, {self.trunk_diameter}cm diameter")
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        print(f"{self.name} ({Vegetable.__name__}): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest\n"
              f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    rose.get_info()
    print()
    oak.get_info()
    print()
    tomato.get_info()
