#!/usr/bin/env python3

class SecurePlant():
    """Class secure plant. If you enter the wrong input, it will print
    the error."""
    def __init__(self, name: str) -> None:
        """Initializing the variable <name> and initializing the height
        and the age."""
        self.name = name
        self.__height: int = 0
        self.__age: int = 0

    def get_height(self) -> int:
        """Returning the height of plant."""
        return self.__height

    def set_height(self, value: int) -> None:
        """Setting up the height if input is corrent."""
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def get_age(self) -> int:
        """Returning the age of plant."""
        return self.__age

    def set_age(self, value: int) -> None:
        """Setting up the age if input is correct"""
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {value} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    print(f"Current plant: {rose.name} ({rose.get_height()}cm, "
          f"{rose.get_age()} days)")
