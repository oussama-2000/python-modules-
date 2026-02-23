import alchemy.elements
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_water
from alchemy.potions import strength_potion


if __name__ == "__main__":

    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print(
        "alchemy.elements.create_fire(): "
        f"{alchemy.elements.create_fire()}"
        )

    print("\nMethod 2 - Specific function import:")
    print(
        "create_water(): "
        f"{create_water()}"
    )

    print("\nMethod 3 - Aliased import:")
    print(
        "heal(): "
        f"{heal()}"
    )

    print("\nMethod 4 - Multiple imports:")
    print(
        "create_rearth(): "
        f"{create_earth()}"
        "\ncreate_fire(): "
        f"{create_fire()}"
        "\nstrength_potion(): "
        f"{strength_potion()}"
    )

    print("\nAll import transmutation methods mastered!")
