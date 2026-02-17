#!/usr/bin/env python3

class Plant:
    """Plant that will be in this garden."""
    def __init__(self, name: str, initial_height: int) -> None:
        """Initializing its name, initial height. Also will initialize
        how many plants are here."""
        self.name = name
        self.height = initial_height
        self.growth_amount: int = 0

    def grow(self, amount: int) -> None:
        """Making the plant grow."""
        self.height += amount
        self.growth_amount += amount
        print(f"{self.name} grew {amount}cm")

    def info(self) -> str:
        """Returning the information about this plant."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Flower class. Can bloom. Have the color."""
    def __init__(self, name: str, initial_height: int, color: str) -> None:
        """Initializing the main variables and the color.
        Initializing the parameter if it is blooming."""
        super().__init__(name, initial_height)
        self.color = color
        self.is_blooming: bool = True

    def info(self) -> str:
        """Returning the information about this plant. Blooming or not."""
        base = super().info()
        status = "(blooming)" if self.is_blooming else "not blooming"
        return f"{base}, {self.color} flowers {status}"


class PrizeFlower(FloweringPlant):
    """How many points this flower gets?"""
    def __init__(self, name: str, initial_height: int, color: str, points: int
                 ) -> None:
        super().__init__(name, initial_height, color)
        self.points = points

    def info(self):
        """Info about this flower. How much prize points it gets."""
        base = super().info()
        return f"{base}, Prize points: {self.points}"


class GardenManager:
    """Manager of garden. Can print stats, add plants, grow the garden,
    create a network of many gardens and validate the height."""
    _total_gardens_managed = 0

    class GardenStats:
        """Helper functions to print the stats."""
        @staticmethod
        def calculate_total_growth(plants: list[Plant]) -> int:
            """Return the sum of growth plants."""
            return sum(p.growth_amount for p in plants)

        @staticmethod
        def count_plant_types(plants: list[Plant]) -> tuple[int, int, int]:
            """Return a tuple of different plant counts."""
            regular = sum(1 for p in plants if type(p) is Plant)
            flowering = sum(1 for p in plants if type(p) is FloweringPlant)
            prize = sum(1 for p in plants if type(p) is PrizeFlower)
            return regular, flowering, prize

        @staticmethod
        def garden_score(plants: list[Plant]) -> int:
            """Calculate score based on height and prize points."""
            score = sum(p.height for p in plants)
            score += sum(p.points for p in plants if hasattr(p, 'points'))
            return score

    def __init__(self, owner: str) -> None:
        """Initialize a new garden with an owner and empty plant list."""
        self.owner = owner
        self.plants: list[Plant] = []
        GardenManager._total_gardens_managed += 1

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden and print a confirmation message."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_garden(self) -> None:
        """Increment the growth of every plant in the garden by 1cm."""
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)

    def generate_report(self) -> None:
        """Print a detailed status report for the garden."""
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(f"- {p.info()}")
        total_growth = self.GardenStats.calculate_total_growth(self.plants)
        reg, flow, prize = self.GardenStats.count_plant_types(self.plants)
        print(f"\nPlants added: {len(self.plants)}, Total growth: "
              f"{total_growth}cm")
        print(f"Plant types: {reg} regular, {flow} flowering, "
              f"{prize} prize flowers")

    @classmethod
    def create_garden_network(cls, owner_list: list[str]
                              ) -> list["GardenManager"]:
        """Create and return a list of GardenManager instances."""
        return [cls(name) for name in owner_list]

    @classmethod
    def get_total_gardens(cls) -> int:
        """Return the total number of GardenManager instances created."""
        return cls._total_gardens_managed

    @staticmethod
    def validate_height(height: int) -> bool:
        """Check if a given height is a positive integer."""
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
