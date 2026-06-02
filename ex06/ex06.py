class Plant:

    class Statistics:

        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"    grow() calls: {self.grow_calls}")
            print(f"    age() calls: {self.age_calls}")
            print(f"    show() calls: {self.show_calls}")

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = height
        self._age = age
        self._stats = Plant.Statistics()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls, height: float, age: int):
        return cls("Anonymous", height, age)

    def show(self) -> None:
        self._stats.show_calls += 1
        print(f"Plant: {self.name.capitalize()}")
        print(f"  Height: {self._height:.1f}cm")
        print(f"  Age: {self._age} days")

    def grow(self) -> None:
        self._stats.grow_calls += 1
        self._height += 0.8

    def age(self) -> None:
        self._stats.age_calls += 1
        self._age += 1

    def get_stats(self):
        return self._stats


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self._has_bloomed = False

    def show(self) -> None:
        super().show()
        print(f"  Color: {self.color}")

    def bloom(self) -> None:
        self._has_bloomed = True
        print(f"{self.name.capitalize()} is blooming!")


class Seed(Flower):

    def __init__(self, name: str, height: float, age: int, color: str, seed_count: int):
        super().__init__(name, height, age, color)
        self.seed_count = seed_count

    def show(self) -> None:
        super().show()
        print(f"  Seed count: {self.seed_count}")


class Tree(Plant):

    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def show(self) -> None:
        super().show()
        print(f"  Trunk diameter: {self.trunk_diameter:.1f}cm")
        print(f"  produce_shade() calls: {self._shade_calls}")

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"{self.name.capitalize()} is providing shade!")


def display_stats(plant: Plant) -> None:
    print(f"\n=== Statistics for {plant.name.capitalize()} ===")
    stats = plant.get_stats()
    stats.display()
    if isinstance(plant, Tree):
        print(f"  (Additional tree stats shown in show() method)")


def main():
    print("=== Garden Analytics ===\n")

    print("Static method test:")
    print(f"Is age 400 older than a year? {Plant.is_older_than_year(400)}")
    print(f"Is age 300 older than a year? {Plant.is_older_than_year(300)}")
    print()

    print("Anonymous plant creation:")
    anonymous = Plant.create_anonymous(10.0, 5)
    anonymous.show()
    print()

    print("Seed creation:")
    sunflower_seed = Seed("Sunflower", 0.5, 1, "yellow", 50)
    sunflower_seed.show()
    print()

    rose = Flower("Rose", 25.0, 30, "red")
    oak = Tree("Oak", 200.0, 400, 35.0)

    print("=== Simulating plant actions ===")
    rose.grow()
    rose.grow()
    rose.age()
    rose.show()

    oak.produce_shade()
    oak.produce_shade()
    oak.grow()
    oak.show()

    display_stats(rose)
    display_stats(oak)


if __name__ == "__main__":
    main()