class Plant:
    """plant class"""

    def __init__(self, name: str, s_height: int, s_age: int) -> None:
        self.name = name
        self.s_height = s_height
        self.s_age = s_age

        print(f"Created : {self.name} ({self.s_height}cm, {self.s_age} days)")


def protram_test() -> None:

    plant_1 = ["Rose", 25, 30]
    plant_2 = ["Oak", 200, 365]
    plant_3 = ["Cactus", 5, 90]
    plant_4 = ["Sunflower", 80, 45]
    plant_5 = ["Fern", 15, 120]

    plants = plant_1, plant_2, plant_3, plant_4, plant_5

    plants_number = 0
    print("=== Plant Factory Output ===")

    for plant in plants:
        Plant(plant[0], plant[1], plant[2])
        plants_number += 1

    print(f"\nTotal plants created: {plants_number}")


if __name__ == "__main__":
    protram_test()
