def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt' ...")
    try:
        with open("lost_archive.txt", "r") as file:
            print(f"{file.read}\nRESPONSE: File is accessed.")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")

    filename: str = ("classified_vault.txt")
    print(f"CRISIS ALERT: Attempting access to '{filename}'...")
    try:
        with open(filename, 'r') as file:
            print(f"{file.read()}\nRESPONSE: Access granted.")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")

    filename = "standard_archive.txt"
    print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    try:
        with open(filename, 'r') as file:
            print(f"SUCCESS: Access recovered - '{file.read()}'")
    except Exception:
        print("RESPONSE: Something is wrong...")
    print("STATUS: Normal operations resumed\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
