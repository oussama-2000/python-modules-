from typing import Callable, Tuple, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not isinstance(spell1, Callable):
        raise ValueError("spell1 Type should be a function !")
    if not isinstance(spell2, Callable):
        raise ValueError("spell2 Type should be a function !")

    def caller(arg: str) -> Tuple:
        t1 = spell1(arg)
        t2 = spell2(arg)

        return (t1, t2)
    return caller


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not isinstance(base_spell, Callable):
        raise ValueError("base_spell Type should be function !")
    if not isinstance(multiplier, int):
        raise ValueError("multiplier Type should be integer !")

    def multiplication() -> int:
        return base_spell() * multiplier
    return multiplication


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not isinstance(condition, Callable):
        raise ValueError("condition Type must be function !")
    if not isinstance(spell, Callable):
        raise ValueError("spell should be Function !")

    def caster(target: str) -> str:
        if condition(target):
            return spell(target)
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(spells: List[Callable]) -> Callable:
    if not spells:
        raise ValueError("no spells provided !")
    if not isinstance(spells, List):
        raise ValueError("spells Type should be list !")
    if not all(isinstance(a, Callable) for a in spells):
        raise ValueError("spells items Type should be functions !")

    def caster(target: str) -> List:
        if not isinstance(target, str) or not target:
            raise ValueError("target Type Invalid !")

        spell_result = []

        for spell in spells:
            spell_result.append(spell(target))
        return spell_result
    return caster


if __name__ == "__main__":

    try:
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

        # def condition(target: str) -> bool:
        #     return target == "dragon"
        # def spell_to_cast(target: str) -> str:
        #     return f"{target} casted"
        # casting = conditional_caster(condition, spell_to_cast)
        # print(casting("dragon"))

        # def spell_1(target: str) -> str:
        #     return f"spell 1: {target}"
        # def spell_2(target: str) -> str:
        #     return f"spell 2: {target}"
        # def spell_3(target: str) -> str:
        #     return f"spell 3: {target}"
        # sequence = spell_sequence([spell_1, spell_2, spell_3])
        # print(sequence("dragon"))

    except Exception as e:
        print(f"Error: {e}")
