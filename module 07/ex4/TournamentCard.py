from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def play(self, game_state: Dict) -> Dict:
        pass

    def attack(self, target: str) -> Dict:
        pass

    def calculate_rating(self) -> int:
        pass

    def get_tournament_stats(self) -> Dict:
        pass
