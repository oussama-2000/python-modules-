
def is_doubled(scores: list, target_score: int) -> bool:
    repeate = 0
    for score in scores:
        if score == target_score:
            repeate += 1
    if repeate >= 2:
        return True
    return False


def analyes() -> dict:
    data = {
        'players': [
            {
                "name": "zlice",
                "achi": {'first_kill', 'level_10', 'treasure_hunter',
                         'speed_demon'
                         },
                'score': 4100,
                "region": 'north',
                'status': 'active'
            },
            {
                'name': 'bob',
                'achi': {'first_kill', 'level_10', 'boss_slayer', 'collector'},
                'score': 1700,
                'region': 'east',
                'status': 'unactive'
            },
            {
                'name': 'charlie',
                'achi': {
                        'level_10', 'treasure_hunter', 'boss_slayer',
                        'speed_demon',
                        'perfectionist'
                        },
                'score': 4300,
                'region': 'central',
                'status': 'active'
            },
            {
                'name': 'diana',
                'achi': {
                        'level_10', 'treasure_hunter',
                        'speed_demon',
                        'perfectionist'
                        },
                'score': 4100,
                'region': 'central',
                'status': 'active'
            }
        ],
        'score_categories': {
            'high': [],
            'medium': [],
            'low': []
        },
        'scores_doubled': [],
        'active_players': [],
        'active_regions': set(),
        'unique_players': set(),
        'unique_achi': set(),
        'total_players': 0,
        'total_unique_achi': 0,
        'average_score': 0,
        'top_performer': []
    }

    # find high  medium and low scores
    for player in data['players']:
        if player['score'] > 2000:
            data['score_categories']['high'] += [player['name']]
        elif player['score'] > 1500:
            data['score_categories']['medium'] += [player['name']]
        else:
            data['score_categories']['low'] += [player['name']]

    # find doubled scores
    scores = []
    for player in data['players']:
        scores += [player['score']]

    for score in scores:
        if is_doubled(scores, score) and score not in data['scores_doubled']:
            data['scores_doubled'] += [score]
    # print(data['scores_doubled'])

    # find active players and regions
    for player in data['players']:
        if player['status'] == "active":
            data['active_players'] += [player['name']]
            data['active_regions'].add(player['region'])

    # find unique players and achivements
    for player in data['players']:
        data['unique_players'].add(player['name'])
        for achi in player['achi']:
            data['unique_achi'].add(achi)

    # find total players
    data['total_players'] = len(data['players'])

    # find total unique achivements
    data['total_unique_achi'] = len(data['unique_achi'])

    # find average score
    data['average_score'] = sum(scores) / data['total_players']

    # find top performer
    top_score = max(scores)
    for player in data['players']:
        if player['score'] == top_score:
            data['top_performer'] = [
                                     player['name'], player['score'],
                                     len(player['achi'])
                                    ]
    return data


def show_stats(data: dict) -> None:
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {sorted(data['score_categories']['high'])}\n"
          f"Scores doubled: {data['scores_doubled']}\n"
          f"Active players: {sorted(data['active_players'])}")

    print("\n=== Dict Comprehension Examples ===")
    print("Player scores: {", end="")
    i = 1
    
    for player in data['players']:
        print(f"'{player['name']}': {player['score']}"
              f"{', ' if i < len(data['players']) else ''}", end="")
        i += 1
    print("}")
    print("Score categories: {"
          f"'high' : {len(data['score_categories']['high'])}, "
          f"'medium' : {len(data['score_categories']['medium'])}, "
          f"'low' : {len(data['score_categories']['low'])}"
          "}")
    print("Achievement counts: {", end="")
    i = 1
    for player in data['players']:
        print(f"'{player['name']}': {len(player['achi'])}"
              f"{', ' if i < len(data['players']) else ''}", end="")
        i += 1
    print("}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {data['total_players']}\n"
          f"Total unique achievements: {data['total_unique_achi']}\n"
          f"Average score: {data['average_score']}\n"
          f"Top performer: {data['top_performer'][0]} "
          f"({data['top_performer'][1]} points, "
          f"{data['top_performer'][2]} achievements)"
          )


if __name__ == "__main__":
    try:
        data = analyes()
        if data:
            show_stats(data)
    except Exception as e:
        print(e)
