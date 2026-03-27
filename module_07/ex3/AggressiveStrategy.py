from typing import Dict, List, Any
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):
    def prioritize_targets(self,
                           available_targets: List[Dict[str, Any]]
                           ) -> List[Dict[str, Any]]:
        return sorted(
            available_targets,
            key=lambda t: (0 if t.get("type") == "Player" else 1,
                           t.get("health", 0))
        )

    def execute_turn(self, hand: List[Card], battlefield: List[str]
                     ) -> Dict[str, Any]:
        cards_played: List[Card] = []
        mana_used: int = 0
        playable: List = sorted([card for card in hand
                                 if card.is_playable(available_mana=5)],
                                key=lambda card: card.cost)
        for card in playable:
            if card.is_playable(available_mana=5):
                card.play()
                mana_used += card.cost
                cards_played.append(card.name)

        total_dmg: int = sum(getattr(card, 'attack', 0)
                             for card in battlefield)
        total_dmg += sum(getattr(card, 'attack', 0)
                         for card in hand
                         if card.name in cards_played
                         and isinstance(card, CreatureCard))
        targets: List[Dict[str, Any]] = [{"name": "Enemy Player",
                                          "type": "Player",
                                          "health": 30}]
        prioritized: List[Dict[str, Any]] = self.prioritize_targets(targets)

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": [t["name"] for t in prioritized],
            "damage_dealt": total_dmg
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"
