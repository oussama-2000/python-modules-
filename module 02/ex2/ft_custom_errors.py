class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


def raise_plant_error():
    raise PlantError("The tomato plant is wilting!")


def raise_water_error():
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise_plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        raise_water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")
test_custom_errors()