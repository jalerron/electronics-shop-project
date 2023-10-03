"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_init(item1):
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 5


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 50000


def test_apply_discount(item1):
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 5000


def test_name(item1):
    assert item1.name == 'Смартфон'

    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_string_to_number(item1):
    assert item1.string_to_number('7') == 7


def test_instantiate_from_csv(item1):
    item1.instantiate_from_csv('../src/items.csv')
    assert item1.all[0].name == 'Смартфон'
    assert item1.all[1].name == 'Ноутбук'


def test_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 5)"


def test_str(item1):
    assert str(item1) == 'Смартфон'