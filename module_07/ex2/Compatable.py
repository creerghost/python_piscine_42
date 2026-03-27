from typing import Dict
from abc import ABC, abstractmethod


class Compatable(ABC):
    @abstractmethod
    def attack(self, target: str) -> Dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        pass
