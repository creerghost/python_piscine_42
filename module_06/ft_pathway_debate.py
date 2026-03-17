import alchemy.transmutation
from alchemy.transmutation import lead_to_gold, stone_to_gem


def ft_pathway_debate() -> None:
    print("\n=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}\n")

    print("Testing Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")
    print(f"elixir_of_life(): {alchemy.transmutation.elixir_of_life()}\n")

    print("Testing Package Access:")
    print(f"alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): [same as above]\n")
    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    ft_pathway_debate()
