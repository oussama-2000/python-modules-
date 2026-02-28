from typing import List, Dict
from ex3.GameStrategy import GameStrategy

# Play high attack creatures first
# Attack immediately
# Target weakest enemies first


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: List, battlefield: List) -> Dict:

        cards_palyed = []
        mana_used = 0
        targets_attacked = []
        enemies = [{2: "Enemy Player"}]
        damage_dealt = 0

        attack_cards = [c for c in hand if hasattr(c, "attack")]

        for card in attack_cards:
            card.play({"name": card.name, "cost": card.cost})
            battlefield.append(card)
            hand.remove(card)
            cards_palyed.append(card.name)
            mana_used += card.cost

            attack = card.attack_target(self.prioritize_targets(enemies))
            if attack["target"] not in targets_attacked:
                targets_attacked.append(attack["target"])
            damage_dealt += attack["damage_dealt"]

        return {
            "card_played": cards_palyed,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: List) -> List:
        targets_attack = available_targets[0].keys()
        weakest_target = available_targets[0][min(targets_attack)]

        return weakest_target
