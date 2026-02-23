from ex0.Card import Card
from typing import Dict


class ArtifactCard(Card):
    """remain in play until destroyed"""

    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

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
            'effect': self.effect
        })

    def activate_ability(self) -> Dict:
        pass
