from unittest.mock import MagicMock, patch

import pytest

from src.utils.dialogs import InternalDialogError, ValidationDialogError
from src.utils.tkinter_exception_hook import tkinter_exception_hook


@pytest.mark.unit
class TestTkinterExceptionHook:
    def test_opens_dialog_for_base_dialog_subclass(self) -> None:
        exc: ValidationDialogError = ValidationDialogError(message="validation failed")

        with patch.object(exc, "open") as mock_open:
            tkinter_exception_hook(type(exc), exc, None)

        mock_open.assert_called_once()

    def test_opens_internal_error_for_unknown_exception(self) -> None:
        exc: RuntimeError = RuntimeError("unexpected")

        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_cls:
            mock_instance: MagicMock = MagicMock()
            mock_cls.return_value = mock_instance
            tkinter_exception_hook(type(exc), exc, None)

        mock_cls.assert_called_once_with(message=str(exc))
        mock_instance.open.assert_called_once()

    def test_opens_internal_error_for_value_error(self) -> None:
        exc: ValueError = ValueError("bad value")

        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_cls:
            mock_instance: MagicMock = MagicMock()
            mock_cls.return_value = mock_instance
            tkinter_exception_hook(type(exc), exc, None)

        mock_cls.assert_called_once_with(message="bad value")

    def test_internal_dialog_error_subclass_calls_open_directly(self) -> None:
        exc: InternalDialogError = InternalDialogError(message="internal")

        with patch.object(exc, "open") as mock_open:
            tkinter_exception_hook(type(exc), exc, None)

        mock_open.assert_called_once()

    def test_message_passed_to_internal_dialog_matches_exception_message(self) -> None:
        exc: KeyError = KeyError("missing key")

        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_cls:
            mock_instance: MagicMock = MagicMock()
            mock_cls.return_value = mock_instance
            tkinter_exception_hook(type(exc), exc, None)

        mock_cls.assert_called_once_with(message=str(exc))
