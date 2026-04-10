from typing import List, Dict, Any


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda x: f"*{x}*", spells))


def mage_stats(mages: List[Dict]) -> Dict[str, Any]:
    return {"max_power": max(mages, key=lambda x: x["power"]),
            "min_power": min(mages, key=lambda x: x["power"]),
            "avg_power": round(sum(x["power"] for x in mages) / len(mages), 2)
            }


def main() -> None:
    artifacts: List[Dict] = [{'name': 'Ice Wand', 'power': 99,
                             'type': 'armor'},
                             {'name': 'Shadow Blade', 'power': 65,
                             'type': 'relic'},
                             {'name': 'Water Chalice', 'power': 100,
                             'type': 'relic'},
                             {'name': 'Lightning Rod', 'power': 95,
                             'type': 'relic'}]
    mages: List[Dict] = [{'name': 'Ash', 'power': 79, 'element': 'lightning'},
                         {'name': 'Sage', 'power': 60, 'element': 'fire'},
                         {'name': 'Alex', 'power': 92, 'element': 'fire'},
                         {'name': 'Nova', 'power': 65, 'element': 'lightning'},
                         {'name': 'Vova', 'power': 61, 'element': 'wind'}]
    spells: List[str] = ['freeze', 'darkness', 'lightning', 'tornado']

    print("Testing artifact sorter...")
    [print(f"{art['name']}: {art['power']} power")
     for art in artifact_sorter(artifacts)]
    print()

    print("Testing power filter (min_power = 70)...")
    [print(f"{mage['name']}: {mage['power']} power")
     for mage in power_filter(mages, 70)]
    print()

    print("Testing spell transformer...")
    [print(f"{spell}", end=" ") for spell in spell_transformer(spells)]
    print("\n")

    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(f"Mages: {', '.join([f"{mage['name']}: {mage['power']} power"
                               for mage in mages])}")
    print(f"Max power: {stats['max_power']['power']} ({stats['max_power']
                                                       ['name']})")
    print(f"Min power: {stats['min_power']['power']} ({stats['min_power']
                                                       ['name']})")
    print(f"Average power: {stats['avg_power']}")


if __name__ == "__main__":
    main()
