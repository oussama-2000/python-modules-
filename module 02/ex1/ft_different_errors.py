def garden_operations() -> None:
    """demonstrates common errors"""
    print("Testing ValueError...")
    try:
        input = "abc"
        int(input)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        _ = 1 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'")

    print("\nTesting KeyError...")
    try:
        garden = {"rose": 1}
        print(garden["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")


def test_error_types() -> None:
    """demonstrate single and multiple errors"""
    print("=== Garden Error Types Demo ===\n")
    garden_operations()

    print("\nTesting multiple errors together...")
    try:
        int("abc")
        _ = 1 / 0
    except (ValueError, ZeroDivisionError):
        pass
    finally:
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
