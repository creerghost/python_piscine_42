from typing import Dict, List, Any
from abc import ABC, abstractmethod


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: List[Any], battlefield: List[str]
                     ) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List[Dict[str, Any]]
                           ) -> List[Dict[str, Any]]:
        pass
