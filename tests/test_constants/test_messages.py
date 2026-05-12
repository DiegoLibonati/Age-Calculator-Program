from src.constants import messages


class TestMessages:
    def test_message_success_age_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_SUCCESS_AGE, str)

    def test_message_success_age_has_name_placeholder(self) -> None:
        assert "{name}" in messages.MESSAGE_SUCCESS_AGE

    def test_message_success_age_has_age_placeholder(self) -> None:
        assert "{age}" in messages.MESSAGE_SUCCESS_AGE

    def test_message_success_age_formats_correctly(self) -> None:
        result: str = messages.MESSAGE_SUCCESS_AGE.format(name="Alice", age=30)

        assert "Alice" in result
        assert "30" in result

    def test_message_error_app_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_ERROR_APP, str)

    def test_message_not_valid_fields_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_FIELDS, str)

    def test_message_not_valid_month_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_MONTH, str)

    def test_message_not_valid_day_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_DAY, str)

    def test_message_not_valid_date_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_DATE, str)

    def test_message_not_found_dialog_type_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_FOUND_DIALOG_TYPE, str)
