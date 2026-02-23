from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum


class Rarity(Enum):
    common = "common"
    rare = "rare"
    epic = "epic"
    legendary = "legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        valid_rarity = [r.value for r in Rarity]
        if rarity.lower() not in valid_rarity:
            raise ValueError("Invalid rarity")
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        pass

    def get_card_info(self) -> Dict:
        return (
            {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity
            }
        )

    def is_playable(self, available_mana: int) -> bool:
        if isinstance(available_mana, int):
            if available_mana >= self.cost:
                return True
        else:
            raise ValueError("Invalid Available Mana")
        return False
