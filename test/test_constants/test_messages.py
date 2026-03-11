from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_DATE,
    MESSAGE_NOT_VALID_DAY,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_NOT_VALID_MONTH,
    MESSAGE_SUCCESS_AGE,
)


class TestMessages:
    def test_success_age_is_string(self) -> None:
        assert isinstance(MESSAGE_SUCCESS_AGE, str)

    def test_success_age_contains_name_placeholder(self) -> None:
        assert "{name}" in MESSAGE_SUCCESS_AGE

    def test_success_age_contains_age_placeholder(self) -> None:
        assert "{age}" in MESSAGE_SUCCESS_AGE

    def test_success_age_formats_correctly(self) -> None:
        result: str = MESSAGE_SUCCESS_AGE.format(name="Alice", age=30)
        assert "Alice" in result
        assert "30" in result

    def test_error_app_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_APP, str)

    def test_error_app_is_not_empty(self) -> None:
        assert len(MESSAGE_ERROR_APP) > 0

    def test_not_valid_fields_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_FIELDS, str)

    def test_not_valid_fields_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_VALID_FIELDS) > 0

    def test_not_valid_month_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_MONTH, str)

    def test_not_valid_month_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_VALID_MONTH) > 0

    def test_not_valid_day_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_DAY, str)

    def test_not_valid_day_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_VALID_DAY) > 0

    def test_not_valid_date_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_DATE, str)

    def test_not_valid_date_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_VALID_DATE) > 0

    def test_not_found_dialog_type_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_DIALOG_TYPE, str)

    def test_not_found_dialog_type_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_FOUND_DIALOG_TYPE) > 0

    def test_all_messages_are_unique(self) -> None:
        all_messages: list[str] = [
            MESSAGE_SUCCESS_AGE,
            MESSAGE_ERROR_APP,
            MESSAGE_NOT_VALID_FIELDS,
            MESSAGE_NOT_VALID_MONTH,
            MESSAGE_NOT_VALID_DAY,
            MESSAGE_NOT_VALID_DATE,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ]
        assert len(all_messages) == len(set(all_messages))
