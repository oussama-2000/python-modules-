from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, List


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.mana = mana
        self.mana_used = 0

        if not isinstance(name, str) or not name:
            raise ValueError("Invalid Card name")
        if not isinstance(cost, int):
            raise ValueError("Invalid Card cost")
        if not isinstance(rarity, str) or not rarity:
            raise ValueError("Invalid Card rarity")
        if not isinstance(attack, int):
            raise ValueError("Invalid Card Attack")
        if not isinstance(health, int):
            raise ValueError("Invalid Card health")
        if not isinstance(mana, int):
            raise ValueError("Invalid Card mana")

    def play(self, game_state: Dict) -> Dict:
        if not isinstance(game_state, Dict):
            raise ValueError("Invalid game state Data")
        if self.is_playable(self.mana):
            self.mana_used = self.mana - self.cost
            self.mana -= self.cost
        return game_state

    def attack(self, target: str) -> Dict:
        if not isinstance(target, str) or not str:
            raise ValueError("Invalid Target Type")
        return (
            {
                'attacker': self.name,
                'target': target,
                'damage': self.attack_power,
                'combat_type': 'melee'
            }
        )

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        if not isinstance(spell_name, str) or not str:
            raise ValueError("Invalid Spell Name")
        if not isinstance(targets, List) or not targets:
            raise ValueError("No Targets Provided")
        return (
            {
                "caster": self.name,
                "spell": spell_name,
                "target": targets,
                "mana_used": self.mana_used
            }
        )

    def defend(self, incoming_damage: int) -> Dict:
        if not isinstance(incoming_damage, int):
            raise ValueError("Invalid incoming Damage")
        self.health -= incoming_damage
        damage_blocked = self.attack_power - incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocker": damage_blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

    def channel_mana(self, amount: int) -> Dict:
        if not isinstance(amount, int):
            raise ValueError("Invalid Passed Amount")
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict:
        return {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity
        }
