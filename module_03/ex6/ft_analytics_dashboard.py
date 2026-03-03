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
            "score": 2050,
            "is_active": False,
            "region": "north",
            "achievements": ["boss_slayer", "level_10"]
        }
    ]

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {[player["player"] for player
                                    in game_data if player["score"]
                                    > 2000]}")
    print(f"Scores doubled: {[player["score"] * 2 for player in game_data]}")
    print(f"Active players: {[player["player"] for player in game_data if
                              player["is_active"] is True]}\n")

    print("=== Dict Comprehension Examples ===")
    print(f"Player scores: {({player["player"]: player["score"]
                              for player in game_data
                              if player['is_active'] is True})}")
    print(f"Score categories: {({cat: len([p for p in game_data if
                                           (cat == 'high' and p['score']
                                            > 2000)
                                           or (cat == 'medium' and 1500
                                               <= p['score'] <= 2000)
                                           or (cat == 'low' and p['score']
                                               < 1500)])
                                               for cat in ['high', 'medium', 'low']})}") # noqa
    print(f"Achievement counts: {({player['player']:
                                   len(player["achievements"])
                                   for player in game_data
                                   if player['is_active'] is True})}\n")

    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {({player['player'] for player in game_data})}")
    print(f"Unique achievements: {({ach for player in game_data for ach in
                                    player['achievements']})}")
    print(f"Active regions: {({player['region'] for player in game_data
                               if player['is_active'] is True})}\n")
    print("=== Combined Analysis ===")
    print(f"Total players: {len([player['player'] for player in game_data])}")
    print(f"Total unique achievements: {sum([len(player['achievements'])
                                             for player in game_data])}")
    scores: list[int] = [player['score'] for player in game_data]
    print(f"Average score: {sum(scores) / len(scores)}")
    highest_score: int = max([player['score'] for player in game_data])
    top_performer: list[str, int, int] = [
        ([player['player'], player['score'], len(player['achievements'])])
        for player in game_data
        if player['score'] == highest_score]
    print(f"Top performer: {top_performer[0][0]} ({top_performer[0][1]} points"
          f", {top_performer[0][2]} achievements)")


if __name__ == "__main__":
    ft_analytics_dashboard()
