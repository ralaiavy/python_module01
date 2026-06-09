class GardenError(Exception):

    def __init__(self, message: str = "Unknown garden error occurred"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):

    def __init__(self, message: str = "Unknown plant error occurred"):
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):

    def __init__(self, message: str = "Unknown watering error occurred"):

        self.message = message
        super().__init__(self.message)


def test_plant_problem() -> None:

    raise PlantError("The tomato plant is wilting!")


def test_water_problem() -> None:

    raise WaterError("Not enough water in the tank!")


def test_garden_problem() -> None:

    raise GardenError()


def test_error_types() -> None:

    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        test_plant_problem()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        test_water_problem()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    
    try:
        test_plant_problem()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    
    try:
        test_water_problem()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()