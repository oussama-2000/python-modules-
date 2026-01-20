class Plant:
    """plant class"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        """shows plant informations"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def protram_test() -> None:
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant_1.show()
    plant_2.show()
    plant_3.show()


if __name__ == "__main__":
    protram_test()
