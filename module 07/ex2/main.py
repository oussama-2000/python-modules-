from ex2.EliteCard import EliteCard


if __name__ == "__main__":

    try:
        print("\n=== DataDeck Ability System ===\n")

        elite_card = EliteCard("Arcane Warrior", 3, "common", 5, 7, 7)

        print(f"{elite_card.__class__.__name__} capabilities")

        bases_classes = elite_card.__class__.__bases__
        for base in bases_classes:
            functions = dir(base)
            capabilities = [fun
                            for fun in functions if not fun.startswith("_")]
            print(f"- {base.__name__}: {capabilities}")

        print(f"\nPlaying {elite_card.name} (Elite Card):\n")

        game_stats = elite_card.get_magic_stats()
        paly_result = elite_card.play(game_stats)

        print("Combat phase:")

        print(f"Attack result: {elite_card.attack('Enemy')}")

        print(f"Defense result {elite_card.defend(2)}")

        print("\nMagic phase:")
        print("Spell cast: "
              f"{elite_card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
        print(f"Mana channel: {elite_card.channel_mana(3)}")

        print("\nMultiple interface implementation successful!")

    except Exception as e:
        print(f"Error: {e}")
