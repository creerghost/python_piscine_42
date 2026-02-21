def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    if plant_name is None:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is"
                         f" too high (max 10)")
    if water_level < 2:
        raise ValueError(f"Error: Water level {water_level} is"
                         f" too low (min 1)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is"
                         f" too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is"
                         f" too high (max 12")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print()

    try:
        print("Testing good values...")
        print(check_plant_health("tomato", 5, 4))
    except ValueError as e:
        print(e)
    print()

    try:
        print("Testing empty plant name...")
        print(check_plant_health(None, 5, 4))
    except ValueError as e:
        print(e)
    print()

    try:
        print("Testing bad water level...")
        print(check_plant_health("tomato", 15, 4))
    except ValueError as e:
        print(e)
    print()

    try:
        print("Testing bad sunlight hours...")
        print(check_plant_health("tomato", 8, 0))
    except ValueError as e:
        print(e)
    print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
