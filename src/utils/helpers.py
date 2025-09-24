from datetime import datetime

from src.utils.messages import (
    MESSAGE_ERROR_FUTURE_DATE,
    MESSAGE_ERROR_INVALID_DATE,
    MESSAGE_ERROR_MISSING_VALUES,
    MESSAGE_ERROR_MONTH_RANGE,
    MESSAGE_ERROR_NON_NUMERIC,
)


def validate_inputs(name: str, year: str, month: str, day: str) -> str | None:
    if not name or not year or not month or not day:
        return MESSAGE_ERROR_MISSING_VALUES

    try:
        year, month, day = int(year), int(month), int(day)
    except ValueError:
        return MESSAGE_ERROR_NON_NUMERIC

    if year > datetime.now().year:
        return MESSAGE_ERROR_FUTURE_DATE

    if not (1 <= month <= 12):
        return MESSAGE_ERROR_MONTH_RANGE

    if not is_valid_date(year, month, day):
        return MESSAGE_ERROR_INVALID_DATE

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
