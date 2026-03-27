from ex0.Card import Card
from typing import Dict, List, Any


class SpellCard(Card):
    played: bool = False

    def __init__(self, name: str,
                 cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict = None) -> Dict[str, Any]:
        if self.played is True:
            raise ValueError("Card is already played (one-time use)")
        self.played = True
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type}

    def resolve_effect(self, targets: List) -> Dict[str, Any]:
        if self.played is True:
            raise ValueError("Card is already played (one-time use)")
        target_names: List[str] = [t.name if hasattr(t, 'name') else str(t)
                                   for t in targets]
        return {
            "spell_resolved": self.name,
            "effect_applied": self.effect_type,
            "targets_affected": target_names
        }
