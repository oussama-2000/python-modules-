def check_temperature(temp_str):
    try:
        deg = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if deg > 40:
        raise ValueError(f"{deg}°C is too hot for plants (max 40°C)")
    if deg < 0:
        raise ValueError(f"{deg}°C is too cold for plants (min 0°C)")

    print(f"Temperature {deg}°C is perfect for plants!")
    return deg


def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"\nTesting temperature: {value}")
        try:
            check_temperature(value)
        except ValueError as e:
            print(f"Error: {e}")

    print("\nAll tests completed- program didn't crash!")
