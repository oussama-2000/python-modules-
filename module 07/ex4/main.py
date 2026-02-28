
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    try:
        print("\n=== DataDeck Tournament Platform ===\n")

        print("Registering Tournament Cards..\n")

        dragon = TournamentCard("dragon_001", "Fire Dragon", 7, "rare", 12,
                                10, 1200)

        dragon_stats = dragon.get_tournament_stats()

        print(f"{dragon_stats['name']} (ID: {dragon_stats['id']}):")

        interfaces = [base.__name__ for base in dragon.__class__.__bases__]

        print(f"- Interfaces: {interfaces}")
        print(f"- Rating: {dragon_stats['rating']}")
        print(f"- Record: {dragon_stats['record']}")

        print()
        wizard = TournamentCard("wizard_001", "Ice Wizard", 6, "common", 11,
                                12, 1150)

        wizard_stats = wizard.get_tournament_stats()

        print(f"{wizard_stats['name']} (ID: {wizard_stats['id']}):")

        interfaces = [base.__name__ for base in wizard.__class__.__bases__]

        print(f"- Interfaces: {interfaces}")
        print(f"- Rating: {wizard_stats['rating']}")
        print(f"- Record: {wizard_stats['record']}")

        tournament = TournamentPlatform()
        tournament.register_card(dragon)
        tournament.register_card(wizard)

        print("\nCreating tournament match...")

        match_result = tournament.create_match(dragon.card_id, wizard.card_id)
        print(f"Match result: {match_result}")

        print("\nTournament Leaderboard:")
        leaderboard = tournament.get_leaderboard()
        for card in leaderboard:
            print(card)

        print("\nPlatform Report:")
        retport = tournament.generate_tournament_report()
        print(retport)

        print("\n=== Tournament Platform Successfully Deployed! ===\n"
              "All abstract patterns working together harmoniously!")

    except ValueError as e:
        print(f"Error: {e}")
