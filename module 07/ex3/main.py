
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


if __name__ == "__main__":
    try:
        print("\n=== DataDeck Game Engine ===\n")
        print("Configuring Fantasy Card Game...")
        factory = FantasyCardFactory()

        print(f"Factory: {FantasyCardFactory.__name__}")
        print(f"Strategy: {AggressiveStrategy.__name__}")

        available_types = factory.get_supported_types()

        print(f"Available types: {available_types}")

        print("\nSimulating aggressive turn...")

        game_engine = GameEngine()

        game_engine.configure_engine(FantasyCardFactory(),
                                     AggressiveStrategy())

        print("Hand:", [f"{card.name} ({card.cost})"
                        for card in game_engine.hand])

        print("\nTurn execution:")
        turn = game_engine.simulate_turn()
        print(f"Strategy: {turn['strategy']}")
        print(f"Actions: {turn['result']}")

        print("\nGame Report:")
        print(game_engine.get_engine_status())

        print("\nAbstract Factory + Strategy Pattern: "
              "Maximum flexibility achieved!")

    except ValueError as e:
        print(f"Error: {e}")
