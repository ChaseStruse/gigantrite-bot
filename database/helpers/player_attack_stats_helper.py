def insert_player_attack_stats(connection, stats: dict):
    sql = '''
    INSERT INTO 
    player_attack_stats (attack_stats_id, attack_speed, range, crit_chance,  melee_crit_chance, ranged_crit_chance,
                         magic_crit_chance, heavy_chance, melee_heavy_chance, range_heavy_chance,magic_heavy_chance,
                         hit_chance, melee_hit_chance, range_hit_chance, magic_hit_chance)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    '''

    data = tuple(stats.values())

    connection.execute(sql, data)
    connection.commit()


def format_player_attack_stats_as_dict(data: tuple):
    return {
        "attack_stats_id": data[0],
        "attack_speed": data[1],
        "range": data[2],
        "crit_chance": data[3],
        "melee_crit_chance": data[4],
        "ranged_crit_chance": data[5],
        "magic_crit_chance": data[6],
        "heavy_chance": data[7],
        "melee_heavy_chance": data[8],
        "range_heavy_chance": data[9],
        "magic_heavy_chance": data[10],
        "hit_chance": data[11],
        "melee_hit_chance": data[12],
        "range_hit_chance": data[13],
        "magic_hit_chance": data[14],
    }


def get_player_attack_stats(cursor, _id):
    sql = """SELECT * FROM player_attack_stats WHERE attack_stats_id = ?"""
    data = cursor.execute(sql, (_id,))
    return format_player_attack_stats_as_dict(data=tuple(data)[0])


