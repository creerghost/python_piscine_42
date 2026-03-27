from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from typing import Dict


def main():
    print("=== DataDeck Tournament Platform ===")
    platform: TournamentPlatform = TournamentPlatform()

    print("Registering Tournament Cards...\n")
    dragon: TournamentCard = TournamentCard("Fire Dragon", 5,
                                            "Legendary", 8, 8, 1200)
    wizard: TournamentCard = TournamentCard("Ice Wizard", 4,
                                            "Rare", 5, 4, 1205)

    for card in [dragon, wizard]:
        platform.register_card(card)
        stats: Dict = card.get_tournament_stats()
        print(f"{card.name} (ID: {card.id}):")
        print(f"- Interfaces: {stats['interfaces']}")
        print(f"- Rating: {stats['rating']}")
        print(f"- Record: {stats['record']}\n")

    print("Creating tournament match...")
    match_result: Dict = platform.create_match("dragon_001", "wizard_001")
    match_result: Dict = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}\n")

    print("Tournament Leaderboard:")
    leaderboard: Dict = platform.get_leaderboard()
    for i, card in enumerate(leaderboard, 1):
        info: Dict = card.get_rank_info()
        print(f"{i}. {card.name} - Rating:"
              f" {info['rating']} ({info['record']})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
