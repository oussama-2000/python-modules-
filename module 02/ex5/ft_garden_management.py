import string


class GardenError(Exception):
    """custum garden Error Error"""
    pass


class PlantError(GardenError):
    """custum plant Error Error"""
    pass


class WaterError(GardenError):
    """custum water Error Error"""
    pass


def is_number(input: any) -> bool:
    """helper function to check numbers"""
    try:
        float(input)
        return True
    except Exception:
        return False


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


class GardenManager:
    """garden manager class"""
    plants = []

    @classmethod
    def add_plant(cls, plant: list = None) -> None:
        """adds plant to garden"""
        try:
            if is_number(plant) or c_isspace(plant):
                raise PlantError("Error adding plant: no plant list given !")
        except PlantError as e:
            print(e)
        if plant and is_number(plant) is False and c_isspace(plant) is False:
            try:
                # validate plant name
                if is_number(plant[0]):
                    raise PlantError("Error adding plant: Plant name"
                                     " cannot be a number!")

                if plant[0] is None or c_isspace(plant[0]):
                    raise PlantError("Error adding plant: Plant name"
                                     " cannot be empty!")

                # validate plant water level
                if is_number(plant[1]) is False or c_isspace(plant[1]):
                    raise PlantError("Error adding plant: Plant water"
                                     " level must be int!")

                # validate plant sunlight
                if is_number(plant[2]) is False or c_isspace(plant[2]):
                    raise PlantError("Error adding plant: Plant sunlight"
                                     " must be int!")

                cls.plants += [plant]
                print(f"Added {plant[0]} successfully")
            except GardenError as e:
                print(e)

    @classmethod
    def water_plants(cls) -> None:
        """waters plants"""
        plant_list = cls.plants
        print("Opening watering system")
        try:
            for plant in plant_list:
                if plant[0]:
                    print(f"Watering {plant[0]} - success")
                else:
                    raise WaterError("Error:  Cannot water None -"
                                     " invalid plant!")
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(cls) -> None:
        """checks plants health"""
        for plant in cls.plants:
            try:
                if plant[1] > 10:
                    raise WaterError("Error checking lettuce: Water level "
                                     f"{plant[1]}"
                                     " is too high (max 10)")
                elif plant[1] < 1:
                    raise WaterError("Error checking lettuce: Water level "
                                     f"{plant[1]}"
                                     " is too low (min 1)")
                elif plant[2] > 12:
                    raise PlantError("Error checking lettuce: Sunlight hours "
                                     f"{plant[2]}"
                                     " is too high (max 12)")
                elif plant[2] < 2:
                    raise PlantError("Error checking lettuce: Sunlight hours "
                                     f"{plant[2]}"
                                     " is too low (min 2)")
                else:
                    print(f"{plant[0]} : healthy (water: {plant[1]}"
                          f" sun: {plant[2]})"
                          )
            except GardenError as e:
                print(e)


def test_garden_management() -> None:
    """demonstration"""
    print("=== Garden Management System ===\n")

    garden1 = GardenManager()

    plant1 = ["tomato", 5, 8]
    plant2 = ["lettuce", 15, 6]
    plant3 = [None, 7, 8]

    plants = plant1, plant2, plant3
    print("Adding plants to garden...")
    for plant in plants:
        garden1.add_plant(plant)

    print("\nWatering plants...")
    garden1.water_plants()

    print("\nChecking plant health...")
    garden1.check_plant_health()

    plant1[1] = 0
    print("\nTesting error recovery...")
    try:
        for plant in plants:
            if plant[1] < 1:
                raise WaterError("Not enough water in the tank")
            else:
                print(f"The {plant[1]} plant water level is good")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
