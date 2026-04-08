from typing import Callable, List


def spell(target: str, power: int, *args, **kwargs) -> str:
    return f"Spell hits {target} for {power} damage"


def fireball(target: str, power: int, *args, **kwargs) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int, *args, **kwargs) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    pass


def spell_sequence(spells: list[Callable]) -> Callable:
    pass


def main() -> None:
    test_values: List[int] = [12, 14, 15]
    test_targets: List[str] = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    
    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    str1, str2 = combined_spell(test_targets[0], test_values[0])
    print(f"Combined spell result: {str1}, {str2}")


if __name__ == "__main__":
    main()
