class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.agee = age

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.agee} days old")

    def grow(self):
        self.height += 6

    def age(self):
        self.agee += 6


plant = Plant("Rose", 25, 30)
print("=== Day 1 ===")
plant.get_info()
plant.grow()
plant.age()
print("=== Day 7 ===")
plant.get_info()
print("Growth this week: +6cm")
