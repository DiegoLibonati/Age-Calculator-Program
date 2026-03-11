from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_NOT_VALID_FIELDS, MESSAGE_SUCCESS_AGE
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock) -> InterfaceApp:
    with patch("src.ui.interface_app.MainView") as mock_main_view_class:
        mock_main_view: MagicMock = MagicMock()
        mock_main_view.grid = MagicMock()
        mock_main_view_class.return_value = mock_main_view
        instance: InterfaceApp = InterfaceApp.__new__(InterfaceApp)
        instance._styles = mock_styles
        instance._root = mock_root
        instance._config = MagicMock()
        instance._main_view = mock_main_view
        return instance


class TestInterfaceAppInit:
    def test_stores_styles(self, interface_app: InterfaceApp, mock_styles: MagicMock) -> None:
        assert interface_app._styles == mock_styles

    def test_stores_root(self, interface_app: InterfaceApp, mock_root: MagicMock) -> None:
        assert interface_app._root == mock_root

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_root.title.assert_called_once_with("Age Calculator")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_root.geometry.assert_called_once_with("400x300")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_root.resizable.assert_called_once_with(False, False)

    def test_default_styles_is_styles_instance(self, mock_root: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock())

        assert isinstance(app._styles, Styles)

    def test_main_view_receives_on_calculate(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        _, kwargs = mock_main_view_class.call_args
        assert callable(kwargs.get("on_calculate"))


class TestInterfaceAppGetCurrentAge:
    def test_validation_dialog_called_when_inputs_are_invalid(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = ""
        interface_app._main_view.year.get.return_value = ""
        interface_app._main_view.month.get.return_value = ""
        interface_app._main_view.day.get.return_value = ""

        with (
            patch("src.ui.interface_app.validate_inputs", return_value=MESSAGE_NOT_VALID_FIELDS),
            patch("src.ui.interface_app.ValidationDialogError") as mock_dialog_class,
        ):
            mock_dialog_class.return_value = MagicMock()
            interface_app._get_current_age()

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_VALID_FIELDS)
        mock_dialog_class.return_value.dialog.assert_called_once()

    def test_set_result_not_called_when_inputs_are_invalid(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = ""
        interface_app._main_view.year.get.return_value = ""
        interface_app._main_view.month.get.return_value = ""
        interface_app._main_view.day.get.return_value = ""

        with (
            patch("src.ui.interface_app.validate_inputs", return_value=MESSAGE_NOT_VALID_FIELDS),
            patch("src.ui.interface_app.ValidationDialogError") as mock_dialog_class,
        ):
            mock_dialog_class.return_value = MagicMock()
            interface_app._get_current_age()

        interface_app._main_view.set_result.assert_not_called()

    def test_set_result_called_with_formatted_message(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = "Alice"
        interface_app._main_view.year.get.return_value = "2000"
        interface_app._main_view.month.get.return_value = "6"
        interface_app._main_view.day.get.return_value = "15"

        with (
            patch("src.ui.interface_app.validate_inputs", return_value=None),
            patch("src.ui.interface_app.calculate_age", return_value=25),
        ):
            interface_app._get_current_age()

        expected: str = MESSAGE_SUCCESS_AGE.format(name="Alice", age=25)
        interface_app._main_view.set_result.assert_called_once_with(expected)

    def test_calculate_age_called_with_parsed_integers(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = "Alice"
        interface_app._main_view.year.get.return_value = "2000"
        interface_app._main_view.month.get.return_value = "6"
        interface_app._main_view.day.get.return_value = "15"

        with (
            patch("src.ui.interface_app.validate_inputs", return_value=None),
            patch("src.ui.interface_app.calculate_age", return_value=25) as mock_calculate,
        ):
            interface_app._get_current_age()

        mock_calculate.assert_called_once_with(year=2000, month=6, day=15)

    def test_validation_dialog_not_called_when_inputs_are_valid(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = "Alice"
        interface_app._main_view.year.get.return_value = "2000"
        interface_app._main_view.month.get.return_value = "6"
        interface_app._main_view.day.get.return_value = "15"

        with (
            patch("src.ui.interface_app.validate_inputs", return_value=None),
            patch("src.ui.interface_app.calculate_age", return_value=25),
            patch("src.ui.interface_app.ValidationDialogError") as mock_dialog_class,
        ):
            interface_app._get_current_age()

        mock_dialog_class.assert_not_called()

    def test_validate_inputs_called_with_all_fields(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = "Alice"
        interface_app._main_view.year.get.return_value = "2000"
        interface_app._main_view.month.get.return_value = "6"
        interface_app._main_view.day.get.return_value = "15"

        with (
            patch("src.ui.interface_app.validate_inputs", return_value=None) as mock_validate,
            patch("src.ui.interface_app.calculate_age", return_value=25),
        ):
            interface_app._get_current_age()

        mock_validate.assert_called_once_with("Alice", "2000", "6", "15")
