class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"Plant: {self.name.capitalize()}")
        print(f"  Height: {self._height:.1f}cm")
        print(f"  Age: {self._age} days")

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self._has_bloomed = False

    def show(self) -> None:
        super().show()
        print(f"  Color: {self.color}")
        print(f"  Has bloomed: {self._has_bloomed}")

    def bloom(self) -> None:
        self._has_bloomed = True
        print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):

    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"  Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"{self.name.capitalize()} is providing nice shade!")


class Vegetable(Plant):

    def __init__(self, name: str, height: float, age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"  Harvest season: {self.harvest_season}")
        print(f"  Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 2


def main():
    rose = Flower("rose", 25.0, 30, "red")
    print("=== Flower ===")
    rose.show()
    rose.bloom()
    print()

    oak = Tree("oak", 200.0, 365, 30.5)
    print("=== Tree ===")
    oak.show()
    oak.produce_shade()
    print()

    tomato = Vegetable("tomato", 15.0, 20, "summer")
    print("=== Vegetable (initial) ===")
    tomato.show()
    print()

    print("=== Vegetable after growth ===")
    tomato.grow()
    tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()