class Plant:
    """plant class"""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.agee = age

    def get_info(self) -> None:
        """shows plant informations"""
        print(f"{self.name}: {self.height}cm, {self.agee} days old")

    def grow(self, value: int) -> None:
        """grows the plant"""
        self.height += value

    def age(self, value: int) -> None:
        """increase the plant age"""
        self.agee += value


def programe_test() -> None:

    plant = Plant("Rose", 25, 30)

    prev_height = plant.height

    growth_value = 6
    aging_value = 6

    print("=== Day 1 ===")

    plant.get_info()
    plant.grow(growth_value)
    plant.age(aging_value)

    print(f"=== Day {aging_value + 1} ===")
    plant.get_info()

    growth = plant.height - prev_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    programe_test()
