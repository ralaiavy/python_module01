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


def water_plant(plant_name: str) -> None:
    if plant_name.isupper():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("TOMATO")
        water_plant("LETTUCE") 
        water_plant("CARROTS")
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}")
    finally:
        print("Closing watering system")
    print()

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("TOMATO")
        water_plant("lettuce")  
        water_plant("CARROTS") 
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("Cleanup always happens, even with errors!")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()