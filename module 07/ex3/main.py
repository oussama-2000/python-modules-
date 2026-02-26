from ex3.CardFactory import CardFactory
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy

if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()

    print(f"Factory: {FantasyCardFactory.__name__}")
    print(f"Strategy: {AggressiveStrategy.__name__}")

    available_types = factory.get_supported_types()

    print(f"Available types: {available_types}")

