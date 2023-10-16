from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard
import pytest


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 5)


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120000, 5, 2)


@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)

