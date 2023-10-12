from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 5)


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120000, 5, 2)

