import string


def c_isspace(s: any) -> bool:
    """helper function to check whitespaces"""
    if not s:
        return True
    try:
        for char in s:
            if char not in string.whitespace:
                return False
    except TypeError:
        return False
    return True


def is_number(input: any) -> bool:
    """helper function to check numbers"""
    try:
        float(input)
        return True
    except Exception:
        return False


def water_plants(plant_list: list = None) -> None:
    """waters plants"""

    print("Opening watering system")
    error_exists = 0
    try:
        if is_number(plant_list):
            raise TypeError("Error: plants must be a list not number !")

        if c_isspace(plant_list):
            raise TypeError("Error: no plant list given!")

        for plant in plant_list:
            if is_number(plant) is False and c_isspace(plant) is False:
                print(f"Watering {plant}")
            else:
                raise ValueError("Error:  Cannot water None - invalid plant!")
    except (ValueError, TypeError) as e:
        error_exists = 1
        print(e)
    finally:
        print("Closing watering system (cleanup)")
    if error_exists == 0:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    """demonstration"""
    print("=== Garden Watering System ===\n")
    plant_list = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(plant_list)

    print("\n")

    print("Testing with error...")
    plant_list = ["tomato", " ", "carrots"]
    water_plants(plant_list)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
