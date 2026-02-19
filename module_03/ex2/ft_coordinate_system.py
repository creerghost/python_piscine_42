import sys
import math


def calculate_distance(cords: tuple[int, int, int]) -> float:
    return (math.sqrt(cords[0]**2 + cords[1]**2 + cords[2]**2))


def parse_args(args: list[str]) -> tuple[int, int, int]:
    formatted_args: list[int] = []
    [formatted_args.append(int(args[i])) for i in range(0, len(args))]
    return (tuple(formatted_args))


def ft_coordinate_system() -> None:
    argc: int = len(sys.argv)
    if argc == 1:
        print("No coordinates provided. Usage: python3 ft_score_analytics.py"
              " <x> <y> <z>")
    elif argc > 4:
        print("Too many arguments provided. Usage: python3 ft_score_analytics"
              ".py <x> <y> <z>")
    else:
        print("=== Game Coordinate System ===")
        print()

        pos_manual: tuple[int, int, int] = (10, 20, 5)
        print(f"Position created: {pos_manual}")
        print(f"Distance between (0, 0, 0) and {pos_manual}:"
              f" {calculate_distance(pos_manual):,.2f}")
        print()
        try:
            print(f"Parsing coordinates: \"{sys.argv[1]},{sys.argv[2]},"
                  f"{sys.argv[3]}\"")
            args: list[str] = [sys.argv[1], sys.argv[2], sys.argv[3]]
            pos: tuple[int, int, int] = parse_args(args)
            print(f"Parsed position: {pos}")
            print(f"Distance between (0, 0, 0) and {pos}:"
                  f" {calculate_distance(pos):,.2f}")
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")


if __name__ == "__main__":
    ft_coordinate_system()
