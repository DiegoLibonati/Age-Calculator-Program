from src.constants.messages import (
    MESSAGE_ERROR_DAY_RANGE,
    MESSAGE_ERROR_FUTURE_DATE,
    MESSAGE_ERROR_INVALID_DATE,
    MESSAGE_ERROR_MISSING_VALUES,
    MESSAGE_ERROR_MONTH_RANGE,
    MESSAGE_ERROR_NON_NUMERIC,
    MESSAGE_HELLO,
)


class TestMessages:
    def test_message_hello_formats_name_and_age(self) -> None:
        result: str = MESSAGE_HELLO.format(name="Ana", age=30)
        assert "Ana" in result
        assert "30" in result

    def test_message_hello_is_string(self) -> None:
        assert isinstance(MESSAGE_HELLO, str)

    def test_message_error_invalid_date_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_INVALID_DATE, str)

    def test_message_error_future_date_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_FUTURE_DATE, str)

    def test_message_error_missing_values_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_MISSING_VALUES, str)

    def test_message_error_month_range_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_MONTH_RANGE, str)

    def test_message_error_day_range_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_DAY_RANGE, str)

    def test_message_error_non_numeric_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_NON_NUMERIC, str)

    def test_message_hello_contains_name_placeholder(self) -> None:
        assert "{name}" in MESSAGE_HELLO

    def test_message_hello_contains_age_placeholder(self) -> None:
        assert "{age}" in MESSAGE_HELLO
