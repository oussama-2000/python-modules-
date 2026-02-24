from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from typing import List


if __name__ == "__main__":

    try:
        print("\n=== DataDeck Deck Builder ===\n")

        print("Building deck with different card types...")

        spell = SpellCard("Lightning Bolt", 3, "rare", "damage")
        creature = CreatureCard("Fire Dragon", 5, "legendary", 5, 6)
        artifact = ArtifactCard("Mana Crystal", 2, "rare", 7,
                                "Permanent: +1 mana per turn")
        test_card = SpellCard("test_card", 3, "rare", "damage")

        cards: List[Card] = [spell, artifact, creature, test_card]

        # aplicate each type magic
        spell.resolve_effect([spell, artifact, creature])  # to set effect
        artifact.activate_ability()

        deck = Deck()

        for card in cards:
            deck.add_card(card)

        deck.remove_card("test_card")  # just to demonstrate remove_card()
        print(f"Deck stats: {deck.get_deck_stats()}")

        deck.shuffle()

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

        print("\nPolymorphism in action: "
              "Same interface, different card behaviors!")
    except ValueError as e:
        print(f"Error: {e}")
