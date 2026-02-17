#!/usr/bin/env python3

class Plant():
    """Main class for plants."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Subclass for flowers. Flowers can bloom."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initializing the main variables from main class and the
        self variable."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Bloom the flowers!"""
        print(f"{self.name} is blooming beatifully!")

    def get_info(self) -> None:
        """Printing the information about this plant and making it bloom."""
        print(f"{self.name} ({Flower.__name__}): {self.height}cm, {self.age}"
              f" age, {self.color} color")
        self.bloom()


class Tree(Plant):
    """Subclass for trees. Trees can produce shade."""
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int
                 ) -> None:
        """Initializing the main variables from main class and the
        self variable."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """How many shade the tree will produce? We will see!"""
        shade_area = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade_area} square meters"
              f" of shade")

    def get_info(self) -> None:
        """Printing the information about this plant and
        making him produce shade."""
        print(f"{self.name} ({Flower.__name__}): {self.height}cm, {self.age}"
              f" days, {self.trunk_diameter}cm diameter")
        self.produce_shade()


class Vegetable(Plant):
    """Subclass for vegetables. Vegetables have nutrients and grow during
    specific seasons."""
    def __init__(self, name: str, height: int, age: int, harvest_season:
                 str, nutritional_value: str) -> None:
        """Initializing the main variables and the self variables."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        """Printing the information about this plant including
        its nutritional value and its harvest season."""
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
