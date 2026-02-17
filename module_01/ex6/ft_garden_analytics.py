#!/usr/bin/env python3

class Plant:
    def __init__(self, name, initial_height):
        self.name = name
        self.height = initial_height
        self.growth_amount = 0
    
    def grow(self, amount):
        self.height += amount
        self.growth_amount += amount
        print(f"{self.name} grew {amount}cm")
    
    def info(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, initial_height, color):
        super().__init__(name, initial_height)
        self.color = color
        self.is_blooming = True

    def info(self):
        base = super().info()
        status = "(blooming)" if self.is_blooming else "not blooming"
        return f"{base}, {self.color} flowers {status}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, initial_height, color, points):
        super().__init__(name, initial_height, color)
        self.points = points
    def info(self):
        base = super().info()
        return f"{base}, Prize points: {self.points}"


class GardenManager:
    _total_gardens_managed = 0

    class GardenStats:
        @staticmethod
        def calculate_total_growth(plants):
            return sum(p.growth_amount for p in plants)

        @staticmethod
        def count_plant_types(plants):
            regular = sum(1 for p in plants if type(p) is Plant)
            flowering = sum(1 for p in plants if type(p) is FloweringPlant)
            prize = sum(1 for p in plants if type(p) is PrizeFlower)
            return regular, flowering, prize

        @staticmethod
        def garden_score(plants):
            score = sum(p.height for p in plants)
            score += sum(p.points for p in plants if hasattr(p, 'points'))
            return score

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager._total_gardens_managed += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_garden(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)
    
    def generate_report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(f"- {p.info()}")
        total_growth = self.GardenStats.calculate_total_growth(self.plants)
        reg_plant, flow_plant, prize_plant = self.GardenStats.count_plant_types(self.plants)
        print(f"\nPlants added: {len(self.plants)}, Total growth: {total_growth}cm")
        print(f"Plant types: {reg_plant} regular, {flow_plant} flowering, {prize_plant} prize flowers")

    @classmethod
    def create_garden_network(cls, owner_list: list):
        return [cls(name) for name in owner_list]
    
    @classmethod
    def get_total_gardens(cls):
        return cls._total_gardens_managed

    @staticmethod
    def validate_height(height):
        return height > 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice_garden = GardenManager("Alice")

    plant_1 = Plant("Oak Tree", 100)
    alice_garden.add_plant(plant_1)

    plant_2 = FloweringPlant("Rose", 25, "red")
    alice_garden.add_plant(plant_2)

    plant_3 = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice_garden.add_plant(plant_3)

    alice_garden.grow_garden()
    alice_garden.generate_report()

    print(f"Height validation test: {GardenManager.validate_height(15)}")
    garden = GardenManager.create_garden_network(["Bob"])

    bob_garden = garden[0]
    bob_garden.plants.append(Plant("Bush", 92))

    alice_score = GardenManager.GardenStats.garden_score(alice_garden.plants)
    bob_score = GardenManager.GardenStats.garden_score(bob_garden.plants)
    
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
