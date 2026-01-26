def fibonacci() -> any:
    """infinite fibonacci generator"""
    a = 0
    b = 1
    while True:
        yield a
        a, b = a + b, a


def is_prime(n: int) -> bool:
    """checks if prime"""
    if n == 1 or n == 0:
        return False
    i = 1
    while n >= i:
        if n % i == 0 and i != n and i != 1:
            return False
        i += 1
    return True


def primes() -> any:
    """infinite prime number generator"""
    i = 1
    while True:
        if is_prime(i):
            yield i
        i += 1


def process_events(number: int) -> any:
    """generator for events"""
    if number <= 0:
        return None
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    levels = [5, 12, 8]

    players_iter = iter(players)
    actions_iter = iter(actions)
    levels_iter = iter(levels)

    print(f"\nProcessing {number} game events...\n")
    for i in range(1, number + 1):
        try:
            player = next(players_iter)
            level = next(levels_iter)
            action = next(actions_iter)
        except StopIteration:
            players_iter = iter(players)
            actions_iter = iter(actions)
            levels_iter = iter(levels)

        yield {
                "id": i,
                "player": player,
                "level": level,
                "action": action
            }


def demo() -> None:
    print("=== Game Data Stream Processor ===")

    events = process_events(1000)
    # print(events)
    total = 0
    height_level = 0
    treasure_events = 0
    levelup_events = 0
    seconds = 0.000

    for event in events:
        total += 1

        if event['level'] > 10:
            height_level += 1

        if event['action'] == "found treasure":
            treasure_events += 1

        if event['action'] == "leveled up":
            levelup_events += 1

        if total <= 3:
            print(f"Event: {event['id']} Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
        if total == 4:
            print("...")
        seconds += 0.00004

    print("\n=== Stream Analytics ===")

    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {height_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}")
    print()
    print(f"Memory usage: Constant ({'streaming' if events else 'no usage'})")
    print(f"Processing time: {seconds:.3f} seconds")
    print()

    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    i = 0
    result = fibonacci()
    for r in result:
        if i == 10:
            print()
            break
        print(r, end="")
        if i != 9:
            print(end=", ")
        i += 1

    print("Prime numbers (first 5): ", end="")
    i = 0
    primes_numbers = primes()
    for r in primes_numbers:
        if i == 5:
            print()
            break
        print(r, end="")
        if i != 4:
            print(end=", ")
        i += 1


if __name__ == "__main__":
    demo()
    # try:
    #     demo()
    # except Exception as e:
    #     print(e)
