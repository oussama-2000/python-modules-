from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Dict


class GameEngine:

    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.hand = []
        self.battlefield = []
        self.turn = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Initialize engine state"""
        if not factory or not strategy or\
            not isinstance(factory, CardFactory) or\
                not isinstance(strategy, GameStrategy):
            raise ValueError("The Game Engine configuration requires"
                             " Valid Card Factory and Game strategy")
        self.factory = factory
        self.strategy = strategy
        self.hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_artifact("Bolt")
        ]
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> Dict:
        """Execute one full game turn"""
        result = self.strategy.execute_turn(
            self.hand,
            self.battlefield
        )

        self.total_damage += result["damage_dealt"]
        self.turn += 1

        return {
            "turn": self.turn,
            "strategy": self.strategy.get_strategy_name(),
            "result": result
        }

    def get_engine_status(self) -> Dict:
        return {
            "turn_simulated": self.turn,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
