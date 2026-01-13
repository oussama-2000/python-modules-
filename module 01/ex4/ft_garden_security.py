class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def set_height(self, new_height):
        if (new_height > 0):
            self.height = new_height
            print(f"Height updated: {self.height}cm [OK]")
        else:
            print("Invalid operation attempted: ", end="")
            print(f"height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, new_age):
        if (new_age > 0):
            self.age = new_age
            print(f"Age updated: {self.age} days [OK]")
        else:
            print("Invalid operation attempted: ", end="")
            print(f"age {new_age}cm [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age


plant = SecurePlant("Rose", 19, 28)
print("=== Garden Security System ===")
print(f"Plant created: {plant.name}")
plant.set_height(25)
plant.set_age(30)
print("\n")
plant.set_height(-5)
print("\n")
print(f"Current plant: {plant.name} ({plant.get_height()}cm,"
      f"{plant.get_age()} days)")
