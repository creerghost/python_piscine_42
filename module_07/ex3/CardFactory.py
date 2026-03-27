from typing import Dict, List, Any
from abc import ABC, abstractmethod
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class CardFactory(ABC):
    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None
                        ) -> CreatureCard:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None
                     ) -> SpellCard:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None
                        ) -> ArtifactCard:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict[str, List[Any]]:
        pass
