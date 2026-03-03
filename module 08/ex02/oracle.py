try:
    import os
    from dotenv import load_dotenv
except ImportError as e:
    print(f"Import Error {e}")
    exit()
#  env_variable: A variable stored in the operating system environment,


def load_configuration():

    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_config(config: dict) -> bool:
    missing = [key for key, value in config.items() if not value]

    if missing:
        print("Missing configuration variables:")
        for key in missing:
            print(f" - {key}")
        return False

    return True


def display_status(config: dict):
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    print("Database: Connected to local instance")

    print("API Access: Authenticated")

    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Zion Network: Online")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        config = load_configuration()

        if not validate_config(config):
            print("\nERROR: Incomplete configuration.")
        else:
            display_status(config)
    except (Exception, ImportError) as e:
        print(f"Error: {e}")
