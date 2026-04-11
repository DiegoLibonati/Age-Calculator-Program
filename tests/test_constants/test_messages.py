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
    def test_message_success_age_format_with_name_and_age(self) -> None:
        result: str = MESSAGE_SUCCESS_AGE.format(name="John", age=30)
        assert result == "Hi John, your age is 30."

    def test_message_success_age_contains_name_placeholder(self) -> None:
        assert "{name}" in MESSAGE_SUCCESS_AGE

    def test_message_success_age_contains_age_placeholder(self) -> None:
        assert "{age}" in MESSAGE_SUCCESS_AGE

    def test_message_error_app_value(self) -> None:
        assert MESSAGE_ERROR_APP == "Internal error. Contact a developer."

    def test_message_not_valid_fields_value(self) -> None:
        assert MESSAGE_NOT_VALID_FIELDS == "The fields entered are invalid."

    def test_message_not_valid_month_value(self) -> None:
        assert MESSAGE_NOT_VALID_MONTH == "Month should be between 1 and 12."

    def test_message_not_valid_day_value(self) -> None:
        assert MESSAGE_NOT_VALID_DAY == "Day is not valid for the given month."

    def test_message_not_valid_date_value(self) -> None:
        assert MESSAGE_NOT_VALID_DATE == "The date entered is not valid."

    def test_message_not_found_dialog_type_value(self) -> None:
        assert MESSAGE_NOT_FOUND_DIALOG_TYPE == "The type of dialog to display is not found."
