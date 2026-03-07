
def mage_counter() -> callable:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter
    return count


def spell_accumulator(initial_power: int) -> callable:

    total_power = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:

    def enchantment(name: str) -> str:
        return f"{enchantment_type} {name}"
    return enchantment


def memory_vault() -> dict[str, callable]:
    vaults = {}

    def store(key: str, value: str) -> None:
        vaults[key] = value

    def recall(key: str) -> str:
        result = vaults.get(key, "Memory not found")
        return result
    return {'store': store, 'recall': recall}


if __name__ == "__main__":

    print("Testing mage counter...")
    x = mage_counter()
    print(f"Call 1: {x()}")
    print(f"Call 2: {x()}")
    print(f"Call 3: {x()}")

    # accumulator = spell_accumulator(5)
    # print(f"call 1: {accumulator(5)}")
    # print(f"call 2: {accumulator(5)}")
    # print(f"call 3: {accumulator(1)}")

    print("\nTesting enchantment factory...")
    enchantment_1 = enchantment_factory("Flaming")
    print(enchantment_1("sword"))
    enchantment_2 = enchantment_factory("Frozen")
    print(enchantment_2("Shield"))

    # memory = memory_vault()
    # store = memory['store']
    # store('name', 'oussama')
    # recall = memory['recall']('name')
    # print(recall)
