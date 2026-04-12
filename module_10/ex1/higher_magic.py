from typing import Callable, Tuple, List, Any


def fireball(target: str, power: int, *args: Any, **kwargs: Any) -> str:
    return (f"Fireball hits {target} with {power} power!"
            if power else f"Fireball hits {target}")


def heal(target: str, power: int, *args: Any, **kwargs: Any) -> str:
    return (f"Heals {target} with {power} power!"
            if power else f"Heals {target}")


def check_power(target: str, power: int) -> bool:
    return power > 50


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]) -> Callable[
                    [str, int], Tuple[str, str]]:
    def combined_spell(*args, **kwargs) -> Tuple[str, str]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined_spell


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    def amplified_spell(*args: Any, **kwargs: Any) -> str:
        return base_spell(*args, **kwargs) * multiplier
    return amplified_spell


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]) -> Callable[[
                        str, int], str]:
    def conditional_spell(*args: Any, **kwargs: Any) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: List[Callable[[str, int], str]]) -> Callable[[
                        str, int], List[str]]:
    def sequence_spell(*args: Any, **kwargs: Any) -> List[str]:
        return [spell(*args, **kwargs) for spell in spells]
    return sequence_spell


def base_power() -> int:
    return 5


def main() -> None:
    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    str1, str2 = combined_spell('Dragon', None)
    print(f"Combined spell result: {str1}, {str2}\n")

    print("Testing power amplifier...")
    before = base_power()
    amplified_spell = power_amplifier(base_power, 2)
    after = amplified_spell()
    print(f"Amplified spell result: {before} --(2x)--> {after}\n")

    print("Testing conditional caster...")
    conditional_spell = conditional_caster(check_power, fireball)
    print(f"Power 51: {conditional_spell('Dragon', 51)}")
    print(f"Power 12: {conditional_spell('Dragon', 12)}\n")

    print("Testing spell sequence...")
    spells = [fireball, heal, fireball, heal]
    sequence = spell_sequence(spells)
    results = sequence('Dragon', 12)
    for i, res in enumerate(results):
        print(f"Spell {i}: {res}")


if __name__ == "__main__":
    main()
