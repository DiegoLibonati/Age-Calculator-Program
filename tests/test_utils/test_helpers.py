from datetime import datetime as real_datetime
from unittest.mock import patch

from src.constants.messages import (
    MESSAGE_NOT_VALID_DATE,
    MESSAGE_NOT_VALID_FIELDS,
)
from src.utils.helpers import calculate_age, is_valid_date, validate_inputs


class TestValidateInputs:
    def test_returns_none_for_valid_inputs(self) -> None:
        result: str | None = validate_inputs("John", "1990", "3", "15")
        assert result is None

    def test_returns_error_for_empty_name(self) -> None:
        result: str | None = validate_inputs("", "1990", "3", "15")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_for_empty_year(self) -> None:
        result: str | None = validate_inputs("John", "", "3", "15")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_for_empty_month(self) -> None:
        result: str | None = validate_inputs("John", "1990", "", "15")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_for_empty_day(self) -> None:
        result: str | None = validate_inputs("John", "1990", "3", "")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_for_non_numeric_year(self) -> None:
        result: str | None = validate_inputs("John", "abc", "3", "15")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_for_non_numeric_month(self) -> None:
        result: str | None = validate_inputs("John", "1990", "xyz", "15")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_for_non_numeric_day(self) -> None:
        result: str | None = validate_inputs("John", "1990", "3", "abc")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_for_future_year(self) -> None:
        result: str | None = validate_inputs("John", "9999", "1", "1")
        assert result == MESSAGE_NOT_VALID_DATE

    def test_returns_error_for_february_30(self) -> None:
        result: str | None = validate_inputs("John", "2000", "2", "30")
        assert result == MESSAGE_NOT_VALID_DATE

    def test_returns_error_for_month_out_of_range(self) -> None:
        result: str | None = validate_inputs("John", "2000", "13", "1")
        assert result == MESSAGE_NOT_VALID_DATE

    def test_returns_error_for_day_zero(self) -> None:
        result: str | None = validate_inputs("John", "2000", "1", "0")
        assert result == MESSAGE_NOT_VALID_DATE

    def test_returns_none_for_leap_year_feb_29(self) -> None:
        result: str | None = validate_inputs("John", "2000", "2", "29")
        assert result is None

    def test_returns_error_for_non_leap_year_feb_29(self) -> None:
        result: str | None = validate_inputs("John", "2001", "2", "29")
        assert result == MESSAGE_NOT_VALID_DATE


class TestCalculateAge:
    def test_birthday_before_current_month(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = real_datetime(2026, 4, 10)
            result: int = calculate_age(year=1990, month=1, day=1)
        assert result == 36

    def test_birthday_after_current_month(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = real_datetime(2026, 4, 10)
            result: int = calculate_age(year=1990, month=12, day=25)
        assert result == 35

    def test_birthday_same_month_before_current_day(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = real_datetime(2026, 4, 10)
            result: int = calculate_age(year=1990, month=4, day=5)
        assert result == 36

    def test_birthday_same_month_same_day(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = real_datetime(2026, 4, 10)
            result: int = calculate_age(year=1990, month=4, day=10)
        assert result == 36

    def test_birthday_same_month_after_current_day(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = real_datetime(2026, 4, 10)
            result: int = calculate_age(year=1990, month=4, day=15)
        assert result == 35

    def test_returns_integer(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = real_datetime(2026, 4, 10)
            result: int = calculate_age(year=1990, month=1, day=1)
        assert isinstance(result, int)


class TestIsValidDate:
    def test_valid_date(self) -> None:
        assert is_valid_date(2000, 3, 15) is True

    def test_invalid_month_too_high(self) -> None:
        assert is_valid_date(2000, 13, 1) is False

    def test_invalid_month_zero(self) -> None:
        assert is_valid_date(2000, 0, 1) is False

    def test_invalid_day_zero(self) -> None:
        assert is_valid_date(2000, 1, 0) is False

    def test_invalid_day_for_month(self) -> None:
        assert is_valid_date(2000, 2, 30) is False

    def test_leap_year_feb_29_is_valid(self) -> None:
        assert is_valid_date(2000, 2, 29) is True

    def test_non_leap_year_feb_29_is_invalid(self) -> None:
        assert is_valid_date(2001, 2, 29) is False

    def test_last_day_of_month_is_valid(self) -> None:
        assert is_valid_date(2000, 1, 31) is True

    def test_day_beyond_month_end_is_invalid(self) -> None:
        assert is_valid_date(2000, 4, 31) is False
