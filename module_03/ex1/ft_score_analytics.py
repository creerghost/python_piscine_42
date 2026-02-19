import sys


def ft_score_analytics() -> None:
    argc: int = len(sys.argv)
    scores: list[int] = []
    [scores.append(int(sys.argv[i + 1])) for i in range(0, argc - 1)]
    print("=== Player Score Analytics ===")

    if argc == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {argc - 1}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
