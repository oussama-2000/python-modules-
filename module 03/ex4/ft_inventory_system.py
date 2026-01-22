import sys


def is_number(char: any) -> bool:
    for c in char:
        if not '0' <= c <= '9' and c != '.':
            return False
    return True


def search(arg: str) -> True:
    _ = False
    counter = 0
    for c in arg:
        if c == ':':
            counter += 1
            _ = True
        if counter > 1:
            return False
    if _:
        return True
    return False


def parsing() -> dict:

    args = sys.argv
    args_count = len(args) - 1

    if args_count == 0:
        print("you enter nothing !")
        return None
    args = args[1:]

    items = dict()
    for arg in args:
        # check ':' position
        if search(arg) is False or arg[0] == ':' or arg[-1] == ':':
            print("given units must be in this form <unit:unit_count> <...>")
            return None

        # check types
        part_1 = ""
        i = 0
        while arg[i] != ':':
            part_1 += arg[i]
            i += 1
        if is_number(part_1):
            print("unit name must not be an integer !")
            return None
        i += 1
        part_2 = ""
        while i < len(arg):
            part_2 += arg[i]
            i += 1
        if is_number(part_2) is False:
            print("unit count must be integer!")
            return None
        items.update({part_1: part_2})

    print(items)


if __name__ == "__main__":
    parsing()
