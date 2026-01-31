import sys


def stream_manager() -> None:

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print()
    if id and status:
        print(f"[STANDARD] Archive status from {id}: {status}",
              file=sys.stdout)
        print("[ALERT] System diagnostic: Communication channels"
              " verified", file=sys.stderr)
        print("[STANDARD] Data transmission complete", file=sys.stdout)

        print("\nThree-channel communication test successful.")
    else:
        print("Error: no input provided")


if __name__ == "__main__":
    stream_manager()
