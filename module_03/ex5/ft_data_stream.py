import time
from typing import Generator


def game_event_generator(count: int) -> Generator[dict, None, None]:
    players: list[str] = ["alice", "bob", "charlie", "david"]
    actions: list[str] = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, count + 1):
        event_data = {
            "id": i,
            "player": players[i % len(players)],
            "level": (i * 7) % 20 + 1,
            "action": actions[i % len(actions)]
        }
        yield event_data


def ft_fibonacci_generator(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def ft_prime_generator(n: int) -> Generator[int, None, None]:
    count, num = 0, 2
    while count < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1


def ft_data_stream():
    high_level_players: int = 0
    treasure_events: int = 0
    level_up_events: int = 0

    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    start_time: int = time.perf_counter()

    for event in game_event_generator(1000):
        if event['id'] <= 3:
            print(f"Event {event['id']}: Player {event['player']}"
                  f" (level {event['level']}) {event['action']}")
        elif event['id'] == 4:
            print("...")

        if event["level"] >= 10:
            high_level_players += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        elif event["action"] == "leveled up":
            level_up_events += 1
    print()
    end_time: int = time.perf_counter()

    print("=== Stream Analytics ===")
    print("Total events processed: 1000")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}\n")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds\n")

    print("=== Generator Demonstration ===")

    fib = [str(x) for x in ft_fibonacci_generator(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fib)}")

    primes = [str(x) for x in ft_prime_generator(5)]
    print(f"Prime numbers (first 5): {', '.join(primes)}")


if __name__ == "__main__":
    ft_data_stream()
