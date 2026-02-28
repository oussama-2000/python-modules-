from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise ValueError("Invalid Given Card")

        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        if not isinstance(card1_id, str) or not isinstance(card2_id, str):
            raise ValueError("Invalid Cards ID")
        if card1_id not in self.cards.keys() or\
                card2_id not in self.cards.keys():
            raise ValueError("Invalid Cards ID")

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        # winner logic: higher attack wins
        if card1.attack_points >= card2.attack_points:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)

        winner.rating += 16
        loser.rating -= 16

        self.matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> List:
        def get_rating(c):
            return c.rating

        sorted_cards = sorted(
            self.cards.values(),
            key=get_rating,
            reverse=True
        )

        leaderboard = []
        i = 1
        for card in sorted_cards:
            leaderboard.append(
                f"{i}. {card.name} - Rating: {card.rating} "
                f"({card.wins}-{card.losses})"
            )
            i += 1

        return leaderboard

    def generate_tournament_report(self) -> Dict:
        total_rating = sum([card.rating for card in self.cards.values()])
        avg_rating = total_rating / len(self.cards) if self.cards else 0

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": round(avg_rating),
            "platform_status": 'active' if self.matches_played > 0
            else 'inactive'
        }
