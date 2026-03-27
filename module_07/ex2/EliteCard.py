from ex0.Card import Card
from typing import List, Dict, Any
from ex2.Compatable import Compatable
from ex2.Magical import Magical


class EliteCard(Card, Compatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 hp: int, mana: int, atk: int) -> None:
        super().__init__(name, cost, rarity)
        self.hp = hp
        self.mana = mana
        self.atk = atk
        self.is_alive: bool = True

    def play(self, game_state: Dict = None) -> Dict[str, Any]:
        return {
            "action": "play",
            "card": self.name,
            "rarity": self.rarity
        }

    def attack(self, target: str) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.atk,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        blocked: int = 3
        damage: int = max(0, incoming_damage - blocked)
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
        return {
            "defender": self.name,
            "damage_taken": damage,
            "damage_blocked": blocked,
            "still_alive": self.is_alive
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {"hp": self.hp, "atk": self.base_atk}

    def cast_spell(self, spell_name: str,
                   targets: List[str]) -> Dict[str, Any]:
        cost_per_target: int = 2
        total_cost: int = len(targets) * cost_per_target
        if self.mana >= total_cost:
            self.mana -= total_cost
            return {
                'caster': self.name,
                'spell': spell_name,
                'targets': targets,
                'mana_used': total_cost
            }
        else:
            raise ValueError("Not enough mana")

    def channel_mana(self, amount: int) -> Dict[str, int]:
        self.mana += amount
        return {'channeled': amount, 'total_mana': self.mana}

    def get_magic_stats(self) -> Dict[str, int]:
        return {"mana": self.mana}
