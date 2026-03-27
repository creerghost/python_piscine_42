from typing import Dict, List
from abc import ABC, abstractmethod


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        pass

    @abstractmethod
    def get_strategy_game(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List) -> List:
        pass
