import logging
from datetime import datetime

from pytest import mark

from src.core.age_calculator import calculate_age, is_valid_date, validate_inputs
from src.utils.constants import (
    ERROR_FUTURE_DATE,
    ERROR_INVALID_DATE,
    ERROR_MISSING_VALUES,
    ERROR_MONTH_RANGE,
    ERROR_NON_NUMERIC,
)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


@mark.parametrize(
    "name, year, month, day, expected",
    [
        ("", "2000", "5", "10", ERROR_MISSING_VALUES),
        ("John", "", "5", "10", ERROR_MISSING_VALUES),
        ("John", "abcd", "5", "10", ERROR_NON_NUMERIC),
        ("John", "2000", "May", "10", ERROR_NON_NUMERIC),
    ],
)
def test_validate_inputs_errors_basic(name, year, month, day, expected):
    result = validate_inputs(name, year, month, day)
    assert result == expected


def test_validate_inputs_future_date():
    future_year = datetime.now().year + 1
    result = validate_inputs("John", str(future_year), "5", "10")
    assert result == ERROR_FUTURE_DATE


@mark.parametrize("month", ["0", "13"])
def test_validate_inputs_month_out_of_range(month):
    result = validate_inputs("John", "2000", month, "10")
    assert result == ERROR_MONTH_RANGE


def test_validate_inputs_invalid_date():
    result = validate_inputs("John", "2000", "2", "30")  # Febrero 30 no existe
    assert result == ERROR_INVALID_DATE


def test_validate_inputs_valid():
    result = validate_inputs("John", "2000", "5", "10")
    assert result is None


def test_calculate_age_exact_birthday():
    today = datetime.now()
    age = calculate_age(today.year - 20, today.month, today.day)
    assert age == 20


def test_calculate_age_before_birthday_this_year():
    today = datetime.now()
    age = calculate_age(today.year - 20, today.month + 1, today.day)
    assert age == 19


def test_calculate_age_after_birthday_this_year():
    today = datetime.now()
    age = calculate_age(today.year - 20, today.month - 1, today.day)
    assert age == 20


@mark.parametrize(
    "year, month, day, expected",
    [
        (2000, 5, 10, True),
        (2000, 2, 30, False),
    ],
)
def test_is_valid_date(year, month, day, expected):
    assert is_valid_date(year, month, day) == expected
