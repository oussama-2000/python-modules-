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

        if not isinstance(name, str) or not name:
            raise ValueError("Invalid ArtifactCard Name Type")
        if not isinstance(cost, int):
            raise ValueError("Invalid ArtifactCard Cost Type")
        if not isinstance(rarity, str) or not rarity:
            raise ValueError("Invalid ArtifactCard Rarity Type")
        if not isinstance(durability, int):
            raise ValueError("Invalid ArtifactCard Durability Type")
        if not isinstance(effect, str) or not effect:
            raise ValueError("Invalid ArtifactCard Effect Type")

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
        if self.durability <= 0:
            self.durability += 1
        return (
            {
                "name": self.name,
                "remaining_durability": self.durability,
                "activated": True
            }
        )
