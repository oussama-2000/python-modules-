
def analyes() -> dict:
    """analyes data by setting statictics"""
    data = {
        'players': [
            {
                "name": "alice",
                "achi": {'first_kill', 'level_10', 'treasure_hunter',
                         'speed_demon'
                         },
                'score': 2300,
                "region": 'north',
                'status': 'active'
            },
            {
                'name': 'bob',
                'achi': {'first_kill', 'level_10', 'boss_slayer', 'collector'},
                'score': 1800,
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
        'score_categories': {},
        'player_scores': {},
        'achi_count': {},
        'high_scores': [],
        'scores_doubled': [],
        'active_players': [],
        'active_regions': set(),
        'unique_players': set(),
        'unique_achi': set(),
        'total_players': 0,
        'total_unique_achi': 0,
        'average_score': 0,
        'top_performer': [{
            'name': None,
            'points': 0,
            'achi_number': 0
        }]
    }

    # ---- list comprehension ---

    # filtering high scores
    data['high_scores'] = [
        p['name']
        for p in data['players']
        if p['score'] > 2000
        ]

    # find doubled scores
    data['scores_doubled'] = [
        player['score'] * 2
        for player in data['players']
        ]

    # filtering active players
    data['active_players'] = [
        player['name']
        for player in data['players']
        if player['status'] == 'active'
        ]

    # --- dict comprehension ---

    # find player scores
    data['player_scores'] = {
        player['name']: player['score']
        for player in data['players']
        if player['status'] == 'active'
    }

    # find score categories
    high = 0
    medium = 0
    low = 0
    for player in data['players']:
        if player['score'] > 2000:
            high += 1
        elif player['score'] > 1500:
            medium += 1
        else:
            low += 1

    data['score_categories'] = {
        'high': high,
        'medium': medium,
        'low': low
    }

    # find achievement counts
    data['achi_count'] = {
        player['name']: len(player['achi'])
        for player in data['players']
        if player['status'] == 'active'
    }

    # ---- set comprehension ----

    # filtering uniqe players
    data['unique_players'] = {player['name'] for player in data['players']}

    # filtering unique achievements
    data['unique_achi'] = {
        achi for achi in player['achi']
        for player in data['players']
        }

    # filtering active regions
    data['active_regions'] = {
        player['region']
        for player in data['players']
        if player['status'] == 'active'
        }

    # --- compined comprehension ---

    # find total players
    data['total_players'] = len(data['players'])

    # find total unique achivements
    data['total_unique_achi'] = len(data['unique_achi'])

    scores = [player['score'] for player in data['players']]

    # find average score
    data['average_score'] = sum(scores) / data['total_players']

    # find top performer
    top_score = max(scores)

    data['top_performer'] = [
        {
            'name': player['name'],
            'points': player['score'],
            'achi_number': len(player['achi'])
        }
        for player in data['players']
        if player['score'] == top_score
    ]
    return data


def show_stats(data: dict) -> None:
    """show statictics """
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {sorted(data['high_scores'])}\n"
          f"Scores doubled: {data['scores_doubled']}\n"
          f"Active players: {sorted(data['active_players'])}")

    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {data['player_scores']}")

    print(f"Score categories: {data['score_categories']}")
    print(f"Achievement counts: {data['achi_count']}")

    print("\n=== Set Comprehension Examples ===")

    print(f"Unique players: {data['unique_players']}\n"
          f"Unique achievements: {data['unique_achi']}\n"
          f"Active regions: {data['active_regions']}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {data['total_players']}\n"
          f"Total unique achievements: {data['total_unique_achi']}\n"
          f"Average score: {data['average_score']}\n"
          f"Top performer: {data['top_performer'][0]['name']} "
          f"({data['top_performer'][0]['points']} points, "
          f"{data['top_performer'][0]['achi_number']} achievements)"
          )


if __name__ == "__main__":
    try:
        data = analyes()
        if data:
            show_stats(data)
    except Exception as e:
        print(f"Error: {e}")
