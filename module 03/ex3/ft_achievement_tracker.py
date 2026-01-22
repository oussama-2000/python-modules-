

def achi_tracker() -> tuple:
    print("=== Achievement Tracker System ===\n")
    player_1 = {
        "name": "Alice",
        "achi": {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    }
    player_2 = {
        "name": "Bob",
        "achi": {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    }
    player_3 = {
        "name": "Charlie",
        "achi": {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                 'perfectionist'}
    }

    players = player_1, player_2, player_3

    for player in players:
        print(f"Player {player['name']} achievements: {player['achi']}")
    return players


def achi_analyse(players: tuple) -> None:

    print("\n=== Achievement Analytics ===")
    player_1, player_2, player_3 = players

    unique_achi = player_1["achi"].union(player_2["achi"], player_3["achi"])
    print(f"All unique achievements : {unique_achi}")
    print(f"Total unique achievements: {len(unique_achi)}")

    print()
    common_achi = player_1["achi"].intersection(player_2["achi"],
                                                player_3["achi"])
    print(f"Common to all players: {common_achi}")

    diff_1_23 = player_1["achi"].difference(player_2["achi"], player_3["achi"])
    diff_2_13 = player_2["achi"].difference(player_1["achi"], player_3["achi"])
    diff_3_12 = player_3["achi"].difference(player_1["achi"], player_2["achi"])

    rare_achi = diff_1_23.union(diff_2_13, diff_3_12)
    print(f"Rare achievements (1 player): {rare_achi}")
    print()

    p_1xp_2 = player_1["achi"].intersection(player_2["achi"])
    print(f"{player_1['name']} vs {player_2['name']} common: {p_1xp_2}")

    p_1 = player_1["achi"].difference(player_2["achi"])
    print(f"{player_1['name']} unique: {p_1}")

    p_2 = player_2["achi"].difference(player_1["achi"])
    print(f"{player_2['name']} unique: {p_2}")


if __name__ == "__main__":
    players_achi = achi_tracker()
    achi_analyse(players_achi)
