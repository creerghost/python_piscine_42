from ex3.CardFactory import CardFactory
from typing import Dict, List
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random
from tools.card_generator import CardGenerator


class FantasyCardFactory(CardFactory):
    def __init__(self):
        generator: CardGenerator = CardGenerator()
        self.creatures: Dict[Dict] = {
            "dragon": {**generator.get_creature("Fire Dragon")},
            "goblin": {**generator.get_creature("Goblin Warrior")},
        }
        self.spells: Dict[Dict] = {
            "fireball": {**generator.get_spell("Fireball")},
            "lightning": {**generator.get_spell("Lightning Bolt")},
        }
        self.artifacts = {
            "mana_ring": {**generator.get_spell("Mana Ring")}
        }

    def _get_template(self, registry: dict,
                      name_or_power: str | int | None) -> Dict:
        if isinstance(name_or_power,
                      str) and name_or_power.lower() in registry:
            return registry[name_or_power.lower()]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        template = self._get_template(self.creatures, name_or_power)
        return CreatureCard(**template)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        template = self._get_template(self.spells, name_or_power)
        return SpellCard(**template)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        template = self._get_template(self.artifacts, name_or_power)
        return ArtifactCard(**template)

    def create_themed_deck(self, size: int) -> Dict:
        deck_cards: List = []
        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])
            if choice == "creature":
                deck_cards.append(self.create_creature())
            elif choice == "spell":
                deck_cards.append(self.create_spell())
            else:
                deck_cards.append(self.create_artifact())

        return {
            "theme": "Fantasy",
            "deck_size": size,
            "cards_generated": len(deck_cards),
            "cards": deck_cards
        }

    def get_supported_types(self) -> Dict:
        return {
            "creatures": list(self.creatures.keys()),
            "spells": list(self.spells.keys()),
            "artifacts": list(self.artifacts.keys())
        }
