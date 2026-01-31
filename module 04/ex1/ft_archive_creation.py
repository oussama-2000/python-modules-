
def archive_creator() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    filename = "new_discovery.txt"
    entries = "[ENTRY 001] New quantum algorithm discovered\n" \
              "[ENTRY 002] Efficiency increased by 347%\n" \
              "[ENTRY 003] Archived by Data Archivist trainee"

    print(f"Initializing new storage unit: {filename}")
    try:
        file = open(filename, "w")
        file.write(entries)
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        print(entries)

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
        file.close()
    except PermissionError:
        print("Error: access deny")


if __name__ == "__main__":
    archive_creator()
