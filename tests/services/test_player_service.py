import pytest
from src.models.character import Character
from src.services import player_service as sut


def test_create_character_returns_expected_character():
    test_attributes = {
        "Strength": 10,
        "Dexterity": 20,
        "Wisdom": 30,
        "Perception": 40
    }
    test_stats = {
        "Attack": 100,
        "Crit": 110,
        "Hit": 120,
        "Protection": 130,
        "Health": 140,
        "Resistence": 150
    }
    expected = Character(name="Test", attributes=test_attributes, stats=test_stats)
    actual = sut.create_character(name="Test", attributes=test_attributes, stats=test_stats)

    assert actual.name == expected.name
    assert actual.attributes == expected.attributes
    assert actual.stats == expected.stats


if __name__ == '__main__':
    pytest.main()
