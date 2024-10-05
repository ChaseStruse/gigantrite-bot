def insert_player(connection, player_info: dict):
    sql = '''
    INSERT INTO 
    player (name, level, strength, dexterity, wisdom, perception, attack_stats_id, defense_stats_id)
    VALUES(?,?,?,?,?,?,?,?)
    '''

    data = tuple(player_info.values())

    connection.execute(sql, data)
    connection.commit()


def format_player_as_dict(data: tuple):
    return {
        "name": data[0],
        "level": data[1],
        "strength": data[2],
        "dexterity": data[3],
        "wisdom": data[4],
        "perception": data[5],
        "attack_stats_id": data[6],
        "defense_stats_id": data[7],
    }


def get_player(cursor, _id):
    sql = """SELECT * FROM player WHERE name = ?"""
    data = cursor.execute(sql, (_id,))
    return format_player_as_dict(data=tuple(data)[0])


