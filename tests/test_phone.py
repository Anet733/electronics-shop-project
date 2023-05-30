from src.phone import Phone
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_str():
    assert str(phone1) == 'iPhone 14'


def test_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim():
    assert phone1.number_of_sim == 2


def test_add():
    assert phone1 + phone1 == 10


