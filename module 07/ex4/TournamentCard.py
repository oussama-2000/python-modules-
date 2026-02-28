from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, card_id: str, name: str,
                 cost: int, rarity: str,
                 attack: int, health: int,
                 rating: int) -> None:
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.attack_points = attack
        self.health_points = health
        self.rating = rating
        self.wins = 0
        self.losses = 0

        if not isinstance(card_id, str) or not card_id:
            raise ValueError("Invalid Card Id")
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid Card name")
        if not isinstance(cost, int):
            raise ValueError("Invalid Card Cost")
        if not isinstance(attack, int):
            raise ValueError("Invalid Card Attack")
        if not isinstance(health, int):
            raise ValueError("Invalid Card health")
        if not isinstance(rating, int):
            raise ValueError("Invalid Card Rating")

    def play(self, game_state: Dict) -> Dict:
        if not isinstance(game_state, Dict):
            raise ValueError("Invalid given game info")
        try:
            game_state['card_id']
            game_state['cost']
        except KeyError:
            raise ValueError("Make Sure The Game Info Contains required"
                             " keys: name and cost")
        return ({
            'card_id': game_state['card_id'],
            'mana_used': game_state['cost'],
            'played': True
        })

    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.card_id,
            "target": target,
            "damage": self.attack_points
        }

    def calculate_rating(self) -> int:
        return self.rating

    def get_tournament_stats(self) -> Dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int):
            raise ValueError("Invalid incoming Damage")
        self.health_points -= incoming_damage
        damage_blocked = self.attack_points - incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocker": damage_blocked,
            "still_alive": self.health_points > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_points,
            "health": self.health_points
        }

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> Dict:
        return {
            "name": self.name,
            "id": self.card_id,
            "rank": self.rating
        }
