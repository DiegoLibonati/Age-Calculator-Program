import logging
from datetime import datetime

from pytest import mark

from src.models import InterfaceApp
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

CUSTOM_BG = "" or "#C98686"


def test_initial_config_tk_app(interface_app: InterfaceApp) -> None:
    root = interface_app.root
    root.update()

    title = root.title
    geometry = root.geometry().split("+")[0]
    resizable = root.resizable()
    config_bg = root.cget("bg")

    assert title == "Age Calculator"
    assert geometry == "400x300"
    assert resizable == (False, False)
    assert config_bg == CUSTOM_BG


@mark.parametrize(
    "year, month, day, expected",
    [
        (2024, 2, 29, True),
        (2023, 2, 29, False),
        (2024, 4, 31, False),
        (2024, 12, 31, True),
    ],
)
def test_is_valid_date(
    interface_app: InterfaceApp, year: int, month: int, day: int, expected: bool
) -> None:
    is_valid_date = interface_app.is_valid_date(year=year, month=month, day=day)

    assert is_valid_date == expected


def test_calculate_age(interface_app: InterfaceApp) -> None:
    name = "Die"
    year, month, day = [1998, 7, 29]
    current_date = datetime.now()

    interface_app._calculate_age(name=name, year=year, month=month, day=day)
    final_label = interface_app.final_label

    relative_age = (
        current_date.year - year
        if month < current_date.month
        or month == current_date.month
        and day <= current_date.day
        else current_date.year - year - 1
    )

    assert final_label["text"] == f"Hi {name}, your age is {relative_age}."


def test_get_current_age_missing_values(interface_app: InterfaceApp) -> None:
    interface_app.name.set("")
    interface_app.year.set(1998)
    interface_app.month.set(7)
    interface_app.day.set(29)

    interface_app._get_current_age()
    final_label = interface_app.final_label

    assert final_label["text"] == ERROR_MISSING_VALUES


def test_get_current_age_with_non_numeric(interface_app: InterfaceApp) -> None:
    interface_app.name.set("Die")
    interface_app.year.set("pepe")
    interface_app.month.set(7)
    interface_app.day.set(29)

    interface_app._get_current_age()
    final_label = interface_app.final_label

    assert final_label["text"] == ERROR_NON_NUMERIC


def test_get_current_age_error_future(interface_app: InterfaceApp) -> None:
    interface_app.name.set("Die")
    interface_app.year.set(123123123123)
    interface_app.month.set(7)
    interface_app.day.set(29)

    interface_app._get_current_age()
    final_label = interface_app.final_label

    assert final_label["text"] == ERROR_FUTURE_DATE


def test_get_current_age_error_month_range(interface_app: InterfaceApp) -> None:
    interface_app.name.set("Die")
    interface_app.year.set(1998)
    interface_app.month.set(13)
    interface_app.day.set(29)

    interface_app._get_current_age()
    final_label = interface_app.final_label

    assert final_label["text"] == ERROR_MONTH_RANGE


def test_get_current_age_error_invalid_date(interface_app: InterfaceApp) -> None:
    interface_app.name.set("Die")
    interface_app.year.set(2023)
    interface_app.month.set(2)
    interface_app.day.set(29)

    interface_app._get_current_age()
    final_label = interface_app.final_label

    assert final_label["text"] == ERROR_INVALID_DATE
