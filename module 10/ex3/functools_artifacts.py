from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import List, Callable, Dict
# reduce() : taks a collection and reduce it to one singel value
# partial : give you ability to change a function signature
# lru_cache : used to optimize function performance by
#             storing the results of expensive function calls


def spell_reducer(spells: List[int], operation: str) -> int:
    if not spells:
        raise ValueError("no spells provided !")
    if not isinstance(spells, List):
        raise ValueError("spells type should be List !")
    if not all(isinstance(a, int) for a in spells):
        raise ValueError("spells items type should be integer !")
    if not isinstance(operation, str) or not operation:
        raise ValueError("Invalid operation type !")

    suported = ['add', 'multiply', 'max', 'min']
    result = None
    if operation in suported:
        if operation == 'add':
            result = reduce(add, spells)
        elif operation == 'multiply':
            result = reduce(mul, spells)
        elif operation == 'max':
            result = reduce(lambda a, b: max(a, b), spells)
        elif operation == 'min':
            result = reduce(lambda a, b: min(a, b), spells)
    else:
        result = "unsuported operation"
    return result


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    if not isinstance(base_enchantment, Callable):
        raise ValueError("base_enchantment type should be function !")

    fire_enchant = partial(
        base_enchantment,
        50,
        "fire",
        )
    ice_enchant = partial(
        base_enchantment,
        50,
        "ice",
        )
    lightning_enchant = partial(
        base_enchantment,
        50,
        "light",
        )

    return {
        'fire_enchant': fire_enchant,
        'ice_enchant': ice_enchant,
        'lighting_enchant': lightning_enchant
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("n should be integer !")

    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:

    @singledispatch
    def process(data: any) -> str:
        return f"Default spell processing: {data}"

    @process.register(int)
    def _(data: int) -> str:
        return f"Ingeger spell processing: {data}"

    @process.register(str)
    def _(data: str) -> str:
        return f"String spell processing: {data}"

    @process.register(list)
    def _(data: List) -> str:
        return f"List spell processing: {data}"

    return process


if __name__ == "__main__":
    try:
        # print("\nTesting spell reducer...")
        # spells = [10, 20, 30, 40]
        # sum_reducer = spell_reducer(spells, "add")
        # product_reducer = spell_reducer(spells, "multiply")
        # max_reducer = spell_reducer(spells, "max")

        # print(f"Sum: {sum_reducer}")
        # print(f"Product: {product_reducer}")
        # print(f"Max: {max_reducer}")

        # def base_enchantment(power: int, element: str, target: str) -> str:
        #     return f"{element}: {power} on {target}"

        # partials = partial_enchanter(base_enchantment)
        # print(partials['fire_enchant']('card1'))
        # print(partials['ice_enchant']('card2'))
        # print(partials['lighting_enchant']('card3'))

        # print("\nTesting memoized fibonacci...")
        # print(f"Fib(10): {memoized_fibonacci(10)}")
        # print(f"Fib(15): {memoized_fibonacci(15)}")

        process = spell_dispatcher()
        print(process("hello"))

    except Exception as e:
        print(f"Error: {e}")
