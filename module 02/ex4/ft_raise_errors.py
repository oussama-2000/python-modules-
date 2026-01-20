
def check_plant_health(plant_name: str = None,
                       water_level: int = None,
                       sunlight_hours: int = None
                       ) -> None:

    try:
        if (plant_name is None and
           water_level is None and
           sunlight_hours is None):
            raise ValueError("Error: no parameter !")
        if plant_name is None:
            raise ValueError("Error: Plant name cannot be empty!")
        elif water_level > 10:
            raise ValueError(f"Error: Water level {water_level} "
                             "is too high (max 10)")
        elif water_level < 1:
            raise ValueError(f"Error: Water level {water_level} "
                             "is too low (min 1)")
        elif sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             "is too high (max 12)")
        elif sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             "is too low (min 2)")
        else:
            print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(e)


def test_plant_checks() -> None:

    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    check_plant_health("tmato", 7, 10)

    print("\n")

    print("Testing empty plant name...")
    check_plant_health(None, 7, 10)
    print("\n")

    print("Testing bad water level...")
    check_plant_health("tomato", 15, 10)
    print("\n")

    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 7, 0)
    print("\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
