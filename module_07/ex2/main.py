from ex2.EliteCard import EliteCard


def main():
    warrior: EliteCard = EliteCard("Arcane Warrior", 5, "Elite", 10, 4, 5)

    print("=== DataDeck Ability System ===")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {warrior.name} (Elite Card):\n")

    print("Combat phase:")
    print(f"Attack result: {warrior.attack('Enemy')}")
    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")
    print(f"Spell cast: {warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}"
          )
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
