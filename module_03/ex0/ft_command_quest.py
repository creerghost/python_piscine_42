import sys


def ft_commant_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    argc: int = len(sys.argv)
    if argc == 1:
        print("No arguments provided!")
    if argc > 1:
        print(f"Arguments recieved: {argc - 1}")
    for arg_num in range(1, argc):
        print(f"Argument {arg_num}: {sys.argv[arg_num]}")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    ft_commant_quest()
