class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


# object creatin
plant_1 = Plant("Rose", 25, 30)
plant_2 = Plant("Sunflower", 80, 45)
plant_3 = Plant("Cactus", 15, 120)
print("=== Garden Plant Registry ===")
plant_1.show()
plant_2.show()
plant_3.show()
