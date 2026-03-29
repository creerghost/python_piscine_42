from ex4.TournamentCard import TournamentCard
from typing import Dict, List, Any


class TournamentPlatform:
    def __init__(self):
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.id] = card
        return card.id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        if card1_id not in self.cards:
            raise KeyError(f"Card with ID '{card1_id}' not registered")
        if card2_id not in self.cards:
            raise KeyError(f"Card with ID '{card2_id}' not registered")

        p1: TournamentCard = self.cards[card1_id]
        p2: TournamentCard = self.cards[card2_id]

        if p1.attack_v >= p2.attack_v:
            winner: TournamentCard = p1
            loser: TournamentCard = p2
        else:
            winner, loser = p2, p1

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            "winner": winner.id,
            "loser": loser.id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> List[TournamentCard]:
        return sorted(
            self.cards.values(),
            key=lambda x: x.calculate_rating(),
            reverse=True
        )

    def generate_tournament_report(self) -> Dict[str, Any]:
        if not self.cards:
            raise ValueError("Cannot generate report with no registered cards")
        ratings: List = [card.calculate_rating()
                         for card in self.cards.values()]
        avg: float = sum(ratings) / len(ratings)
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": int(avg),
            "platform_status": "active"
        }
