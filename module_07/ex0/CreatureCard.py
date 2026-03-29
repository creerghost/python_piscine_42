from ex0.Card import Card
from typing import Dict, Any, Optional


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 health: int, attack: int) -> None:
        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise ValueError("Attack or health must be positive values")
        self.health = health
        self.attack = attack

    def play(self,
             game_state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"}

    def attack_target(self, target: Any) -> Dict[str, Any]:
        target_name: str = target.name if hasattr(target,
                                                  'name') else str(target)

        return {"attacker": self.name,
                "target": target_name,
                "damage_dealt": self.attack,
                "combat_resolved": True}

    def get_card_info(self) -> Dict[str, Any]:
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info
