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
        self.effect = None

        if not isinstance(name, str) or not name:
            raise ValueError("Invalid SpellCard Name Type")
        if not isinstance(cost, int):
            raise ValueError("Invalid SpellCard Cost Type")
        if not isinstance(rarity, str) or not rarity:
            raise ValueError("Invalid SpellCard Rarity Type")
        valid_effects_type = [e.value for e in EffectType]
        if not isinstance(effect_type, str) or\
                effect_type.lower() not in valid_effects_type:
            raise ValueError("Invalid SpellCard Effect Type")

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

    def resolve_effect(self, targets: List) -> Dict:
        """to set effect"""
        if not isinstance(targets, List):
            raise ValueError("Invalid Targets for resolving Spell Card Effect")
        if len(targets) == 0:
            raise ValueError("Invalid Targets for resolving Spell Card Effect")
        self.effect = f'Deal {len(targets)} damage to target'
        return ({
            'effect': self.effect
        })
