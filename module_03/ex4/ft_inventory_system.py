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
        values: int = 0
        keys: int = 0
        max_val: int = -1
        min_val: int = 2147483647
        max_key: str = None
        min_key: str = None
        moderate: set[int] = {}
        scarce: set[int] = {}
        restock_list: list[str] = []
        is_sword: bool = False
        for k, v in inventory.items():
            values += v
            keys += 1
            if v > max_val:
                max_val = v
                max_key = k
            if v < min_val:
                min_val = v
                min_key = k
            if v > 3:
                moderate[k] = v
            else:
                scarce[k] = v
            if k == "sword":
                is_sword = True

        print(f"Total items in inventory: {values}")
        print(f"Unique item types: {keys}\n")

        print("=== Current Inventory ===")
        for k, v in inventory.items():
            if v == 1:
                print(f"{k}: {v} unit ({(v / values * 100):.1f}%)")
            else:
                print(f"{k}: {v} units ({(v / values * 100):.1f}%)")
            if v == min_val:
                restock_list.append(k)
        print()

        print("=== Inventory Statistics ===")
        if max_val == 1:
            print(f"Most abundant: {max_key} ({max_val} unit)")
        else:
            print(f"Most abundant: {max_key} ({max_val} units)")
        if min_val == 1:
            print(f"Least abundant: {min_key} ({min_val} unit)")
        else:
            print(f"Least abundant: {min_key} ({min_val} units)")
        print()

        print("=== Item Categories ===")
        print(f"Moderate: {moderate}")
        print(f"Scarce {scarce}\n")

        print("=== Management Suggestions ===")
        print(f"Restock needed: {restock_list}\n")

        print("=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {list(inventory.keys())}")
        print(f"Dictionary values: {list(inventory.values())}")
        print(f"Sample lookup - 'sword' in inventory: {is_sword}")


if __name__ == "__main__":
    ft_inventory_system()
