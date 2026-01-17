
class Plant:
    """plant class (common features)"""
    def __init__(self, name, height):
        self.name = name
        self.height = height


class Flower(Plant):
    """flower plant type class"""
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(Flower):
    """PrizeFlower plant type class"""
    def __init__(self, name, height, color, prize):
        super().__init__(name, height, color)
        self.prize = prize


class GardenManager:
    """garden manager class"""
    managers = []

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = self.GardenStats(self.plants)
        GardenManager.managers.append(self)

    class GardenStats:
        """inner class for statistics calculation"""
        def __init__(self, plants):
            self.plants = plants
            self.types_count = {
                        "regular": 0,
                        "flowering": 0,
                        "prize_flowers": 0
                                }
            self.plants_number = 0
            self.growth_total = 0

        def count_types(self):
            for plant in self.plants:
                if type(plant) is Plant:
                    self.types_count["regular"] += 1
                elif type(plant) is Flower:
                    self.types_count["flowering"] += 1
                elif type(plant) is PrizeFlower:
                    self.types_count["prize_flowers"] += 1

        def count_plants_number(self):
            for i in self.plants:
                self.plants_number += 1

        def grew(self, value):
            self.growth_total += value

        @staticmethod
        def validate_plant_height(plant):
            """utility function"""
            return plant.height > 0

    # Instance methods
    def add_plant(self, plant):
        self.plants += [plant]
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self, values):
        print(f"{self.owner} is helping all plants grow...")
        j = 0
        for plant in self.plants:
            plant.height += values[j]
            print(f"{plant.name} grew {values[j]}cm")
            self.stats.grew(values[j])
            j += 1

    def generate_report(self):
        print(f"\n=== {self.owner} Garden Report ===")
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

        self.stats.count_plants_number()

        print(f"\nPlants added: {self.stats.plants_number},"
              f"Total growth: {self.stats.growth_total}cm")

        self.stats.count_types()

        print("Plant types:", end=" ")
        print(self.stats.types_count["regular"], "regular", end=" ")
        print(self.stats.types_count["flowering"], "flowering", end=" ")
        print(self.stats.types_count["prize_flowers"], "prize flowers")

    @staticmethod
    def grow_tracker(old_height, new_height):
        value = new_height - old_height
        return value

    @classmethod
    def create_garden_network(cls):
        valid = True

        for manager in cls.managers:
            for plant in manager.plants:
                if cls.stats.validate_plant_height(plant) == 0:
                    valid = False

        print(f"\nHeight validation test: {valid}")

        print("Garden scores - ", end="")
        i = 0
        for manager in cls.managers:

            total_height = 0
            for p in manager.plants:
                total_height += p.height

            prize_points = 0
            for p in manager.plants:
                if type(p) is PrizeFlower:
                    prize_points += p.prize

            growth_bonus = manager.stats.growth_total * 10

            score = total_height + prize_points + growth_bonus
            sep = ", " if i < len(cls.managers) - 1 else ""
            print(f" {manager.owner}: {score}{sep}", end="")
            i += 1
        total_gardens = len(cls.managers)
        print(f"\nTotal gardens managed: {total_gardens}")


print("=== Garden Management System Demo ===", end="\n\n")

plant_1_info = ["Oak Tree", 100, 101]
plant_2_info = ["Rose", 25, "red", 26]
plant_3_info = ["Sunflower", 50, "yellow", 10, 51]


plant1 = Plant(plant_1_info[0], plant_1_info[1])
plant2 = Flower(plant_2_info[0], plant_2_info[1], plant_2_info[2])
plant3 = PrizeFlower(
            plant_3_info[0],
            plant_3_info[1],
            plant_3_info[2],
            plant_3_info[3]
                )


manager1 = GardenManager("Alice")
plants = plant1, plant2, plant3

for i in plants:
    manager1.add_plant(i)

print("\n")

growth_values = [
    GardenManager.grow_tracker(plant_1_info[1], plant_1_info[-1]),
    GardenManager.grow_tracker(plant_2_info[1], plant_2_info[-1]),
    GardenManager.grow_tracker(plant_3_info[1], plant_3_info[-1]),
]

manager1.grow_all(growth_values)

manager1.generate_report()

manager2 = GardenManager("Bob")


manager2.add_plant(Flower("Rose", 92, "red"))


manager1.create_garden_network()
