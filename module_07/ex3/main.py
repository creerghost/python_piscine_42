from typing import Dict
from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


def main() -> None:
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    game: GameEngine = GameEngine()
    factory: FantasyCardFactory = FantasyCardFactory()
    strategy: AggressiveStrategy = AggressiveStrategy()
    print(f"Factory: {FantasyCardFactory.__name__}")
    print(f"Strategy: {AggressiveStrategy.__name__}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    game.configure_engine(factory, strategy)
    turn_execution: Dict = game.simulate_turn()
    print(f"Hand: {[f"{card.name} ({card.cost})" for card in game.hand]}\n")
    print("Turn execution:")
    print(f"Strategy: {turn_execution['strategy']}")
    print(f"Actions: {turn_execution['actions']}\n")

    print("Game report:")
    print(game.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern:"
          " Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
