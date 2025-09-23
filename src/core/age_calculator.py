from datetime import datetime

from src.utils.constants import (
    ERROR_FUTURE_DATE,
    ERROR_INVALID_DATE,
    ERROR_MISSING_VALUES,
    ERROR_MONTH_RANGE,
    ERROR_NON_NUMERIC,
)


def validate_inputs(name: str, year: str, month: str, day: str) -> str | None:
    if not name or not year or not month or not day:
        return ERROR_MISSING_VALUES

    try:
        year, month, day = int(year), int(month), int(day)
    except ValueError:
        return ERROR_NON_NUMERIC

    if year > datetime.now().year:
        return ERROR_FUTURE_DATE

    if not (1 <= month <= 12):
        return ERROR_MONTH_RANGE

    if not is_valid_date(year, month, day):
        return ERROR_INVALID_DATE

    return None


def calculate_age(year: int, month: int, day: int) -> int:
    current_date = datetime.now()
    return (
        current_date.year - year
        if month < current_date.month
        or (month == current_date.month and day <= current_date.day)
        else current_date.year - year - 1
    )


def is_valid_date(year: int, month: int, day: int) -> bool:
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False
