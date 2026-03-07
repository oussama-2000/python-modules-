

def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    sorted_artifacts = sorted(artifacts,
                              key=lambda c: c['power'],
                              reverse=True)
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered = filter(lambda m: m['power'] >= min_power, mages)
    return list(filtered)


def spell_transformer(spells: list[str]) -> list[str]:
    transformed = map(lambda a: f"* {a} *", spells)
    return list(transformed)


def mage_stats(mages: list[dict]) -> dict:
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

    artifacts = [
        {'name': "Fire Staff", 'power': 92, 'element': "ddd"},
        {'name': "Crystal Orb", 'power': 85, 'element': "ggg"}
    ]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)

    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
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
