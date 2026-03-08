from typing import Callable, Dict


def mage_counter() -> Callable:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter
    return count


def spell_accumulator(initial_power: int) -> Callable:
    if not isinstance(initial_power, int):
        raise ValueError("initial_power Type should be integer !")

    total_power = initial_power

    def accumulate(amount: int) -> int:
        if not isinstance(amount, int):
            raise ValueError("amount type should be integer !")

        nonlocal total_power
        total_power += amount
        return total_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    if not isinstance(enchantment_type, str) or\
            not enchantment_type:
        raise ValueError("Invalid enchantment_type type !")

    def enchantment(name: str) -> str:
        if not isinstance(name, str) or not name:
            raise ValueError("invalid name type !")

        return f"{enchantment_type} {name}"
    return enchantment


def memory_vault() -> Dict[str, Callable]:
    vaults = {}

    def store(key: any, value: any) -> None:
        if not key or not value:
            raise ValueError("you should provide key and value to stroe !")

        vaults[key] = value

    def recall(key: any) -> any:
        if not key:
            raise ValueError("you should provide key to recall !")

        result = vaults.get(key, "Memory not found")
        return result
    return {'store': store, 'recall': recall}


if __name__ == "__main__":

    try:
        print("Testing mage counter...")
        x = mage_counter()
        print(f"Call 1: {x()}")
        print(f"Call 2: {x()}")
        print(f"Call 3: {x()}")

        # accumulator = spell_accumulator(5)
        # print(f"call 1: {accumulator(5)}")
        # print(f"call 2: {accumulator(5)}")
        # print(f"call 3: {accumulator(1)}")

        # print("\nTesting enchantment factory...")
        # enchantment_1 = enchantment_factory("Flaming")
        # print(enchantment_1("sword"))
        # enchantment_2 = enchantment_factory("Frozen")
        # print(enchantment_2("Shield"))

        # memory = memory_vault()
        # store = memory['store']
        # store('name', 'oussama')
        # recall = memory['recall']('name')
        # print(recall)

    except Exception as e:
        print(f"Error: {e}")
