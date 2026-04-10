import sys
import os
import site
#  python3 -m venv matrix_env
#  source matrix_env/bin/activate
#  deactivate


def is_in_venv() -> bool:
    """
    Detects whether the program is running inside a virtual environment.

    When a virtual environment is activated, sys.prefix points to the
    virtual environment's directory, while sys.base_prefix continues to
    point to the global Python installation directory. If they differ,
    we are safely inside the construct.
    """
    try:
        return sys.prefix != sys.base_prefix
    except AttributeError:
        return hasattr(sys, 'real_prefix')


def display_outside_venv() -> None:
    """
    Displays warnings and instructions when
    running in the global environment.
    """
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate    # On Windows\n")
    print("Then run this program again.")


def display_inside_venv() -> None:
    """
    Displays environment details
    when safely inside a virtual environment.
    """
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")

    try:
        venv_path: str = sys.prefix
        venv_name: str = os.path.basename(venv_path)

        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting"
              " the global system.\n")

        print("Package installation path:")

        # site.getsitepackages() gets the paths
        # where packages are installed
        site_packages = site.getsitepackages()
        for path in site_packages:
            if 'site-packages' in path:
                print(path)
                break
        else:
            if site_packages:
                print(site_packages[0])

    except Exception as e:
        print(f"Error reading package paths: {e}")


def main() -> None:
    """Main execution function handling the environment check."""
    try:
        if is_in_venv():
            display_inside_venv()
        else:
            display_outside_venv()
    except Exception as e:
        print(f"A glitch in the Matrix occurred: {e}")


if __name__ == "__main__":
    main()
