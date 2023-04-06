import pytest
from src.item import Item


@pytest.fixture
def test_class():
    return Item("Смартфон", 10000, 20)
