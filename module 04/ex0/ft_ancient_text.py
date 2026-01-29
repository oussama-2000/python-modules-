

def reader() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file}")
    try:
        with open(file, "r") as file:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            print(file.read())
    except FileNotFoundError:
        print("ERROR: Storage Value Not Found")
    else:
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    reader()
