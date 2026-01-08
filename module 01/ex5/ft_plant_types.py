class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def show_char(self):
        print(f"{self.name} (Flower): {self.height}cm,"
              f" {self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.meters = trunk_diameter

    def produce_shade(self):
        # Area = π × r²
        raduis = self.meters / 2
        square_raduis = raduis * raduis
        square_meters = 3.14 * square_raduis
        print(f"{self.name} provides {square_meters:.0f} square meters of shade")

    def show_char(self):
        print(f"{self.name} (Tree): {self.height}cm,"
              f" {self.age} days, {self.meters}cm diameter")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.season = harvest_season
        self.value = nutritional_value

    def show_nutritional_value(self):
        print(f"{self.name} is rich in {self.value}")

    def show_char(self):
        print(f"{self.name} (Vegetable): {self.height}cm,"
              f" {self.age} days, {self.season} harvest")


print("=== Garden Plant Types ===", end="\n\n")

rose = Flower("Rose", 25, 30, "red")
tulip = Flower("Tulip", 20, 25, "yellow")

oak = Tree("Oak", 500, 1825, 50)
orange = Tree("Orange", 100, 300, 40)

tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
carrot = Vegetable("Carrot", 30, 70, "spring", "vitamin A")

rose.show_char()
rose.bloom()
print("\n")
oak.show_char()
oak.produce_shade()
print("\n")
tomato.show_char()
tomato.show_nutritional_value()
