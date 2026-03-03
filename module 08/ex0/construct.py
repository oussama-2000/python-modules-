try:
    import sys
    import site
except ImportError as e:
    print(f"Import Error {e}")


def check_venv_existence() -> bool:
    venv = sys.prefix != sys.base_prefix
    return venv


def get_venv_info() -> dict:
    info = {
        'name': None,
        'path': None
    }

    full_path = sys.prefix
    components = full_path.split("/")
    info['name'] = components[-1]
    info['path'] = sys.prefix
    return info


if __name__ == "__main__":

    message = None
    venv_exists = check_venv_existence()
    if venv_exists:
        message = "Welcome to the construct"
    else:
        message = "You're still plugged in"

    print(f"\nMATRIX STATUS: {message}")

    print()
    print(f"Current Python: {sys.executable}")
    if venv_exists:
        print(f"Virtual Envirement: {get_venv_info()['name']}")
    else:
        print("Virtual Envirement: None detected")

    if venv_exists:
        print(f"Envirement Path: {get_venv_info()['path']}")

        print()
        print("SUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting"
              "the global system.")

        print()
        print("Package installation path:")
        print(site.getsitepackages()[0])
    else:
        print("\nWARNING: You're in the global environment!\n"
              "The machines can see everything you install.\n\n"
              "To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\n"
              "Scripts\n"
              "activate      # On Windows\n\n"
              "Then run this program again."
              )
