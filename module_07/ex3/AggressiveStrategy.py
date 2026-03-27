from typing import Dict, List
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):
    def prioritize_targets(self, available_targets: List) -> List:
        return sorted(
            available_targets,
            key=lambda t: (0 if t.get("type") == "Player" else 1,
                           t.get("health", 0))
        )

    def execute_turn(self, hand: List[Card], battlefield: List) -> Dict:
        cards_played: List[Card] = []
        playable: List = sorted([card for card in hand if card.is_playable()],
                                key=lambda card: card.cost)
        for card in playable:
            if card.is_playable():
                card.play()
                cards_played.append(card.name)

        total_dmg: int = sum(getattr(card, 'attack', 0)
                             for card in battlefield)
        total_dmg += sum(getattr(card, 'attack', 0)
                         for card in hand
                         if card.name in cards_played
                         and isinstance(card, CreatureCard))
        targets: List = [{"name": "Enemy Player", "type": "Player",
                          "health": 30}]
        prioritized: List = self.prioritize_targets(targets)

        return {
            "cards_played": cards_played,
            "mana_used": 0,
            "targets_attacked": [t["name"] for t in prioritized],
            "damage_dealt": total_dmg
        }

    def get_strategy_game(self):
        return self.__name__
