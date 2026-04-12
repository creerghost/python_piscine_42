from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable, Any, Dict, List
from operator import add, mul


def spell_reducer(spells: List[int], operation: str) -> int:
    if spells == []:
        return 0
    res = reduce(lambda x, y:
                 add(x, y) if operation == "add"
                 else mul(x, y) if operation == "multiply"
                 else max(x, y) if operation == "max"
                 else min(x, y) if operation == "min"
                 else 0, spells)
    if res == 0:
        raise ValueError("Invalid operation")
    return res


def enchantment(power: int, element: str, target: str) -> str:
    return f"{element} {target} with {power} power!"


def partial_enchanter(base_enchantment: Callable[[int, str, str],
                                                 str]) -> Dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "Fire"),
        "ice": partial(base_enchantment, 50, "Ice"),
        "lightning": partial(base_enchantment, 50, "Lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(spell: Any) -> str:
        return f"Unknown spell type: {spell}"

    @dispatcher.register(int)
    def _(damage: int) -> str:
        return f"Direct Damage Spell: {damage} HP"

    @dispatcher.register(str)
    def _(enchantment: str) -> str:
        return f"Applied enchantment: {enchantment}"

    @dispatcher.register(list)
    def _(multi_cast: List[Any]) -> str:
        return f"Multi-casting: {', '.join(multi_cast)}"

    return dispatcher


def main() -> None:
    print("Testing spell reducer...")
    spells = [1, 2, 3, 4, 5]
    print(f"Sum of spells: {spell_reducer(spells, 'add')}")
    print(f"Product of spells: {spell_reducer(spells, 'multiply')}")
    print(f"Max of spells: {spell_reducer(spells, 'max')}")
    print(f"Min of spells: {spell_reducer(spells, 'min')}")
    try:
        print(f"Invalid operation: {spell_reducer(spells, 'invalid')}")
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting partial enchanter...")
    enchanter = partial_enchanter(enchantment)
    print(f"Fire enchantment: {enchanter['fire']('Dragon')}")
    print(f"Ice enchantment: {enchanter['ice']('Dragon')}")
    print(f"Lightning enchantment: {enchanter['lightning']('Dragon')}")

    print("\nTesting memoized Fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"Direct damage: {dispatcher(100)}")
    print(f"Enchantment: {dispatcher('Flaming')}")
    print(f"Multi-cast: {dispatcher(['Fireball', 'Heal', 'Fireball'])}")
    print(f"Unknown spell: {dispatcher(None)}")


if __name__ == "__main__":
    main()
