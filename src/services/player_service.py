from ..models.character import Character


def create_character(name: str, attributes: dict, stats: dict) -> Character:
    """
    Allows user to create a character that can be referenced with other functions within the bot
    :param name: Character Name
    :param attributes: Character Strength, Dexterity, Wisdom, and Perception
    :param stats: Character Attack, Crit, Hit, Protection, Health, Resistence
    :return: Character object
    """
    new_character = Character(name=name, attributes=attributes, stats=stats)
    return new_character

