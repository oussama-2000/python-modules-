class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def is_number(input: any) -> bool:
    try:
        float(input)
        return True
    except Exception:
        return False


class GardenManager:
    plants = []

    @classmethod
    def add_plants(cls, plant_list: str):

        print("Adding plants to garden...")
        try:
            if plant_list is None or is_number(plant_list):
                raise PlantError("Error adding plant: no plant list given !")
        except PlantError as e:
            print(e)
        if plant_list is not None and is_number(plant_list) is False:
            for plant in plant_list:
                try:
                    if plant["name"] is None:
                        raise PlantError("Error adding plant: Plant name cannot be empty!")

                    if is_number(plant["name"]):
                        raise PlantError("Error adding plant: Plant name cannot be a number!")

                    cls.plants += [plant]
                    print(f"Added {plant['name']} successfully")
                except GardenError as e:
                    print(e)

    @classmethod
    def water_plants(cls):
        print("Watering plants...")
        plant_list = cls.plants
        print("Opening watering system")
        try:
            for plant in plant_list:
                if plant["name"]:
                    print(f"Watering {plant['name']} - success")
                else:
                    raise WaterError("Error:  Cannot water None - invalid plant!")
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(cls) -> None:
        print("Checking plant health...")
        for plant in cls.plants:
            try:
                if plant["name"] is None:
                    raise ValueError("Error checking lettuce: Plant name cannot be empty!")
                elif plant["water"] > 10:
                    raise ValueError("Error checking lettuce: Water level "
                                     f"{plant['water']}"
                                     " is too high (max 10)")
                elif plant["water"] < 1:
                    raise ValueError("Error checking lettuce: Water level "
                                     f"{plant['water']}"
                                     " is too low (min 1)")
                elif plant["sun"] > 12:
                    raise ValueError("Error checking lettuce: Sunlight hours "
                                     f"{plant['sun']}"
                                     " is too high (max 12)")
                elif plant["sun"] < 2:
                    raise ValueError("Error checking lettuce: Sunlight hours "
                                     f"{plant['sun']}"
                                     " is too low (min 2)")
                else:
                    print(f"{plant['name']} : healthy (water: {plant['water']}"
                          f"sun: {plant['sun']}"
                          )
            except ValueError as e:
                print(e)


def test_garden_management() -> None:

    garden1 = GardenManager()

    plants = [
            {"name": "tomato", "water": 5, "sun": 8},
            {"name": "lettuce", "water": 15, "sun": 8},
            {"name": None, "water": 15, "sun": 8}
            ]

    garden1.add_plants(plants)
    print("\n")

    garden1.water_plants()
    print("\n")

    garden1.check_plant_health()


if __name__ == "__main__":
    test_garden_management()
