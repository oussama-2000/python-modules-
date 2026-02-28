from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def register_card(self, card: TournamentCard) -> str:
        pass

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        pass

    def get_leaderboard(self) -> List:
        pass

    def generate_tournament_report(self) -> Dict:
        pass
