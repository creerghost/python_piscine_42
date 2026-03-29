from ex3.CardFactory import CardFactory
from typing import Dict, List, Any
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random
from tools.card_generator import CardGenerator


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        generator: CardGenerator = CardGenerator()
        self.creatures: Dict[str, Dict[str, Any]] = {
            "dragon": {**generator.get_creature("Fire Dragon")},
            "goblin": {**generator.get_creature("Goblin Warrior")},
        }
        self.spells: Dict[str, Dict[str, Any]] = {
            "fireball": {**generator.get_spell("Fireball")},
            "lightning": {**generator.get_spell("Lightning Bolt")},
        }
        self.artifacts: Dict[str, Dict[str, Any]] = {
            "mana_crystal": {**generator.get_artifact("Mana Crystal")}
        }

    def _get_template(self, registry: Dict[str, Dict[str, Any]],
                      name_or_power: str | int | None) -> Dict:
        if isinstance(name_or_power,
                      str) and name_or_power.lower() in registry:
            return registry[name_or_power.lower()]

        if not registry:
            raise ValueError("Cannot select template from empty registry")
        random_key = random.choice(list(registry.keys()))
        return registry[random_key]

    def create_creature(self, name_or_power: str | int | None = None
                        ) -> CreatureCard:
        template: Dict[str, Dict[str, Any]] = self._get_template(
            self.creatures, name_or_power)
        return CreatureCard(**template)

    def create_spell(self, name_or_power: str | int | None = None
                     ) -> SpellCard:
        template: Dict[str, Dict[str, Any]] = self._get_template(
            self.spells, name_or_power)
        return SpellCard(**template)

    def create_artifact(self, name_or_power: str | int | None = None
                        ) -> ArtifactCard:
        template: Dict[str, Dict[str, Any]] = self._get_template(
            self.artifacts, name_or_power)
        return ArtifactCard(**template)

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        deck_cards: List = []
        for _ in range(size):
            choice: str = random.choice(["creature", "spell", "artifact"])
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

    def get_supported_types(self) -> Dict[str, List[Any]]:
        return {
            "creatures": list(self.creatures.keys()),
            "spells": list(self.spells.keys()),
            "artifacts": list(self.artifacts.keys())
        }
