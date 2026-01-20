class SecurePlant:
    """secure plant class"""

    def __init__(self, name: str, height: str, age: int) -> None:
        self.name = name
        self.__height = None
        self.__age = None
        self.set_height(height, 0)
        self.set_age(age, 0)

    def set_height(self, new_height: int, message: int) -> None:
        """setter for set height prorprity"""

        if (new_height > 0):
            self.__height = new_height
            if message:
                print(f"Height updated: {self.__height}cm [OK]")
        else:
            print("Invalid operation attempted: ", end="")
            print(f"height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, new_age: int, message: int) -> None:
        """setter for set age protprity"""

        if (new_age > 0):
            self.__age = new_age
            if message:
                print(f"Age updated: {self.__age} days [OK]")
        else:
            print("Invalid operation attempted: ", end="")
            print(f"age {new_age}cm [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        """getter for get height proprity"""
        return self.__height

    def get_age(self) -> int:
        """getter for get age proprity"""
        return self.__age


def program_test() -> None:

    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 19, 28)
    print(f"Plant created: {plant.name}")

    plant.set_height(25, 1)
    plant.set_age(30, 1)

    print("\n")

    plant.set_height(-5, 1)

    print("\n")

    print(f"Current plant: {plant.name} ({plant.get_height()}cm, "
          f"{plant.get_age()} days)")


if __name__ == "__main__":
    program_test()
