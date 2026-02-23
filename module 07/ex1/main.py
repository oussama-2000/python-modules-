from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from typing import List


if __name__ == "__main__":

    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")

    spell = SpellCard("Lightning Bolt", 3, "rare", "damage")
    creature = CreatureCard("Fire Dragon", 5, "legendary", 5, 6)
    artifact = ArtifactCard("Mana Crystal", 2, "rare", 7,
                            "Permanent: +1 mana per turn")

    cards: List[Card] = spell, artifact, creature
    deck = Deck()

    for card in cards:
        deck.add_card(card)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards\n")

    drew1 = deck.draw_card()
    print(f"Drew: {drew1.name} "
          f"({drew1.__class__.__name__})")

    print(f"Play result: {drew1.play(drew1.get_card_info())}")

    print()
    drew2 = deck.draw_card()
    print(f"Drew: {drew2.name} ({drew2.__class__.__name__})")

    print(f"Play result: {drew2.play(drew2.get_card_info())}")

    print()
    drew2 = deck.draw_card()
    print(f"Drew: {drew2.name} ({drew2.__class__.__name__})")

    print(f"Play result: {drew2.play(drew2.get_card_info())}")
