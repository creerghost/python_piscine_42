
def ft_achievement_tracker() -> None:
    a: set[str] = {"first_kill", "level_10", "treasure_hunter", "speed"
                   "_demon"}
    b: set[str] = {"first_kill", "level_10", "boss_slayer", "collector"}
    c: set[str] = {"level_10", "treasure_hunter", "boss_"
                   "slayer", "speed_demon", "perfectionist"}
    print("=== Achievement Tracker System ===")
    print()

    print(f"Player alice achievements: {a}")
    print(f"Player bob achievements: {b}")
    print(f"Player charlie achievements: {c}")
    print()

    print("=== Achievement Analytics ===")
    print(f"ALL unique achievements: {a | b | c}")
    print(f"Total unique achievements: {len(a | b | c)}")
    print()

    print(f"Common to all players: {a & c & b}")
    a_unique: set[str] = a - b - c
    b_unique: set[str] = b - a - c
    c_unique: set[str] = c - a - b
    print(f"Rare achievements (1 player): {a_unique | b_unique | c_unique}")
    print()

    print(f"Alice vs Bob common: {a & b}")
    print(f"Alice unique: {a - b}")
    print(f"Bob unique: {b - a}")


if __name__ == "__main__":
    ft_achievement_tracker()
