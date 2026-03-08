from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    if not artifacts:
        raise ValueError("no artifacts provided !")
    if not isinstance(artifacts, List):
        raise ValueError("artifacts Type must be list !")
    if not all(isinstance(a, Dict) for a in artifacts):
        raise ValueError("artifacts list items must be dict Type !")

    sorted_artifacts = sorted(artifacts,
                              key=lambda c: c['power'],
                              reverse=True)
    return sorted_artifacts


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    if not mages:
        raise ValueError("no mages provided !")
    if not isinstance(mages, List):
        raise ValueError("mages Type must be list !")
    if not all(isinstance(a, Dict) for a in mages):
        raise ValueError("mages list items must be dict Type !")
    if not isinstance(min_power):
        raise ValueError("min power Type should be integer")

    filtered = filter(lambda m: m['power'] >= min_power, mages)
    return list(filtered)


def spell_transformer(spells: List[str]) -> List[str]:
    if not spells:
        raise ValueError("no spells provided !")

    transformed = map(lambda a: f"* {a} *", spells)
    return list(transformed)


def mage_stats(mages: List[Dict]) -> Dict:
    if not mages:
        raise ValueError("no mages provided !")
    if not isinstance(mages, List):
        raise ValueError("mages Type must be list !")
    if not all(isinstance(a, Dict) for a in mages):
        raise ValueError("mages list items must be dict Type !")

    stats = {
        'max_pwer': 0,
        'min_pwer': 0,
        'avg_power': 0,
    }

    stats['max_pwer'] = max(mages, key=lambda a: a['power'])
    stats['min_pwer'] = min(mages, key=lambda a: a['power'])
    mages_sum = sum(map(lambda a: a['power'], mages))
    stats['avg_power'] = round((mages_sum / len(mages)), 2)

    return stats


if __name__ == "__main__":
    try:
        artifacts = [
            {'name': "Fire Staff", 'power': 92, 'element': "ddd"},
            {'name': "Crystal Orb", 'power': 85, 'element': "ggg"}
        ]

        print("\nTesting artifact sorter...")
        sorted_artifacts = artifact_sorter(artifacts)

        print(
            f"{sorted_artifacts[0]['name']} "
            f"({sorted_artifacts[0]['power']} power)"
            f" comes before {sorted_artifacts[1]['name']} "
            f"({sorted_artifacts[1]['power']} power)"
        )

        print()
        print("Testing spell transformer...")

        spells = ["fireball", "heal", "shield"]
        transformed = spell_transformer(spells)
        for item in transformed:
            print(item, end=" ")
        print()

    except Exception as e:
        print(f"Error: {e}")
