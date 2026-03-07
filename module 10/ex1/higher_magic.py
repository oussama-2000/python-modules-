

def spell_combiner(spell1: callable, spell2: callable) -> callable:

    def caller(arg: str) -> tuple:
        t1 = spell1(arg)
        t2 = spell2(arg)

        return (t1, t2)
    return caller


def power_amplifier(base_spell: callable, multiplier: int) -> callable:

    def multiplication() -> int:
        return base_spell() * multiplier
    return multiplication


def conditional_caster(condition: callable, spell: callable) -> callable:

    def caster(target: str) -> str:
        if condition(target):
            return spell(target)
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:

    def caster(target: str) -> list:
        spell_result = []

        for spell in spells:
            spell_result.append(spell(target))
        return spell_result
    return caster


if __name__ == "__main__":

    print("Testing spell combiner...")

    def fireball(target) -> str:
        return f"Fireball hits {target}"

    def heal(target) -> str:
        return f"Heals {target}"

    combined = spell_combiner(fireball, heal)

    print(
        "Combined spell result: "
        f"{combined('Dragon')[0]}"
        f"{combined('Dragon')[1]}"
        )

    print("\nTesting power amplifier...")

    def spell() -> int:
        return 10

    multiplication = power_amplifier(spell, 3)
    Amplified = multiplication()
    print(
        f"Original: {spell()}"
        f", Amplified: {Amplified}"
    )

    def condition(target: str) -> bool:
        return target == "dragon"

    def spell_to_cast(target: str) -> str:
        return f"{target} casted"

    casting = conditional_caster(condition, spell_to_cast)
    # print(casting("dragon"))

    def spell_1(target: str) -> str:
        return f"spell 1: {target}"

    def spell_2(target: str) -> str:
        return f"spell 2: {target}"

    def spell_3(target: str) -> str:
        return f"spell 3: {target}"

    sequence = spell_sequence([spell_1, spell_2, spell_3])
    # print(sequence("dragon"))
