from datetime import datetime
from unittest.mock import patch

from src.constants.messages import (
    MESSAGE_NOT_VALID_DATE,
    MESSAGE_NOT_VALID_FIELDS,
)
from src.utils.helpers import calculate_age, is_valid_date, validate_inputs


class TestIsValidDate:
    def test_returns_true_for_valid_date(self) -> None:
        assert is_valid_date(2000, 6, 15) is True

    def test_returns_false_for_invalid_day(self) -> None:
        assert is_valid_date(2000, 2, 30) is False

    def test_returns_false_for_invalid_month(self) -> None:
        assert is_valid_date(2000, 13, 1) is False

    def test_returns_true_for_leap_year_day(self) -> None:
        assert is_valid_date(2000, 2, 29) is True

    def test_returns_false_for_non_leap_year_day(self) -> None:
        assert is_valid_date(2001, 2, 29) is False

    def test_returns_true_for_last_day_of_month(self) -> None:
        assert is_valid_date(2000, 1, 31) is True

    def test_returns_false_for_day_zero(self) -> None:
        assert is_valid_date(2000, 1, 0) is False


class TestValidateInputs:
    def test_returns_none_for_valid_inputs(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2025, 6, 15)
            mock_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            result: str | None = validate_inputs("Alice", "2000", "6", "15")
        assert result is None

    def test_returns_not_valid_fields_when_name_is_empty(self) -> None:
        result: str | None = validate_inputs("", "2000", "6", "15")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_not_valid_fields_when_year_is_empty(self) -> None:
        result: str | None = validate_inputs("Alice", "", "6", "15")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_not_valid_fields_when_month_is_empty(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "", "15")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_not_valid_fields_when_day_is_empty(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "6", "")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_not_valid_fields_when_year_is_not_numeric(self) -> None:
        result: str | None = validate_inputs("Alice", "abc", "6", "15")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_not_valid_fields_when_month_is_not_numeric(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "xyz", "15")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_not_valid_fields_when_day_is_not_numeric(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "6", "xyz")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_not_valid_date_when_year_is_in_future(self) -> None:
        future_year: str = str(datetime.now().year + 1)
        result: str | None = validate_inputs("Alice", future_year, "6", "15")
        assert result == MESSAGE_NOT_VALID_DATE

    def test_returns_not_valid_date_when_date_is_invalid(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "2", "30")
        assert result == MESSAGE_NOT_VALID_DATE

    def test_returns_not_valid_month_when_month_is_zero(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "0", "1")
        assert result == MESSAGE_NOT_VALID_DATE

    def test_returns_not_valid_month_when_month_is_thirteen(self) -> None:
        result: str | None = validate_inputs("Alice", "2000", "13", "1")
        assert result == MESSAGE_NOT_VALID_DATE


class TestCalculateAge:
    def test_returns_correct_age_when_birthday_already_passed(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2025, 6, 15)
            result: int = calculate_age(year=2000, month=3, day=10)
        assert result == 25

    def test_returns_correct_age_when_birthday_not_yet_this_year(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2025, 3, 1)
            result: int = calculate_age(year=2000, month=6, day=15)
        assert result == 24

    def test_returns_correct_age_on_exact_birthday(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2025, 6, 15)
            result: int = calculate_age(year=2000, month=6, day=15)
        assert result == 25

    def test_returns_correct_age_when_same_month_but_day_not_reached(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2025, 6, 10)
            result: int = calculate_age(year=2000, month=6, day=15)
        assert result == 24

    def test_returns_integer(self) -> None:
        with patch("src.utils.helpers.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2025, 6, 15)
            result: int = calculate_age(year=2000, month=3, day=10)
        assert isinstance(result, int)
