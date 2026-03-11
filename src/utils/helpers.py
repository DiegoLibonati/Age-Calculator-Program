from datetime import datetime

from src.constants.messages import (
    MESSAGE_NOT_VALID_DATE,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_NOT_VALID_MONTH,
)


def validate_inputs(name: str, year: str, month: str, day: str) -> str | None:
    if not name or not year or not month or not day:
        return MESSAGE_NOT_VALID_FIELDS

    try:
        year, month, day = int(year), int(month), int(day)
    except ValueError:
        return MESSAGE_NOT_VALID_FIELDS

    if year > datetime.now().year or not is_valid_date(year, month, day):
        return MESSAGE_NOT_VALID_DATE

    if not (1 <= month <= 12):
        return MESSAGE_NOT_VALID_MONTH

    return None


def calculate_age(year: int, month: int, day: int) -> int:
    current_date = datetime.now()
    return current_date.year - year if month < current_date.month or (month == current_date.month and day <= current_date.day) else current_date.year - year - 1


def is_valid_date(year: int, month: int, day: int) -> bool:
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False
