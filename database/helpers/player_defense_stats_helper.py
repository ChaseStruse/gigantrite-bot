def insert_player_defense_stats(connection, stats: dict):
    sql = '''
    INSERT INTO 
    player_defense_stats (defense_stats_id, damage_reduction, melee_defense, range_defense,magic_defense, melee_evasion, 
                          range_evasion, magic_evasion, magic_endurance) 
    VALUES(?,?,?,?,?,?,?,?,?)
    '''

    data = tuple(stats.values())

    connection.execute(sql, data)
    connection.commit()


def format_player_defense_stats_as_dict(data: tuple):
    return {
        "defense_stats_id": data[0],
        "damage_reduction": data[1],
        "melee_defense": data[2],
        "range_defense": data[3],
        "magic_defense": data[4],
        "melee_evasion": data[5],
        "range_evasion": data[6],
        "magic_evasion": data[7],
        "magic_endurance": data[8]
    }


def get_player_defense_stats(cursor, _id):
    sql = """SELECT * FROM player_defense_stats WHERE defense_stats_id = ?"""
    data = cursor.execute(sql, (_id,))
    return format_player_defense_stats_as_dict(data=tuple(data)[0])


