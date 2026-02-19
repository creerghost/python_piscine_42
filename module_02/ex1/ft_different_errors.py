def garden_operations(num=None, zero=None, file_path=None, key=None) -> tuple:
    num_converted: int = None
    num_zero_test: int = None
    file_content: str = None
    if num is not None:
        num_converted = int(num)
    if zero is not None:
        num_zero_test = 123 / int(zero)
    if file_path is not None:
        file_content = open(file_path, "r")
        file_content.close()
    if key is not None:
        key_content: dict = key["missing_plant"]
    return num_converted, num_zero_test, file_content, key

def test_error_types():
    print("=== Garden Error Types Demo ===")
    try:
        print("Testing ValueError...")
        number = garden_operations(num="abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    try:
        print("Testing ZeroDivisionError...")
        number = garden_operations(zero="0")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    try:
        print("Testing FileNotFoundError...")
        garden_operations(file_path="missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'")
    print()

    try:
        print("Testing KeyError...")
        garden_operations(key={"name": "rose"})
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()

    try:
        print("Testing multiple errors together...")
        garden_operations("abc", "0", "missing.txt", {"name": "rose"})
    except Exception:
        print("Caught an error, but program continues!")
    print()

    print("All error types tested successfully!")

if __name__ == "__main__":
    test_error_types()
