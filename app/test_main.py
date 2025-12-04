import datetime

from unittest import mock

from app.main import outdated_products


class MyDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls(2022, 2, 10)


def test_data_is_today() -> None:
    products = [
        {
            "name": "tuna",
            "expiration_date": datetime.date(
                2022, 2, 10
            ),
            "price": 400},
    ]

    with mock.patch("app.main.datetime.date", MyDate):
        result = outdated_products(products)

    assert result == []


def test_product_expired() -> None:
    products = [
        {"name": "tuna",
         "expiration_date": datetime.date(
             2022, 2, 11
         ),
         "price": 400},
    ]
    with mock.patch("app.main.datetime.date", MyDate):
        result = outdated_products(products)

    assert result == []


def test_product_is_valid() -> None:
    products = [
        {"name": "tuna",
         "expiration_date": datetime.date(
             2022, 2, 9
         ),
         "price": 400},
    ]
    with mock.patch("app.main.datetime.date", MyDate):
        result = outdated_products(products)

    assert result == ["tuna"]


def test_list_is_empty() -> None:
    products = []
    with mock.patch("app.main.datetime.date", MyDate):
        result = outdated_products(products)

    assert result == []
