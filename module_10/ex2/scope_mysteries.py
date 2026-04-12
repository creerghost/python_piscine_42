from typing import Callable, Dict, Any, List


def mage_counter() -> Callable[[], int]:
    count: int = 1

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> Dict[str, Callable]:
    vault: Dict[str, List[Any]] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = [value]

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter = mage_counter()
    for i in range(3):
        print(f"Call {i+1}: {counter()}")

    print("\nTesting enchantment factory...")
    fire_enchant = enchantment_factory("Flaming")
    ice_enchant = enchantment_factory("Frozen")
    print(fire_enchant("Sword"))
    print(ice_enchant("Shield"))

    print("\nTesting spell accumulator (initial = 10)...")
    accumulator = spell_accumulator(10)
    print(f"Accumulator: {accumulator(20)}")
    print(f"Accumulator: {accumulator(30)}")
    print(f"Accumulator: {accumulator(40)}\n")

    print("Testing memory vault...")
    vault = memory_vault()
    secret = "hello"
    print(f"Store 'secret' = {secret}")
    print(f"Return value of inner function 'secret':"
          f" {vault['store']('secret', secret)}")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('awodawjopd')}\\n")

    print("Testing vault with unexisting inner function...")
    try:
        print(f"{vault['hello']('ajwdajwkd')}")
    except KeyError:
        print("KeyError: 'hello' function not found")

# class MemoryVault:
#     def __init__(self) -> None:
#         self._vault: Dict[str, Any] = {}

#     def store(self, key: str, value: Any) -> None:
#         self._vault[key] = [value]

#     def recall(self, key: str) -> Any:
#         return self._vault.get(key, "Memory not found")


# def main():
#     vault = MemoryVault()
#     secret = "hello"
#     print(f"Store 'secret' = {secret}")
#     vault.store("secret", secret)
#     print(f"Recall 'secret': {vault.recall('secret')}")

if __name__ == "__main__":
    main()
