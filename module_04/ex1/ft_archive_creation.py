def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    filename: str = "new_discovery.txt"
    print(f"Initializing new storage unit: {filename}")
    file = open(filename, "x")
    print("Storage unit created successfully...\n")
    file.close()
    print("Inscribing preservation data...", end=' ')
    file = open(filename, "a")
    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    file.close()
    file = open(filename, "r")
    print()
    print(file.read())
    file.close()

    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    ft_archive_creation()
