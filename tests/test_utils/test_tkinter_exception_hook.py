import sys
from unittest.mock import MagicMock, patch

from src.utils.dialogs import ValidationDialogError
from src.utils.tkinter_exception_hook import tkinter_exception_hook


class TestTkinterExceptionHook:
    def test_calls_open_when_exc_is_base_dialog(self) -> None:
        try:
            raise ValidationDialogError("test error")
        except ValidationDialogError:
            exc_type, exc_value, exc_tb = sys.exc_info()

        with patch("src.utils.tkinter_exception_hook.logger"):
            with patch.object(exc_value, "open") as mock_open:
                tkinter_exception_hook(exc_type, exc_value, exc_tb)

        mock_open.assert_called_once()

    def test_creates_internal_dialog_error_when_exc_is_not_base_dialog(self) -> None:
        try:
            raise ValueError("unexpected error")
        except ValueError:
            exc_type, exc_value, exc_tb = sys.exc_info()

        with patch("src.utils.tkinter_exception_hook.logger"):
            with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_cls:
                mock_instance: MagicMock = MagicMock()
                mock_cls.return_value = mock_instance
                tkinter_exception_hook(exc_type, exc_value, exc_tb)

        mock_cls.assert_called_once_with(message="unexpected error")
        mock_instance.open.assert_called_once()

    def test_logs_error_for_base_dialog_exception(self) -> None:
        try:
            raise ValidationDialogError("test error")
        except ValidationDialogError:
            exc_type, exc_value, exc_tb = sys.exc_info()

        with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
            with patch.object(exc_value, "open"):
                tkinter_exception_hook(exc_type, exc_value, exc_tb)

        mock_logger.error.assert_called_once()

    def test_logs_error_for_unknown_exception(self) -> None:
        try:
            raise RuntimeError("runtime problem")
        except RuntimeError:
            exc_type, exc_value, exc_tb = sys.exc_info()

        with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
            with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_cls:
                mock_cls.return_value = MagicMock()
                tkinter_exception_hook(exc_type, exc_value, exc_tb)

        mock_logger.error.assert_called_once()
