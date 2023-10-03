from src.item import Item
import pytest


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 5)
