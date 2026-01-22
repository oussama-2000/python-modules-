import sys
import math


def parsing() -> tuple:
    """parsing args to make clean coordinates tuple"""
    args = sys.argv
    args_count = len(args) - 1

    try:
        if args_count < 1:
            print("no coordinates given !")
            return None
        elif args_count > 1:
            print("coordinates form must be as <x,y,z>")
            return None
        else:
            coords = args[1].split(",")
            result = []
            for c in coords:
                result += [int(c)]
            result = tuple(result)
            if len(result) != 3:
                raise ValueError("coordinates must be 3 dimensions(x,y,z)")
    except (ValueError, TypeError) as e:
        print(f"Parsing invalid coordinates: \"{args[1]}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    else:
        print(f"Parsing coordinates: \"{args[1]}\"")
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
    parsed_coordinates = parsing()
    if parsed_coordinates:
        calculate_distance(parsed_coordinates)
        unpacking(parsed_coordinates)
