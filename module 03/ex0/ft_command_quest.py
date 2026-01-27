import sys


def program() -> None:
    """command interpreter"""
    print("=== Command Quest ===")

    arguments = sys.argv
    arguments_count = len(arguments)
    if not arguments:
        return None
    if arguments_count == 1:
        print("No arguments provided!")

    print(f"Program name: {arguments[0]}")

    if arguments_count != 1:
        print(f"Arguments received: {arguments_count - 1}")

    i = arguments_count
    j = 1
    while i > 1:
        print(f"Argument {j}: {arguments[j]}")
        i -= 1
        j += 1

    print(f"Total arguments: {arguments_count}")


if __name__ == "__main__":
    program()
