from datetime import datetime
from unittest.mock import patch

from src.constants.messages import (
    MESSAGE_NOT_VALID_DATE,
    MESSAGE_NOT_VALID_FIELDS,
)
from src.utils.helpers import calculate_age, is_valid_date, validate_inputs


class TestValidateInputs:
    def test_returns_none_when_all_inputs_are_valid(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "1", "1")

        assert result is None

    def test_returns_error_when_name_is_empty(self) -> None:
        result: str | None = validate_inputs("", "2000", "1", "1")

        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_when_year_is_empty(self) -> None:
        result: str | None = validate_inputs("Alice", "", "1", "1")

        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_when_month_is_empty(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "", "1")

        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_when_day_is_empty(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "1", "")

        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_when_year_is_not_numeric(self) -> None:
        result: str | None = validate_inputs("Alice", "abc", "1", "1")

        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_when_month_is_not_numeric(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "abc", "1")

        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_when_day_is_not_numeric(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "1", "abc")

        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_when_year_is_in_future(self) -> None:
        result: str | None = validate_inputs("Alice", "3000", "1", "1")

        assert result == MESSAGE_NOT_VALID_DATE

    def test_returns_error_when_date_is_invalid(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "2", "30")

        assert result == MESSAGE_NOT_VALID_DATE

    def test_returns_error_when_month_exceeds_twelve(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "13", "1")

        assert result == MESSAGE_NOT_VALID_DATE


class TestCalculateAge:
    def test_returns_correct_age_when_birthday_has_passed(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2026, 5, 12)

            age: int = calculate_age(2000, 1, 1)

        assert age == 26

    def test_returns_correct_age_when_birthday_has_not_passed(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2026, 5, 12)

            age: int = calculate_age(2000, 12, 31)

        assert age == 25

    def test_returns_correct_age_on_birthday(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2026, 5, 12)

            age: int = calculate_age(2000, 5, 12)

        assert age == 26

    def test_returns_correct_age_for_same_month_day_after_today(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2026, 5, 12)

            age: int = calculate_age(2000, 5, 13)

        assert age == 25


class TestIsValidDate:
    def test_returns_true_for_valid_date(self) -> None:
        result: bool = is_valid_date(2000, 1, 1)

        assert result is True

    def test_returns_false_for_invalid_day_in_february(self) -> None:
        result: bool = is_valid_date(2000, 2, 30)

        assert result is False

    def test_returns_false_for_invalid_month(self) -> None:
        result: bool = is_valid_date(2000, 13, 1)

        assert result is False

    def test_returns_true_for_leap_year_feb_29(self) -> None:
        result: bool = is_valid_date(2000, 2, 29)

        assert result is True

    def test_returns_false_for_non_leap_year_feb_29(self) -> None:
        result: bool = is_valid_date(2001, 2, 29)

        assert result is False
