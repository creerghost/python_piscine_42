from functools import wraps
from typing import Callable, Any
import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Spell {func.__name__} completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power')
            if power is None and len(args) >= 3:
                power = args[2]
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying {i} time")
            return (f"Spell {func.__name__} failed after "
                    f"{max_attempts} attempts")
        return wrapper
    return decorator


@spell_timer
def fireball() -> str:
    time.sleep(0.2)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def bad_spell(state: list = [0]) -> str:
    state[0] += 1
    if state[0] <= 5:
        raise Exception
    return "Spell cast!"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(c.isalpha() or c == ' ' for c in name):
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def main() -> None:
    print("Testing spell timer...")
    spell = fireball()
    print(f"Result:{spell}\n")

    print("Testing retrying spell...")
    print(bad_spell())

    print("\nTesting MageBuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("GG"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fire", 5))


if __name__ == "__main__":
    main()
