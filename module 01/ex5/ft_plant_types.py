class Plant:
    """plant class with common features"""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """flower plant type class"""

    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """bloom ability method"""

        print(f"{self.name} is blooming beautifully!")

    def show_char(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm,"
              f" {self.age} days, {self.color} color")


class Tree(Plant):
    """tree plant type class"""

    def __init__(
            self,
            name: str,
            height: str,
            age: str,
            trunk_diameter: int
            ):

        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """produce shade ability method"""

        shade_area = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def show_char(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm,"
              f" {self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """vegetable plant type class"""

    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str
            ):

        super().__init__(name, height, age)
        self.season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutritional_value(self) -> None:
        """shows nutritional value method"""

        print(f"{self.name} is rich in {self.nutritional_value}")

    def show_char(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm,"
              f" {self.age} days, {self.season} harvest")


def protram_test() -> None:

    print("=== Garden Plant Types ===", end="\n\n")

    rose = Flower("Rose", 25, 30, "red")
    _ = Flower("Tulip", 20, 25, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    _ = Tree("Orange", 100, 300, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    _ = Vegetable("Carrot", 30, 70, "spring", "vitamin A")

    rose.show_char()
    rose.bloom()
    print("\n")
    oak.show_char()
    oak.produce_shade()
    print("\n")
    tomato.show_char()
    tomato.show_nutritional_value()


if __name__ == "__main__":
    protram_test()
