class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self):
        self.message = f"The Tomato is wilting!"
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self):
        self.message = f"Not enough water in the tank!"
        super().__init__(self.message)


def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    print()
    try:
        print("Testing PlantError...")
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    try:
        print("Testing WaterError...")
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing catching all garden errors...")
    for error in [PlantError(), WaterError()]:
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
