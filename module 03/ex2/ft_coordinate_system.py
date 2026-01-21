import sys
import math

# p1 = (0, 0, 0)
# p2 = (10, 20, 5)

# distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])** 2 + (p2[2] - p2[2])**2)

# print(distance)

def parsing() -> tuple:
    args = sys.argv.split()
    args_count = len(args) - 1

    try:
        if args_count != 3:
            raise Exception("coordinates must be in this form x, y, z")
        coords = []
        i = args_count
        j = 1
        while i > 0:
            coords += [args[j]]
            i -= 1
            j += 1
    except Exception as e:
        print(e)
    else:
        print(coords)

if __name__ == "__main__":
    parsing()
