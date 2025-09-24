import logging
from datetime import datetime

from src.ui.interface_app import InterfaceApp
from src.utils.messages import (
    MESSAGE_ERROR_FUTURE_DATE,
    MESSAGE_ERROR_INVALID_DATE,
    MESSAGE_ERROR_MISSING_VALUES,
    MESSAGE_ERROR_MONTH_RANGE,
    MESSAGE_ERROR_NON_NUMERIC,
    MESSAGE_HELLO,
)
from src.utils.styles import BG_COLOR

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

CUSTOM_BG = "" or BG_COLOR


def test_initial_config_tk_app(interface_app: InterfaceApp) -> None:
    root = interface_app.root
    root.update()

    title = root.title()
    geometry = root.geometry().split("+")[0]
    resizable = root.resizable()
    config_bg = root.cget("bg")

    assert title == "Age Calculator"
    assert geometry == "400x300"
    assert resizable == (False, False)
    assert config_bg == CUSTOM_BG


def test_get_current_age_valid(interface_app: InterfaceApp) -> None:
    name, year, month, day = "Die", 1998, 7, 29
    current_date = datetime.now()

    interface_app.name.set(name)
    interface_app.year.set(str(year))
    interface_app.month.set(str(month))
    interface_app.day.set(str(day))

    interface_app._get_current_age()
    final_label = interface_app.final_label

    relative_age = (
        current_date.year - year
        if month < current_date.month
        or (month == current_date.month and day <= current_date.day)
        else current_date.year - year - 1
    )

    assert final_label["text"] == MESSAGE_HELLO.format(name=name, age=relative_age)


def test_get_current_age_missing_values(interface_app: InterfaceApp) -> None:
    interface_app.name.set("")
    interface_app.year.set("1998")
    interface_app.month.set("7")
    interface_app.day.set("29")

    interface_app._get_current_age()
    final_label = interface_app.final_label

    assert final_label["text"] == MESSAGE_ERROR_MISSING_VALUES


def test_get_current_age_with_non_numeric(interface_app: InterfaceApp) -> None:
    interface_app.name.set("Die")
    interface_app.year.set("pepe")
    interface_app.month.set("7")
    interface_app.day.set("29")

    interface_app._get_current_age()
    final_label = interface_app.final_label

    assert final_label["text"] == MESSAGE_ERROR_NON_NUMERIC


def test_get_current_age_error_future(interface_app: InterfaceApp) -> None:
    interface_app.name.set("Die")
    future_year = datetime.now().year + 10
    interface_app.year.set(str(future_year))
    interface_app.month.set("7")
    interface_app.day.set("29")

    interface_app._get_current_age()
    final_label = interface_app.final_label

    assert final_label["text"] == MESSAGE_ERROR_FUTURE_DATE


def test_get_current_age_error_month_range(interface_app: InterfaceApp) -> None:
    interface_app.name.set("Die")
    interface_app.year.set("1998")
    interface_app.month.set("13")
    interface_app.day.set("29")

    interface_app._get_current_age()
    final_label = interface_app.final_label

    assert final_label["text"] == MESSAGE_ERROR_MONTH_RANGE


def test_get_current_age_error_invalid_date(interface_app: InterfaceApp) -> None:
    interface_app.name.set("Die")
    interface_app.year.set("2023")
    interface_app.month.set("2")
    interface_app.day.set("29")

    interface_app._get_current_age()
    final_label = interface_app.final_label

    assert final_label["text"] == MESSAGE_ERROR_INVALID_DATE
