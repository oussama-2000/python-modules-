import sys
import math

# p1 = (0, 0, 0)
# p2 = (10, 20, 5)

# distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])** 2 + (p2[2] - p2[2])**2)

# print(distance)


def parsing() -> tuple:
    args = sys.argv
    args_count = len(args) - 1

    error = False
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
                raise TypeError("coordinates must be 3 dimensions(x,y,z)")
    except Exception as e:
        error = True
        print(f"Parsing invalid coordinates: \"{args[1]}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    else:
        if not error:
            print(f"Parsing coordinates: \"{args[1]}\"")
        print(result)


if __name__ == "__main__":
    parsing()
