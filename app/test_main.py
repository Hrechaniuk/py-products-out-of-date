import datetime

from unittest import mock
from unittest.mock import Mock

from app.main import outdated_products


@mock.patch("app.main.datetime.date.today")
def test_data_is_today(today_mock: Mock) -> None:
    today_mock.return_value = datetime.date(2022, 2, 10)

    products = [
        {"name": "tuna", "expiration_date": datetime.date(2022, 2, 10), "price": 400},
    ]

    result = outdated_products(products)

    assert result == []


@mock.patch("app.main.datetime.date.today")
def test_product_expired(today_mock: Mock) -> None:
    today_mock.return_value = datetime.date(2022, 2, 10)
    products = [
        {"name": "tuna", "expiration_date": datetime.date(2022, 2, 11), "price": 400},
    ]
    result = outdated_products(products)
    assert result == []


@mock.patch("app.main.datetime.date.today")
def test_data_is_valid(today_mock: Mock) -> None:
    today_mock.return_value = datetime.date(2022, 2, 10)
    products = [
        {"name": "tuna", "expiration_date": datetime.date(2022, 2, 9), "price": 400},
    ]
    result = outdated_products(products)
    assert result == ["tuna"]


@mock.patch("app.main.datetime.date.today")
def test_empty_products(today_mock: Mock) -> None:
    today_mock.return_value = datetime.date(2022, 2, 10)
    products = []
    result = outdated_products(products)
    assert result == []
