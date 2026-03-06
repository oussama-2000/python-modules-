

def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    sorted_artifacts = sorted(artifacts,
                              key=lambda c: c['power'],
                              reverse=True)
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    pass


if __name__ == "__main__":
    artifacts = [
        {'name': "artifact1", 'power': 6, 'element': "ddd"},
        {'name': "artifact2", 'power': 1, 'element': "ggg"},
        {'name': "artifact3", 'power': 2, 'element': "ccc"},
    ]
    print(artifact_sorter(artifacts))
