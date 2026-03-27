from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Dict, List, Any


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0
        self.hand: List[Any] = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        if not self.factory or not self.strategy:
            raise ValueError("Engine must be configured first")

        self.hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell("lightning")
        ]

        self.cards_created += len(self.hand)

        battlefield: List[str] = ["Enemy Player", "Enemy Creature"]

        turn_result: Dict[str, Any] = self.strategy.execute_turn(
            self.hand, battlefield)

        self.turns_simulated += 1
        self.total_damage += turn_result.get("damage_dealt", 0)

        return {
            "strategy": self.strategy.get_strategy_name(),
            "actions": turn_result
        }

    def get_engine_status(self) -> Dict[str, Any]:
        strategy_name: str = (self.strategy.get_strategy_name()
                              if self.strategy else "None")
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
