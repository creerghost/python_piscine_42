def ft_analytics_dashboard() -> None:
    game_data: list[dict] = [
        {
            "player": "alice",
            "score": 2300,
            "is_active": True,
            "region": "north",
            "achievements": ["first_kill", "level_10", "first_kill",
                             "boss_slayer", "level_10"]
        },
        {
            "player": "bob",
            "score": 1800,
            "is_active": True,
            "region": "east",
            "achievements": ["first_kill", "first_kill", "first_kill"]
        },
        {
            "player": "charlie",
            "score": 2150,
            "is_active": True,
            "region": "central",
            "achievements": ["level_10", "boss_slayer", "first_kill",
                             "level_10", "boss_slayer", "first_kill",
                             "level_10"]
        },
        {
            "player": "diana",
            "score": 2150,
            "is_active": False,  # Diana isn't in the "Active players"
            "region": "north",
            "achievements": ["boss_slayer", "level_10"]
        }
    ]

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {[player["player"] for player
                                    in game_data if player["score"]
                                    > 2000]}")
    print(f"Scores doubled: {[]}")
if __name__ == "__main__":
    ft_analytics_dashboard()
