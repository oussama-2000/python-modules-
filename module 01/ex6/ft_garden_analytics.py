class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class Flower(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(Flower):
    def __init__(self, name, height, color, prize):
        super().__init__(name, height, color)
        self.prize = prize


class GardenManager():
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def create_garden_network(self, plant):
        self.plants += [plant]
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_tracker(old_height, new_height):
        value = old_height - new_height
        return value

    def grow_all(self, values):
        print(f"{self.owner} is helping all plants grow...")
        j = 0
        for plant in self.plants:
            plant.height += values[j]
            print(f"{plant.name} grew {values[j]}cm")
            j += 1

    def generate_report(self):
        print("Plants in garden:")
        for plant in self.plants:
            if type(plant) is Plant:
                print(f"- {plant.name}: {plant.height}cm")
            elif type(plant) is Flower:
                print(f"- {plant.name}: {plant.height}cm, {plant.color} "
                      f"flowers (blooming)")
            else:
                print(f"- {plant.name}: {plant.height}cm, {plant.color}"
                      f"flowers (blooming), Prize points: {plant.prize}")




plant_1_info = ["Oak Tree", 100, 101]
plant_2_info = ["Rose", 25, "red", 26]
plant_3_info = ["Sunflower", 50, "yellow", 10, 51]

print("=== Garden Management System Demo ===", end="\n\n")

plant1 = Plant(plant_1_info[0], plant_1_info[1])
plant2 = Flower(plant_2_info[0], plant_2_info[1], plant_2_info[2])
plant3 = PrizeFlower(plant_3_info[0], plant_3_info[1], plant_3_info[2],
                     plant_3_info[3])

garden1 = GardenManager("Alice")
plants = plant1, plant2, plant3

for i in plants:
    garden1.create_garden_network(i)

print("\n")
plant_infos = plant_1_info, plant_2_info, plant_3_info

values = []
for i in plant_infos:
    values += [GardenManager.grow_tracker(plant_infos[0][-1],
               plant_infos[0][1])]

garden1.grow_all(values)

print("\n=== Alice's Garden Report ===")
garden1.generate_report()
