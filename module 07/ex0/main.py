from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    try:
        print("\n=== DataDeck Card Foundation ===\n")

        print("Testing Abstract Base Class Design:\n")

        card = CreatureCard(
            'First Dragon', 5,
            'Legendary', 7, 5
            )

        print("CreatureCard Info:")
        info = card.get_card_info()
        print(info)

        mana = 6
        print(f"\nPlaying Fire Dragon with {mana} mana available:")

        print(f"Playable: {card.is_playable(mana)}")

        play_result = card.play(info)
        print("Play result: ", end="")
        print(play_result)

        print(f"\n{card.name} attacks Goblin Warrior:")
        print("Attack result:", end="")
        combat = card.attack_target("Goblin Warrior")
        print(combat)

        print("\nTesting insufficient mana (3 available):")
        print(f"Playable: {card.is_playable(3)}")

        print("\nAbstract pattern successfully demonstrated!")

    except KeyError as e:
        print(f"Error: {e}")
