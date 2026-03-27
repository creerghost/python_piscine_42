from typing import Dict
from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict = None) -> Dict:
        pass

    def get_card_info(self) -> Dict:
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        return True if available_mana >= self.cost else False
