class GardenError(Exception):
    """for garden problems"""
    pass


class PlantError(GardenError):
    """For problems with plants"""
    pass


class WaterError(GardenError):
    """For problems with watering"""
    pass


def test_custom_errors() -> None:
    """demonstration"""

    print("=== Custom Garden Errors Demo ===")

    plant = {"name": "tomato", "water_level": 0, "sunlight": 1}

    print("\nTesting PlantError...")
    try:
        if plant["sunlight"] < 2:
            raise PlantError(f"The {plant['name']} plant is wilting!")
        else:
            print(f"The {plant['name']} plant sunlight is good")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        if plant["water_level"] < 1:
            raise WaterError("Not enough water in the tank!")
        else:
            print(f"The {plant['name']} plant water level is good")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise PlantError(f"The {plant['name']} plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
