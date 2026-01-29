import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

id = input("Input Stream active. Enter archivist ID: ")
status = input("Input Stream active. Enter status report: ")
print()
sys.stdout.write(f"[STANDARD] Archive status from {id}: {status}\n")
sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
sys.stdout.write("[STANDARD] Data transmission complete\n")

print("\nThree-channel communication test successful.")
