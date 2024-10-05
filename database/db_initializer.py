import sqlite3
from helpers import player_defense_stats_helper, player_attack_stats_helper, player_helper


def create_db_connection():
    return sqlite3.connect("gigantrite.db")


def create_tables(cur):
    cur.execute("CREATE TABLE player(name, level, strength, dexterity, wisdom, perception, attack_stats_id, "
                "defense_stats_id)")
    cur.execute("CREATE TABLE player_attack_stats("
                "attack_stats_id, attack_speed, range, crit_chance,  melee_crit_chance, ranged_crit_chance, "
                "magic_crit_chance, heavy_chance, melee_heavy_chance, range_heavy_chance,magic_heavy_chance, "
                "hit_chance, melee_hit_chance, range_hit_chance, magic_hit_chance"
                ")")
    cur.execute("CREATE TABLE player_defense_stats("
                "defense_stats_id, damage_reduction, melee_defense, range_defense, magic_defense, melee_evasion, "
                "range_evasion, magic_evasion, magic_endurance"
                " )")


def get_all_tables(cur):
    return cur.execute("SELECT name FROM sqlite_master")


if __name__ == '__main__':
    connection = create_db_connection()

    cursor = connection.cursor()
