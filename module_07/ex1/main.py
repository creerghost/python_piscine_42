from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from tools.card_generator import CardGenerator
from typing import List


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    generator: CardGenerator = CardGenerator()
    deck: Deck = Deck()
    cards_list: List[Card] = [
        SpellCard(**generator.get_spell("Lightning Bolt")),
        ArtifactCard(**generator.get_artifact("Mana Crystal")),
        CreatureCard(**generator.get_creature("Fire Dragon"))
        ]
    for card in cards_list:
        deck.add_card(card)

    print(f"Deck stats: {deck.get_deck_stats()}\n")
    print("Drawing and playing cards:\n")

    # deck.shuffle()
    while deck.card_list:
        drawn_card: Card = deck.draw_card()
        card_type: str = type(drawn_card).__name__.replace("Card", "")

        print(f"Drew: {drawn_card.name} ({card_type})")
        print(f"Play result: {drawn_card.play({})}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
