from ex0.CreatureCard import CreatureCard
from tools.card_generator import CardGenerator


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    generator = CardGenerator()
    card = CreatureCard(**generator.get_creature("Fire Dragon"))
    enemy = CreatureCard(**generator.get_creature("Goblin Warrior"))
    print(f"CreatureCard Info:\n"
          f"{card.get_card_info()}\n")
    mana_total: int = 6
    print(f"Playing {card.name} with {mana_total}"
          f" mana available:")
    print(f"Playable: {card.is_playable(mana_total)}\n"
          f"{card.play()}\n")
    print(f"{card.name} attacks {enemy.name}:")
    print(f"Attack result: {card.attack_target(enemy)}\n")

    mana_insuff: int = 3
    print(f"Testing insufficient mana ({mana_insuff} available)")
    print(f"Playable: {card.is_playable(mana_insuff)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
