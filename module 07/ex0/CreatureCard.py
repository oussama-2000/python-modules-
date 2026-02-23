from ex0 import Card


class CreatureCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int
                 ) -> None:
        super().__init__(attack, health)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return game_state

    def attack_target(self, target) -> dict:
        pass
