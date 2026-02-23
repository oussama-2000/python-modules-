

def record_spell(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire import validate_ingredients

    validation = validate_ingredients(ingredients)

    if validation == "VALID":
        return (
            f"Spell recorded: {spell_name} ({validation}])"
        )

    return (
            f"Spell rejected: {spell_name} ({validation})"
        )
