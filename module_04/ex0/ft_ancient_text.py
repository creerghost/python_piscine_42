def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        filename: str = "ancient_fragment.txt"
        print(f"Accessing Storage Vault: {filename}")
        file = open(filename, "r")
        print("Connection established...\n")
        print(file.read())
        print("\nData recovery complete. Storage unit disconnected.")
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    ft_ancient_text()
