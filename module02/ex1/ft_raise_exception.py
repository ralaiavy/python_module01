def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)

    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    elif temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")

    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    print("Input data is '25'")
    try:
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("Input data is 'abc'")
    try:
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("Input data is '100'")
    try:
        temperature = input_temperature("100")
        print(f"Temperature is now {temperature}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("Input data is '-50'")
    try:
        temperature = input_temperature("-50")
        print(f"Temperature is now {temperature}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()