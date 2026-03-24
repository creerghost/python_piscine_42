from ex0.Card import Card
from typing import Dict, Any


class CreatureCard(Card):
    def __init__(self, health: int, attack: int) -> None:
        try:
            super().__init__()
            if attack < 0 or health < 0:
                raise ValueError("Attack or health must be positive values")
            else:
                self.health = health
                self.attack = attack
        except ValueError as e:
            print(f"Error: {e}")

    def play(self, game_state: Dict[Any]) -> Dict[Dict[Any]]:
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"}

    def attack_target(self, target: Dict[Any]) -> Dict[Any]:
        target_name: str = target.name if hasattr(target,
                                                  'name') else str(target)

        return {"attacker": self.name,
                "target": target_name,
                "damage_dealt": self.attack,
                "combat_resolved": True}

    def get_card_info(self) -> Dict[Dict[Any]]:
        info = super().get_card_info()
        info["type"] = self.type
        info["attack"] = self.attack
        info["health"] = self.health
        return info
