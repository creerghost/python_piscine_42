from ex0.Card import Card
from typing import Dict, Any, Optional


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self,
             game_state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> Dict[str, Any]:
        if self.durability <= 0:
            return {
                "artifact_activated": self.name,
                "status": "destroyed",
                "effect_applied": "None"
            }
        self.durability -= 1

        return {
            "artifact_activated": self.name,
            "status": "destroyed",
            "effect_applied": "None"
        }
