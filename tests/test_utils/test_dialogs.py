from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_ERROR_APP, MESSAGE_NOT_FOUND_DIALOG_TYPE
from src.utils.dialogs import (
    AuthenticationDialogError,
    BaseDialog,
    BaseDialogError,
    BaseDialogNotification,
    BusinessDialogError,
    ConflictDialogError,
    DeprecatedDialogWarning,
    InternalDialogError,
    NotFoundDialogError,
    SuccessDialogInformation,
    ValidationDialogError,
)


class TestBaseDialog:
    def test_default_dialog_type_is_error(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.dialog_type == BaseDialog.ERROR

    def test_default_message_is_error_app(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.message == MESSAGE_ERROR_APP

    def test_custom_message_overrides_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message="custom error")

        assert dialog.message == "custom error"

    def test_title_returns_error_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.title == "Error"

    def test_title_returns_warning_for_warning_type(self) -> None:
        class WarningDialog(BaseDialog):
            dialog_type = BaseDialog.WARNING

        dialog: WarningDialog = WarningDialog()

        assert dialog.title == "Warning"

    def test_title_returns_information_for_info_type(self) -> None:
        class InfoDialog(BaseDialog):
            dialog_type = BaseDialog.INFO

        dialog: InfoDialog = InfoDialog()

        assert dialog.title == "Information"

    def test_to_dict_contains_dialog_type(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test")
        result: dict[str, Any] = dialog.to_dict()

        assert result["dialog_type"] == BaseDialog.ERROR

    def test_to_dict_contains_title(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test")
        result: dict[str, Any] = dialog.to_dict()

        assert result["title"] == "Error"

    def test_to_dict_contains_message(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test")
        result: dict[str, Any] = dialog.to_dict()

        assert result["message"] == "test"

    def test_open_calls_handler_for_dialog_type(self) -> None:
        mock_handler: MagicMock = MagicMock()
        dialog: BaseDialog = BaseDialog()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_handler}):
            dialog.open()

        mock_handler.assert_called_once_with("Error", MESSAGE_ERROR_APP)

    def test_open_calls_showerror_when_dialog_type_is_unknown(self) -> None:
        class UnknownDialog(BaseDialog):
            dialog_type = "unknown_type"

        dialog: UnknownDialog = UnknownDialog()

        with patch("src.utils.dialogs.messagebox.showerror") as mock_showerror:
            dialog.open()

        mock_showerror.assert_called_once_with(BaseDialog.ERROR, MESSAGE_NOT_FOUND_DIALOG_TYPE)


class TestBaseDialogError:
    def test_is_subclass_of_exception(self) -> None:
        assert issubclass(BaseDialogError, Exception)

    def test_is_subclass_of_base_dialog(self) -> None:
        assert issubclass(BaseDialogError, BaseDialog)

    def test_dialog_type_is_error(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert error.dialog_type == BaseDialog.ERROR

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BaseDialogError):
            raise BaseDialogError()

    def test_can_be_caught_as_base_exception(self) -> None:
        with pytest.raises(Exception):
            raise BaseDialogError()


class TestValidationDialogError:
    def test_is_subclass_of_base_dialog_error(self) -> None:
        assert issubclass(ValidationDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError()

        assert error.message == "Validation error"

    def test_custom_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="invalid input")

        assert error.message == "invalid input"


class TestInternalDialogError:
    def test_is_subclass_of_base_dialog_error(self) -> None:
        assert issubclass(InternalDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        error: InternalDialogError = InternalDialogError()

        assert error.message == "Internal error"


class TestAuthenticationDialogError:
    def test_is_subclass_of_base_dialog_error(self) -> None:
        assert issubclass(AuthenticationDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        error: AuthenticationDialogError = AuthenticationDialogError()

        assert error.message == "Authentication error"


class TestNotFoundDialogError:
    def test_is_subclass_of_base_dialog_error(self) -> None:
        assert issubclass(NotFoundDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        error: NotFoundDialogError = NotFoundDialogError()

        assert error.message == "Resource not found"


class TestConflictDialogError:
    def test_is_subclass_of_base_dialog_error(self) -> None:
        assert issubclass(ConflictDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        error: ConflictDialogError = ConflictDialogError()

        assert error.message == "Conflict error"


class TestBusinessDialogError:
    def test_is_subclass_of_base_dialog_error(self) -> None:
        assert issubclass(BusinessDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        error: BusinessDialogError = BusinessDialogError()

        assert error.message == "Business rule violated"


class TestBaseDialogNotification:
    def test_is_subclass_of_base_dialog(self) -> None:
        assert issubclass(BaseDialogNotification, BaseDialog)

    def test_is_not_subclass_of_exception(self) -> None:
        assert not issubclass(BaseDialogNotification, Exception)


class TestDeprecatedDialogWarning:
    def test_is_subclass_of_base_dialog_notification(self) -> None:
        assert issubclass(DeprecatedDialogWarning, BaseDialogNotification)

    def test_dialog_type_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()

        assert warning.dialog_type == BaseDialog.WARNING

    def test_default_message(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()

        assert warning.message == "This feature is deprecated"


class TestSuccessDialogInformation:
    def test_is_subclass_of_base_dialog_notification(self) -> None:
        assert issubclass(SuccessDialogInformation, BaseDialogNotification)

    def test_dialog_type_is_info(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()

        assert info.dialog_type == BaseDialog.INFO

    def test_default_message(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()

        assert info.message == "Operation completed successfully"
