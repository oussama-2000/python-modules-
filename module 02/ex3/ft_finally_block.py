def water_plants(plant_list):

    print("Opening watering system")
    error_exists = 0
    try:
        if plant_list is None:
            raise TypeError("Error: no plant list was given!")

        for plant in plant_list:
            if plant:
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


def test_watering_system():
    print("=== Garden Watering System ===\n")
    plant_list = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(plant_list)

    print("\n")

    print("Testing with error...")
    plant_list = ["tomato", None, "carrots"]
    water_plants(plant_list)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
