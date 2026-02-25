from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int
                 ) -> None:
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health

        if not isinstance(name, str) or not name:
            raise ValueError("Card name Type is Invalid")
        if not isinstance(cost, int):
            raise ValueError("Cost Type is Invalid")
        if not isinstance(rarity, str) or not rarity:
            raise ValueError("Rarity Type is Invalid")
        if not isinstance(attack, int):
            raise ValueError("Attack Type is Invalid")
        if not isinstance(health, int):
            raise ValueError("Health Type is Invalid")
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")

    def play(self, game_state: Dict) -> Dict:
        if not isinstance(game_state, Dict):
            raise ValueError("Invalid given game info")
        try:
            game_state['name']
            game_state['cost']
        except KeyError:
            raise ValueError("Make Sure The Game Info Contains required"
                             " keys: name and cost")
        return ({
            'card_played': game_state['name'],
            'mana_used': game_state['cost'],
            'effect': "Creature summoned to battlefield"
        })

    def attack_target(self, target: str) -> Dict:
        if not isinstance(target, str):
            raise ValueError("Invalid Target Type")
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> Dict:
        return (
            {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "type": "Creature",
                "attack": self.attack,
                "health": self.health
            }
        )
