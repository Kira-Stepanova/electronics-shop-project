"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_Item_init(test_class):
    assert test_class.name == "Смартфон"
    assert test_class.price == 10000
    assert test_class.quantity == 20


def test_calculate_total_price(test_class):
    assert test_class.calculate_total_price() == 200000
