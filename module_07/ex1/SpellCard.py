from ex0.Card import Card
from typing import Dict, List


class SpellCard(Card):
    def __init__(self, name: str,
                 cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict = None) -> Dict:
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type}

