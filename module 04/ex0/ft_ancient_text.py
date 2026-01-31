

def text_recovery() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")
    try:
        file = open(filename, "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage Value Not Found")
    except PermissionError:
        print("ERROR: access deny")
    else:
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    text_recovery()
