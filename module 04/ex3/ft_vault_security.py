
def vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    file = "classified_data.txt"

    print("Initiating secure vault access...")
    try:
        with open(file, "r") as f:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(f.read())

        entries = "[CLASSIFIED] New security protocols archived"
        with open(file, "w") as f:
            print("\nSECURE PRESERVATION:")
            f.write(entries)
            print(entries)
            print("Vault automatically sealed upon completion")

        print("\nAll vault operations completed with maximum security.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print("access deny")


if __name__ == "__main__":
    vault_security()
