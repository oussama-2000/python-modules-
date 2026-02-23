from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from typing import Dict, List
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random


class Deck():
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("Cannot draw from an empty deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:
        total_cards = len(self.cards)
        creatures_count = 0
        spells_count = 0
        artifacts_count = 0

        for card in self.cards:
            if isinstance(card, CreatureCard):
                creatures_count += 1
            if isinstance(card, SpellCard):
                spells_count += 1
            if isinstance(card, ArtifactCard):
                artifacts_count += 1
        cost_summ = 0
        for card in self.cards:
            cost_summ += card.cost
        avg = cost_summ / total_cards if total_cards else 0

        return (
            {
                'total_cards': total_cards,
                'creatures': creatures_count,
                'spells': spells_count,
                'artifacts': artifacts_count,
                'avg_cost': round(avg, 1)
            }
        )
