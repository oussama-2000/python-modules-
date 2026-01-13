def check_temperature(temp_str):

    try:
        deg = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    else:
        if deg > 40:
            print(f"Error: {deg}°C is too hot for plants (max 40°C)")
        elif deg < 0:
            print(f"Error: {deg}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {deg}°C is perfect for plants!")
            print("\nAll tests completed - program didn't crash!")


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")
    inp = input("Testing temperature: ")
    check_temperature(inp)
test_temperature_input()