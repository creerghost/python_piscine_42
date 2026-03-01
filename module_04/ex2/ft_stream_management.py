import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    arch_id: str = input("Input Stream active. Enter archivist ID: ")
    status: str = input("Input Stream active. Enter status report: ")
    print()
    sys.stdout.write(f"[STANDARD] Archive status from {arch_id}: {status}\n")
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n\n")
    print("Three-channel comminication test successful.")


if __name__ == "__main__":
    ft_stream_management()
