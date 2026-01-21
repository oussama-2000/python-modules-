import sys


def parsing() -> list:
    """parsing the user input to make a clean scores list"""
    arguments = sys.argv
    arguments_count = len(arguments) - 1

    if arguments_count == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return None
    i = arguments_count
    j = 1
    scors = []
    try:
        while i > 0:
            arg = int(arguments[j])
            scors += [arg]
            i -= 1
            j += 1
    except ValueError:
        print("make sure you enter valid scores")
        return None

    return scors


def analyse(scors: list) -> None:
    """analyses given scores"""

    print(f"Scores processed: {scors}")
    print(f"Total players: {len(scors)}")
    print(f"Total score {sum(scors)}")

    min_s = min(scors)
    max_s = max(scors)
    average = sum(scors) / len(scors)
    print(f"Average score: {average}")
    print(f"High score: {max_s}")
    print(f"Low score: {min_s}")
    s_range = max_s - min_s
    print(f"Score range: {s_range}")


if __name__ == "__main__":

    print("=== Player Score Analytics ===")
    result = parsing()
    if result:
        analyse(result)
    print()
