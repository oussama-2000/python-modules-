
def archive_creator() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    file = "new_discovery.txt"
    entries = "[ENTRY 001] New quantum algorithm discovered\n" \
              "[ENTRY 002] Efficiency increased by 347%\n" \
              "[ENTRY 003] Archived by Data Archivist trainee"

    print(f"Initializing new storage unit: {file}")

    with open(file, "w") as f:
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        f.write(entries)
        print(entries)

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file}' ready for long-term preservation.")


if __name__ == "__main__":
    archive_creator()
