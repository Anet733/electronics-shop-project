"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_calculate_total_price():
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


Item.instantiate_from_csv()


def test_instantiate_from_csv():
    assert len(Item.all) == 10


def test_repr():
    assert repr(item1) == "Item('Смартфон', 8000.0, 20)"
    assert str(item2) == 'Ноутбук'


def test_add():
    assert item1 + phone1 == 25


