from alchemy.grimoire import validate_ingredients, record_spell

if __name__ == "__main__":

    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")

    print('validate_ingredients("fire air") ', end="")
    print(validate_ingredients("fire air"))

    print('validate_ingredients("dragon scales"): ', end="")
    print(validate_ingredients("dragon scales"))

    print("\nTesting spell recording with validation:")
    print('record_spell("Fireball", "fire air"): ', end="")
    print(record_spell("Fireball", "fire air"))

    print('record_spell("Dark Magic", "shadow"): ', end="")
    print(record_spell("Dark Magic", "shadow"))

    print("\nTesting late import technique:")
    print('record_spell("Lightning", "air"): ', end="")
    print(record_spell("Lightning", "air"))

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
