from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_SUCCESS_AGE
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.utils.dialogs import ValidationDialogError


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock) -> InterfaceApp:
    with patch("src.ui.interface_app.MainView") as mock_main_view_class:
        mock_main_view_class.return_value = MagicMock()
        instance: InterfaceApp = InterfaceApp.__new__(InterfaceApp)
        instance._styles = mock_styles
        instance._config = MagicMock()
        instance._root = mock_root
        instance._main_view = mock_main_view_class.return_value
        return instance


class TestInterfaceAppInit:
    def test_stores_styles(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        assert app._styles is mock_styles

    def test_stores_root(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        assert app._root is mock_root

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

    def test_background_uses_primary_color(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.config.assert_called_once_with(background=mock_styles.PRIMARY_COLOR)

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

    def test_main_view_grid_called(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view: MagicMock = MagicMock()
            mock_main_view_class.return_value = mock_main_view
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_main_view.grid.assert_called_once_with(row=0, column=0, sticky="nsew")

    def test_columnconfigure_called_on_root(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.columnconfigure.assert_called_once_with(0, weight=1)

    def test_rowconfigure_called_on_root(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.rowconfigure.assert_called_once_with(0, weight=1)


class TestInterfaceAppGetCurrentAge:
    def test_raises_validation_error_when_validate_inputs_returns_error(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = ""
        interface_app._main_view.year.get.return_value = ""
        interface_app._main_view.month.get.return_value = ""
        interface_app._main_view.day.get.return_value = ""

        with (
            patch("src.ui.interface_app.validate_inputs", return_value="some error"),
            pytest.raises(ValidationDialogError) as exc_info,
        ):
            interface_app._get_current_age()

        assert exc_info.value.message == "some error"

    def test_set_result_not_called_when_validation_fails(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = ""
        interface_app._main_view.year.get.return_value = ""
        interface_app._main_view.month.get.return_value = ""
        interface_app._main_view.day.get.return_value = ""

        with (
            patch("src.ui.interface_app.validate_inputs", return_value="some error"),
            pytest.raises(ValidationDialogError),
        ):
            interface_app._get_current_age()

        interface_app._main_view.set_result.assert_not_called()

    def test_set_result_called_with_formatted_message(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = "Alice"
        interface_app._main_view.year.get.return_value = "1990"
        interface_app._main_view.month.get.return_value = "5"
        interface_app._main_view.day.get.return_value = "15"

        with (
            patch("src.ui.interface_app.validate_inputs", return_value=None),
            patch("src.ui.interface_app.calculate_age", return_value=34),
        ):
            interface_app._get_current_age()

        interface_app._main_view.set_result.assert_called_once_with(MESSAGE_SUCCESS_AGE.format(name="Alice", age=34))

    def test_calculate_age_called_with_int_values(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = "Bob"
        interface_app._main_view.year.get.return_value = "1995"
        interface_app._main_view.month.get.return_value = "3"
        interface_app._main_view.day.get.return_value = "20"

        with (
            patch("src.ui.interface_app.validate_inputs", return_value=None),
            patch("src.ui.interface_app.calculate_age", return_value=29) as mock_calculate,
        ):
            interface_app._get_current_age()

        mock_calculate.assert_called_once_with(year=1995, month=3, day=20)

    def test_validate_inputs_called_with_correct_values(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = "Alice"
        interface_app._main_view.year.get.return_value = "1990"
        interface_app._main_view.month.get.return_value = "5"
        interface_app._main_view.day.get.return_value = "15"

        with (
            patch("src.ui.interface_app.validate_inputs", return_value=None) as mock_validate,
            patch("src.ui.interface_app.calculate_age", return_value=34),
        ):
            interface_app._get_current_age()

        mock_validate.assert_called_once_with("Alice", "1990", "5", "15")

    def test_calculate_age_not_called_when_validation_fails(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = ""
        interface_app._main_view.year.get.return_value = ""
        interface_app._main_view.month.get.return_value = ""
        interface_app._main_view.day.get.return_value = ""

        with (
            patch("src.ui.interface_app.validate_inputs", return_value="error"),
            patch("src.ui.interface_app.calculate_age") as mock_calculate,
            pytest.raises(ValidationDialogError),
        ):
            interface_app._get_current_age()

        mock_calculate.assert_not_called()
