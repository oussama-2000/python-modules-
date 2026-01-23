import math


def parsing(args: str = None, message: bool = True) -> tuple:
    """parsing args to make clean coordinates tuple"""

    try:
        if not args:
            raise TypeError("no coordinates given")
        coords = args.split(",")
        result = []
        for c in coords:
            result += [int(c)]
        result = tuple(result)
        if len(result) != 3: #len !
            raise ValueError("coordinates must be 3 dimensions(x,y,z)")
    except (ValueError, TypeError, AttributeError) as e:
        print(f"Parsing invalid coordinates: \"{args}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    else:
        if message:
            print(f"Parsing coordinates: \"{args}\"")
            print(f"Parsed position: {result}")
        return result


def calculate_distance(position: tuple) -> None:
    """calculate distance between origin position and player position"""
    o_p = (0, 0, 0)
    p_p = position
    distance = math.sqrt(
                        (p_p[0] - o_p[0])**2
                        + (p_p[1] - o_p[1])**2
                        + (p_p[2] - o_p[2])**2
                        )
    print(f"Distance between {o_p} and {p_p} : {distance:.2f}")


def unpacking(coordinates: tuple) -> None:
    """unpacking coordinates to make it visible clearly"""
    print("\nUnpacking demonstration:")

    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]

    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    # test1
    coordinates_1 = parsing("10, 20, 5", False)
    if coordinates_1:
        print(f"Position created: {coordinates_1}")
        calculate_distance(coordinates_1)

    print()
    # test2
    coordinates_2 = parsing("3,4,0")
    if coordinates_2:
        calculate_distance(coordinates_2)

    print()
    # test3
    parsed_coordinates = parsing("abc,def,ghi")
    if parsed_coordinates:
        calculate_distance(parsed_coordinates)

    if coordinates_2:
        print()
        unpacking(coordinates_2)
