from ex0.Card import Card
from typing import Dict, Any
from ex2.Compatable import Compatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Compatable, Rankable):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int, rating: int):
        super().__init__(name, cost, rarity)
        self.id: str = f"{name.split()[-1].lower()}_001"
        self.attack_v = attack
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = rating

    def play(self, game_state: Dict = None) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Entered the tournament grounds"
        }

    def attack(self, target) -> Dict[str, Any]:
        target_name: str = (target.name if hasattr(target, 'name')
                            else str(target))
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_v,
            "combat_type": "tournament_melee"
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        self.health -= incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict[str, int]:
        return {"attack": self.attack, "health": self.health}

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += (wins * 16)

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= (losses * 16)

    def get_rank_info(self) -> Dict:
        return {
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}"
        }

    def calculate_rating(self) -> int:
        return self.rating

    def get_tournament_stats(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "interfaces": ["Card", "Combatable", "Rankable"],
            "record": f"{self.wins}-{self.losses}",
            "rating": self.rating
        }
