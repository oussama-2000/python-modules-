
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

    print("\nSimulating aggressive turn...")
    hand = [
        factory.create_creature("dragon"),
        factory.create_creature("goblin"),
        factory.create_artifact("Bolt")
        ]

    print("Hand:", [f"{card.name} ({card.cost})" for card in hand])

    print("Turn execution:")
    aggressive = AggressiveStrategy()
    print(f"Strategy: {aggressive.get_strategy_name()}")

    actions = aggressive.execute_turn(hand, [])

    print(f"Actions: {actions}")

    print("\nGame Report:")
    
