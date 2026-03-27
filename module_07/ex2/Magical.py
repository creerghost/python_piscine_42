from typing import Dict, List, Any
from abc import ABC, abstractmethod


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> Dict[str, Any]:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, int]:
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, int]:
        pass
