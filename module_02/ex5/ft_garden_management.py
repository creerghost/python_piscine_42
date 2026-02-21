class GardenError(Exception):
    pass


class WaterError(GardenError):
    def __init__(self) -> None:
        self.message = "Not enough water in tank!"
        super().__init__(self.message)


class Plant:
    def __init__(self, name: str, water_lvl: int, sun_lvl: int) -> None:
        self.name = name
        self.water_lvl = water_lvl
        self.sun_lvl = sun_lvl


class GardenManager():
    def __init__(self) -> None:
        self.plants: list[Plant] = []

    def add(self, plant: Plant) -> None:
        try:
            if plant.name is None:
                raise ValueError("Error adding plant: Plant name cannot be"
                                 " empty!")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except ValueError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant is None:
                    raise ValueError(f"Cannot water {plant.name} - "
                                     f"invalid plant!")
                print(f"Watering {plant.name} - success")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: Plant) -> None:
        try:
            if plant.water_lvl > 10:
                raise ValueError(f"Water level {plant.water_lvl} is"
                                 f" too high (max 10)")
            if plant.sun_lvl < 2:
                raise ValueError(f"Sunlight level {plant.sun_lvl} is"
                                 f" too low (min 2)")
            print(f"{plant.name}: healthy (water: {plant.water_lvl},"
                  f" sun: {plant.sun_lvl})")
        except ValueError as e:
            print(f"Error checking {plant.name}: {e}")


def test_garden_management():
    print("=== Garden Management System ===")
    print()

    garden = GardenManager()
    tomato = Plant("tomato", 5, 8)
    lettuce = Plant("lettuce", 15, 8)
    unknown_plant = Plant(None, 5, 8)

    print("Adding plants to garden...")
    garden.add(tomato)
    garden.add(lettuce)
    garden.add(unknown_plant)
    print()

    print("Watering plants...")
    garden.water_plants()
    print()

    print("Checking plant health...")
    for plant in garden.plants:
        garden.check_plant_health(plant)
    print()

    print("Testing error recovery...")
    try:
        raise WaterError
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
