class Plant:
    def __init__(self, name, s_height, s_age):
        self.name = name
        self.s_height = s_height
        self.s_age = s_age

    def get_info(self):
        print(f"Created : {self.name} ({self.s_height}cm, {self.s_age} days)")


plants = {1: ["Rose", 25, 30], 2: ["Oak", 200, 365], 3: ["Cactus", 5, 90],
          4: ["Sunflower", 80, 45], 5: ["Fern", 15, 120]}
plants_number = 0
print("=== Plant Factory Output ===")
for key, val in plants.items():
    key = Plant(val[0], val[1], val[2])
    key.get_info()
    plants_number += 1
print(f"\nTotal plants created: {plants_number}")
