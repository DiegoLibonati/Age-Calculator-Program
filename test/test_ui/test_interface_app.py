from unittest.mock import MagicMock, patch

import pytest

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

    def test_main_view_is_created(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_main_view_class.assert_called_once()

    def test_main_view_on_calculate_is_bound(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        _, kwargs = mock_main_view_class.call_args
        assert callable(kwargs.get("on_calculate"))


class TestInterfaceAppGetCurrentAge:
    def test_calls_set_result_with_error_when_inputs_invalid(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = ""
        interface_app._main_view.year.get.return_value = ""
        interface_app._main_view.month.get.return_value = ""
        interface_app._main_view.day.get.return_value = ""

        with patch("src.ui.interface_app.validate_inputs", return_value="Please complete all fields."):
            interface_app._get_current_age()

        interface_app._main_view.set_result.assert_called_once_with("Please complete all fields.")

    def test_calls_set_result_with_age_when_inputs_valid(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = "Ana"
        interface_app._main_view.year.get.return_value = "1990"
        interface_app._main_view.month.get.return_value = "5"
        interface_app._main_view.day.get.return_value = "15"

        with (
            patch("src.ui.interface_app.validate_inputs", return_value=None),
            patch("src.ui.interface_app.calculate_age", return_value=34),
        ):
            interface_app._get_current_age()

        interface_app._main_view.set_result.assert_called_once()
        call_arg: str = interface_app._main_view.set_result.call_args[0][0]
        assert "Ana" in call_arg
        assert "34" in call_arg

    def test_does_not_call_calculate_age_when_error(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.get.return_value = ""
        interface_app._main_view.year.get.return_value = ""
        interface_app._main_view.month.get.return_value = ""
        interface_app._main_view.day.get.return_value = ""

        with (
            patch("src.ui.interface_app.validate_inputs", return_value="error"),
            patch("src.ui.interface_app.calculate_age") as mock_calculate,
        ):
            interface_app._get_current_age()

        mock_calculate.assert_not_called()
