def garden_operations(num: str = None, zero: str = None,
                      file_path: str = None, key: dict = None) -> tuple:
    num_converted: int = None
    num_zero_test: int = None
    file_content: str = None
    key_content: dict = None
    if num is not None:
        num_converted = int(num)
    if zero is not None:
        num_zero_test = 123 / int(zero)
    if file_path is not None:
        file_content = open(file_path, "r")
        file_content.close()
    if key is not None:
        key_content = key["missing_plant"]
    return num_converted, num_zero_test, file_content, key_content


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    try:
        print("Testing ValueError...")
        garden_operations(num="abc")
        print("Everything is good!")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    try:
        print("Testing ZeroDivisionError...")
        garden_operations(zero="0")
        print("Everything is good!")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    try:
        print("Testing FileNotFoundError...")
        garden_operations(file_path="missing.txt")
        print("Everything is good!")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'")
    print()

    try:
        print("Testing KeyError...")
        garden_operations(key={"name": "rose"})
        print("Everything is good!")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()

    try:
        print("Testing multiple errors together...")
        garden_operations("abc", "0", "missing.txt", {"name": "rose"})
        print("Everything is good!")
    except Exception:
        print("Caught an error, but program continues!")
    print()

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
