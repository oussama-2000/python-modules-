from ex0.Card import Card
from typing import Dict, List
from enum import Enum


class EffectType(Enum):
    damage = "damage"
    heal = "heal"
    buff = "buff"
    debuff = "debuff"


class SpellCard(Card):
    """one-time use"""

    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str
                 ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

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
            'effect': 'Deal 3 damage to target'
        })

    def resolve_effect(self, targets: List) -> Dict:
        pass
