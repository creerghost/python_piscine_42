import sys

def ft_score_analytics() -> None:
    argc: int = len(sys.argv)
    scores: list[int] = []
    [scores.append(int(sys.argv[i + 1])) for i in range (0, argc - 1)]
    print("=== Player Score Analytics ===")

    if argc == 1:
        print(f"No scores provided. Usage: python3 ft_score_analytics.py"
              f" <score1> <score2> ...")
    else:
        print(f"Scores processed: [", end = '')
        [print(scores[i], end = ', ') for i in range (0, argc - 2)]
        print(f"{scores[argc - 2]}]\n")

        print(f"Total players: {argc - 1}\n")
        print(f"Total score: {sum(scores)}")

if __name__ == "__main__":
    ft_score_analytics()
