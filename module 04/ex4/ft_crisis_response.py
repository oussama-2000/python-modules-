
def crisis_response() -> None:

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    files = [
            "lost_archive.txt",
            "classified_vault.txt",
            "standard_archive.txt"
             ]
    for file in files:
        try:
            with open(file, "r") as f:
                print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
                print("SUCCESS: Archive recovered - "
                      "``Knowledge preserved for humanity``")
                print("STATUS: Normal operations resumed\n")
                f.read()
        except FileNotFoundError:
            print(f"CRISIS ALERT: Attempting access to '{file}'...")
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")
        except PermissionError:
            print(f"CRISIS ALERT: Attempting access to '{file}'...")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response()
