def water_plants(plant_list):

    print("Opening watering system")
    try:
        for plant in plant_list:
            if (plant):
                print(f"Watering {plant}")
            else:
                raise ValueError("Error:  Cannot water None - invalid plant!")
        print("Watering completed successfully!")
    except ValueError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


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


test_watering_system()
