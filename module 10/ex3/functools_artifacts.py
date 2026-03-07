from functools import reduce
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    result = None

    if operation == 'add':
        result = reduce(add, spells)
    elif operation == 'multiply':
        result = reduce(mul, spells)
    elif operation == 'max':
        result = reduce(max, spells)
    elif operation == 'min':
        result = reduce(min, spells)

    return result


spells = [1, 2, 3]
sum_reducer = spell_reducer(spells, "add")
product_reducer = spell_reducer(spells, "multiply")

print(f"Sum: {sum_reducer}")
print(f"Product {product_reducer}")
