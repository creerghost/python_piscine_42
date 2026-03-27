from typing import Dict, List
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List[Card], battlefield: List) -> Dict:
        cards_played: List[Card] = []
        playable: List = sorted([card for card in hand if card.is_playable()],
                                key=lambda card: card.cost)
        for card in playable:
            if card.is_playable():
                card.play()
                cards_played.append(card.name)

    def get_strategy_game(self):
        return self.__name__
