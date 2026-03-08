# A decorator is a function that wraps another function to modify its behavior.
from functools import wraps
import time
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    if not isinstance(func, Callable):
        raise ValueError("func type should be function !")

    @wraps(func)
    def wrapper(*args, **s) -> any:
        print(f"Casting function: {func.__name__} ...")
        start_time = time.time()
        result = func(*args, **s)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Spell completed in {execution_time:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    if not isinstance(min_power, int):
        print("dkdkdk")
        raise ValueError("min power type should be integer !")

    def container(func: Callable) -> Callable:
        if not isinstance(func, Callable):
            raise ValueError("func type should be function !")

        @wraps(func)
        def validate(*args, **s) -> None | int:
            try:
                power = None
                if "power" in s.keys():
                    power = s["power"]
                else:
                    power = args[-1]

                if not isinstance(power, int):
                    return "Insufficient power for this spell"

                if power >= min_power:
                    return func(*args, **s)
                else:
                    return "Insufficient power for this spell"
            except IndexError:
                return "Insufficient power for this spell"
        return validate
    return container


def retry_spell(max_attempts: int) -> Callable:
    if not isinstance(max_attempts, int):
        raise ValueError("invalid max attempts type !")

    def container(func):
        @wraps(func)
        def wrapper(*args, **s):

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **s)

                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")

            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return container


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str):
            return False

        check = True
        for i in name:
            if not i.isalpha() and i != " ":
                check = False

        if len(name) >= 3 and check:
            return True

        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        if not spell_name or not power:
            raise ValueError("spell name and power required !")
        if not isinstance(power, int):
            raise ValueError("invalid power type !")

        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    try:
        print("\nTesting spell timer...")

        @spell_timer
        def hello():
            return "Fireball cast!"

        print(f"Result: {hello()}")

        # @power_validator(1)
        # def spell(power: int):
        #     return f"verified : {power}"

        # print(spell(1))

        # @retry_spell(2)
        # def spell():
        #     raise ValueError
        # spell()

        print("\nTesting MageGuild...")
        guild = MageGuild()
        print(guild.validate_mage_name("    "))
        print(guild.validate_mage_name(""))
        print(guild.cast_spell("faireball", 15))
        print(guild.cast_spell("faireball", 9))

    except Exception as e:
        print(f"Error: {e}")
