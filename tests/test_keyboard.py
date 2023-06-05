import pytest
from src.keyboard import KeyBoard

kb = KeyBoard('Dark Project KD87A', 9600, 5)


def test_init():
    assert str(kb) == "Dark Project KD87A"


def test_str():
    assert str(kb.language) == "EN"


def test_change_lang():
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
