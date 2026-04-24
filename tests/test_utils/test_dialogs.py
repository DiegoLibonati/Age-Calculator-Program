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

    def test_none_message_keeps_class_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message=None)
        assert dialog.message == MESSAGE_ERROR_APP

    def test_title_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.title == "Error"

    def test_title_for_warning_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.WARNING
        assert dialog.title == "Warning"

    def test_title_for_info_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.INFO
        assert dialog.title == "Information"

    def test_to_dict_contains_dialog_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result: dict[str, Any] = dialog.to_dict()
        assert result["dialog_type"] == BaseDialog.ERROR

    def test_to_dict_contains_title(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result: dict[str, Any] = dialog.to_dict()
        assert "title" in result
        assert result["title"] == "Error"

    def test_to_dict_contains_message(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test message")
        result: dict[str, Any] = dialog.to_dict()
        assert result["message"] == "test message"

    def test_open_calls_showerror_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test error")
        mock_showerror: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_showerror}):
            dialog.open()
        mock_showerror.assert_called_once_with("Error", "test error")

    def test_open_calls_showwarning_for_warning_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.WARNING
        mock_showwarning: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_showwarning}):
            dialog.open()
        mock_showwarning.assert_called_once()

    def test_open_calls_showinfo_for_info_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.INFO
        mock_showinfo: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_showinfo}):
            dialog.open()
        mock_showinfo.assert_called_once()

    def test_open_with_invalid_dialog_type_falls_back_to_showerror(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = "INVALID"
        with patch("src.utils.dialogs.messagebox.showerror") as mock_showerror:
            dialog.open()
        mock_showerror.assert_called_once_with(BaseDialog.ERROR, MESSAGE_NOT_FOUND_DIALOG_TYPE)


class TestBaseDialogError:
    def test_is_exception_subclass(self) -> None:
        assert issubclass(BaseDialogError, Exception)

    def test_is_base_dialog_subclass(self) -> None:
        assert issubclass(BaseDialogError, BaseDialog)

    def test_dialog_type_is_error(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert error.dialog_type == BaseDialog.ERROR


class TestValidationDialogError:
    def test_is_base_dialog_error_subclass(self) -> None:
        assert issubclass(ValidationDialogError, BaseDialogError)

    def test_custom_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="invalid input")
        assert error.message == "invalid input"

    def test_can_be_raised_and_caught_as_exception(self) -> None:
        with pytest.raises(ValidationDialogError):
            raise ValidationDialogError(message="test")

    def test_can_be_caught_as_base_dialog_error(self) -> None:
        with pytest.raises(BaseDialogError):
            raise ValidationDialogError(message="test")


class TestInternalDialogError:
    def test_is_base_dialog_error_subclass(self) -> None:
        assert issubclass(InternalDialogError, BaseDialogError)

    def test_custom_message(self) -> None:
        error: InternalDialogError = InternalDialogError(message="internal failure")
        assert error.message == "internal failure"


class TestAuthenticationDialogError:
    def test_is_base_dialog_error_subclass(self) -> None:
        assert issubclass(AuthenticationDialogError, BaseDialogError)

    def test_dialog_type_is_error(self) -> None:
        error: AuthenticationDialogError = AuthenticationDialogError()
        assert error.dialog_type == BaseDialog.ERROR


class TestNotFoundDialogError:
    def test_is_base_dialog_error_subclass(self) -> None:
        assert issubclass(NotFoundDialogError, BaseDialogError)

    def test_instantiation(self) -> None:
        error: NotFoundDialogError = NotFoundDialogError()
        assert error is not None

    def test_default_message(self) -> None:
        error: NotFoundDialogError = NotFoundDialogError()
        assert error.message == "Resource not found"


class TestConflictDialogError:
    def test_is_base_dialog_error_subclass(self) -> None:
        assert issubclass(ConflictDialogError, BaseDialogError)

    def test_instantiation(self) -> None:
        error: ConflictDialogError = ConflictDialogError()
        assert error is not None

    def test_default_message(self) -> None:
        error: ConflictDialogError = ConflictDialogError()
        assert error.message == "Conflict error"


class TestBusinessDialogError:
    def test_is_base_dialog_error_subclass(self) -> None:
        assert issubclass(BusinessDialogError, BaseDialogError)

    def test_instantiation(self) -> None:
        error: BusinessDialogError = BusinessDialogError()
        assert error is not None

    def test_default_message(self) -> None:
        error: BusinessDialogError = BusinessDialogError()
        assert error.message == "Business rule violated"


class TestDeprecatedDialogWarning:
    def test_is_base_dialog_notification_subclass(self) -> None:
        assert issubclass(DeprecatedDialogWarning, BaseDialogNotification)

    def test_dialog_type_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert warning.dialog_type == BaseDialog.WARNING

    def test_open_calls_showwarning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        mock_showwarning: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_showwarning}):
            warning.open()
        mock_showwarning.assert_called_once()


class TestSuccessDialogInformation:
    def test_is_base_dialog_notification_subclass(self) -> None:
        assert issubclass(SuccessDialogInformation, BaseDialogNotification)

    def test_dialog_type_is_info(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert info.dialog_type == BaseDialog.INFO

    def test_open_calls_showinfo(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        mock_showinfo: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_showinfo}):
            info.open()
        mock_showinfo.assert_called_once()
