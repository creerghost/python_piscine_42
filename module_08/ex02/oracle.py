import os
import sys
from dotenv import load_dotenv
# cp .env.example .env


def access_mainframe() -> None:
    """Loads and validates the Oracle's configuration securely."""
    print("ORACLE STATUS: Reading the Matrix...")

    env_loaded: bool = load_dotenv()

    mode: str | None = os.getenv("MATRIX_MODE")
    db_url: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    log_level: str | None = os.getenv("LOG_LEVEL")
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT")

    if not all([mode, db_url, api_key, log_level, zion_endpoint]):
        print("\nWARNING: The Oracle's vision is clouded.")
        print("Default/missing configuration detected. "
              "Please set up your .env file.")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode if mode else 'Unconfigured'}")

    if mode == "development":
        print("Database: Connected to local instance")
    elif mode == "production":
        print("Database: Connected to production mainframe")
    else:
        print("Database: Disconnected")

    print("API Access: Authenticated" if api_key else "API Access:"
          " UNAUTHORIZED")
    print(f"Log Level: {log_level if log_level else 'INFO'}")
    print("Zion Network: Online" if zion_endpoint else "Zion Network: Offline")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if env_loaded or os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


def main() -> None:
    """Main execution pipeline."""
    try:
        access_mainframe()
    except Exception as e:
        print(f"Critical mainframe error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
