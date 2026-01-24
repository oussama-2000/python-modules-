# # using generator funciton (yield) make noo need to store any data in a variable or what ever

# def reader(filename):
#     file = open(filename)
#     for line in file:
#         yield line



# filename = "file.txt"
# lines = reader(filename)



# while True:
#     try:
#         print(next(lines))
#     except StopIteration:
#         break

def game_event_stream(n):
    """Generator that produces game events on demand"""
    players = ("alice", "bob", "charlie")
    actions = ("killed monster", "found treasure", "leveled up")

    for i in range(1, n + 1):
        yield {
            "id": i,
            "player": players[i % 3],
            "level": (i * 7) % 20,
            "action": actions[i % 3]
        }


def process_events(n):
    print(f"Processing {n} game events...")

    total_events = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    for event in game_event_stream(n):
        total_events += 1

        if event["level"] >= 10:
            high_level_players += 1

        if event["action"] == "found treasure":
            treasure_events += 1

        if event["action"] == "leveled up":
            level_up_events += 1

        if total_events <= 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['action']}"
            )

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print(f"Memory usage: Constant ({'streaming' if event else 'no usage'})")


def fibonacci():
    """Infinite Fibonacci generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def primes():
    """Infinite prime number generator"""
    n = 2
    while True:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n
        n += 1


def generator_demo():
    print("\n=== Generator Demonstration ===")

    fib = fibonacci()
    print("Fibonacci sequence (first 10):", end=" ")
    for _ in range(10):
        print(next(fib), end=", " if _ < 9 else "\n")

    prime_gen = primes()
    print("Prime numbers (first 5):", end=" ")
    for _ in range(5):
        print(next(prime_gen), end=", " if _ < 4 else "\n")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    process_events(1000)
    generator_demo()
