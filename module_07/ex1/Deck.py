from ex0.Card import Card
from typing import List, Dict
import random
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex1.ArctifactCard import ArctifactCard


class Deck:
    def __init__(self) -> None:
        self.card_list: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.card_list.append(card)

    def remove_card(self, card_name: str) -> bool:
        remove: Card = [x for x in self.card_list if x.name == self.card_list]
        if remove is None:
            return False
        self.card_list.pop(remove)
        return True

    def shuffle(self) -> None:
        random.shuffle(self.card_list)

    def draw_card(self) -> Card:
        if not self.card_list:
            raise ValueError("The deck is empty")
        return self.card_list.pop(0)

    def get_deck_stats(self) -> Dict:
        creatures: List[Card] = [x for x in self.card_list
                                 if isinstance(x, CreatureCard)]
        spells: List[Card] = [x for x in self.card_list
                              if isinstance(x, SpellCard)]
        artifacts: List[Card] = [x for x in self.card_list
                                 if isinstance(x, ArctifactCard)]
        summ: int = sum(x.cost for x in self.card_list)
        return {
            "total_cards": len(self.card_List),
            "creatures": len(creatures),
            "spells": len(spells),
            "artifacts": len(artifacts),
            "avg_cost": summ / len(self.card_list)
        }
