"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 5)


def test_init():
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 5


def test_calculate_total_price():
    assert item1.calculate_total_price() == 50000


def test_apply_discount():
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 5000


def test_name():
    assert item1.name == 'Смартфон'

    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_string_to_number():
    assert Item.string_to_number('7') == 7


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[1].name == 'Ноутбук'
