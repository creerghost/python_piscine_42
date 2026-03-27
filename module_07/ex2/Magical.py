from typing import Dict, List
from abc import ABC, abstractmethod


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        pass
