import sys


def is_number(inp: any) -> bool:
    """checks if number"""
    try:
        int(inp)
        return True
    except Exception:
        return False


def search(arg: str) -> bool:
    """looking for ':' and how many repeatitions"""
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


def most_abundant(items: dict) -> tuple:
    """looking for most aboundant item """
    most = list(items.items())[0]
    contity = list(items.values())[0]
    for i in items.items():
        if i[1] > contity:
            contity = i[1]
            most = i
    return most


def least_abundant(items: dict) -> tuple:
    """looking for least aboundant item"""
    least = list(items.items())[0]
    contity = list(items.values())[0]
    for i in items.items():
        if i[1] < contity:
            contity = i[1]
            least = i
    return least


def find_moderate(items: dict, middle: int) -> dict:
    """looking for moderate items"""
    moderate = {}
    for i in items.items():
        if i[1] > middle:
            moderate.update({i})
    return moderate


def find_scarce(items: dict, middle: int) -> dict:
    """looking for scarce items"""
    scarce = {}
    for i in items.items():
        if i[1] <= middle:
            scarce.update({i})
    return scarce


def find_restock_needed(items: dict) -> list:
    """find item that needs restock"""
    target = []
    for i in items.items():
        if i[1] <= 1:
            target += [i[0]]
    return target


def parsing() -> dict:
    """pars arguments and return clean data as a dictionary"""
    args = sys.argv
    args_count = len(args) - 1

    if args_count == 0:
        print("you enter nothing !")
        return None
    args = args[1:]

    data = dict(
        items={},
        most={
            'name': None,
            'contity': 0
        },
        least={
            'name': None,
            'contity': 0
        },
        moderate={},
        scare={},
        restock_neaded=[],
        total=0,
        unique=0
    )

    for arg in args:
        # check ':' position
        if search(arg) is False or arg[0] == ':' or arg[-1] == ':':
            print("given units must be in this form <unit:unit_count> <...>")
            return None

        # split and check type
        part_1 = ""
        i = 0
        while arg[i] != ':':
            part_1 += arg[i]
            i += 1

        i += 1
        part_2 = ""
        while i < len(arg):
            part_2 += arg[i]
            i += 1

        if is_number(part_2) is False:
            print("unit count must be integer!")
            return None
        data["items"].update({part_1: int(part_2)})

    return data


def analyse(data: dict) -> None:
    """analyse data by seting values"""

    items = data["items"]

    # finding total
    total = 0
    for i in items.values():
        total += i
    data["total"] = total

    # finding unique count
    unique = set()
    for i in items.keys():
        unique.add(i)
    data["unique"] = len(unique)

    # finding most
    most = most_abundant(items)
    data["most"].update({'name': most[0]})
    data["most"].update({'contity': most[1]})

    # finding least
    least = least_abundant(items)
    data["least"].update({'name': least[0]})
    data["least"].update({'contity': least[1]})

    # finding moderate
    print()
    middle = (most[1] + least[1]) / 2
    moderate = find_moderate(data['items'], middle)
    data["moderate"] = moderate

    # finding scarce
    scarce = find_scarce(data['items'], middle)
    data["scarce"] = scarce

    # finding restock needed items
    restock_needed = find_restock_needed(data['items'])
    data["restock_needed"] = restock_needed


def show_stats(data: dict) -> None:
    """show statictics"""
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {data['total']}")
    print(f"Unique item types: {data['unique']}")

    print("\n=== Current Inventory ===")

    items = data['items']
    for i in items.items():
        if data['total'] != 0:
            percentage = (i[1] / data['total']) * 100
            print(f"{i[0]}: {i[1]} {'units' if i[1] > 1 else 'unit'} "
                  f"({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")

    print(f"Most abundant: {data['most']['name']} ({data['most']['contity']} "
          f"{'units' if data['most']['contity'] > 1 else 'unit'})")

    print(f"Least abundant: {data['least']['name']} "
          f"({data['least']['contity']} "
          f"{'units' if data['least']['contity'] > 1 else 'unit'})")

    print("\n=== Item Categories ===")
    print(f"Moderate: {data['moderate']}")
    print(f"Scarce: {data['scarce']}")

    if data['restock_needed']:
        print("\n=== Management Suggestions ===")
        print(f"Restock needed: {data['restock_needed']}")

    print("\n=== Dictionary Properties Demo ===")
    keys = list(items.keys())
    print(f"Dictionary keys: {keys}")

    values = list(items.values())
    print(f"Dictionary values: {values}")

    sample = "sword"
    exsists = True if data['items'].get(sample, False) else False
    print(f"Sample lookup - '{sample}' in inventory: {exsists}")


if __name__ == "__main__":
    try:
        data = parsing()
        if data:
            analyse(data)
            show_stats(data)
    except Exception as e:
        print(f"Error : {e}")
