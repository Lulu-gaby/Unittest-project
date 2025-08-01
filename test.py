import pytest
from main import count_vowels

def test_all_vowels():
    assert count_vowels("аеиоуыэюяАЕИОУЫЭЮЯ") == len("аеиоуыэюяАЕИОУЫЭЮЯ")

def test_no_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0

def test_mixed_string():
    assert count_vowels("Привет друзья!") == 4

def test_empty_string():
    assert count_vowels("") == 0

@pytest.mark.parametrize("input_string, expected_count", [
    ("Учеба", 3),
    ("Тест", 1),
    ("1234", 0),
    ("Поздравляю!", 4),
])
def test_parametrized(input_string, expected_count):
    assert count_vowels(input_string) == expected_count