import sys


def parse_args(args: list[str]) -> dict[str:int]:
    return {arg.split(":")[0]: int(arg.split(":")[1])
            for arg in args}


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    argc = len(sys.argv)
    if argc == 1:
        print("No items provided. Usage: python3 ft_inventory_system.py"
              " <item1:amount> <item2:amount> ...")
    else:
        inventory = parse_args(sys.argv[1:])
        print(inventory.values())


if __name__ == "__main__":
    ft_inventory_system()