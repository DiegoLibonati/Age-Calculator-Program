import tkinter as tk

import pytest

from src.configs.default_config import DefaultConfig
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.utils.dialogs import ValidationDialogError


class TestInterfaceApp:
    @pytest.fixture(scope="function")
    def interface_app(self, root: tk.Tk) -> InterfaceApp:
        return InterfaceApp(root=root, config=DefaultConfig())

    def test_instantiation(self, interface_app: InterfaceApp) -> None:
        assert interface_app is not None

    def test_instantiation_with_custom_styles(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root=root, config=DefaultConfig(), styles=Styles())
        assert app is not None

    def test_get_current_age_raises_on_empty_name(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.set("")
        interface_app._main_view.year.set("1990")
        interface_app._main_view.month.set("1")
        interface_app._main_view.day.set("1")
        with pytest.raises(ValidationDialogError):
            interface_app._get_current_age()

    def test_get_current_age_raises_on_all_empty_fields(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.set("")
        interface_app._main_view.year.set("")
        interface_app._main_view.month.set("")
        interface_app._main_view.day.set("")
        with pytest.raises(ValidationDialogError):
            interface_app._get_current_age()

    def test_get_current_age_raises_on_future_year(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.set("John")
        interface_app._main_view.year.set("9999")
        interface_app._main_view.month.set("1")
        interface_app._main_view.day.set("1")
        with pytest.raises(ValidationDialogError):
            interface_app._get_current_age()

    def test_get_current_age_raises_on_non_numeric_year(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.set("John")
        interface_app._main_view.year.set("abcd")
        interface_app._main_view.month.set("1")
        interface_app._main_view.day.set("1")
        with pytest.raises(ValidationDialogError):
            interface_app._get_current_age()

    def test_get_current_age_raises_on_invalid_date(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.set("John")
        interface_app._main_view.year.set("2000")
        interface_app._main_view.month.set("2")
        interface_app._main_view.day.set("30")
        with pytest.raises(ValidationDialogError):
            interface_app._get_current_age()

    def test_get_current_age_sets_result_on_valid_input(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.set("Alice")
        interface_app._main_view.year.set("1990")
        interface_app._main_view.month.set("1")
        interface_app._main_view.day.set("1")
        interface_app._get_current_age()
        result: str = interface_app._main_view._result_text.get()
        assert "Alice" in result
        assert "age is" in result

    def test_get_current_age_result_contains_name(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.name.set("Bob")
        interface_app._main_view.year.set("1985")
        interface_app._main_view.month.set("3")
        interface_app._main_view.day.set("20")
        interface_app._get_current_age()
        result: str = interface_app._main_view._result_text.get()
        assert "Bob" in result
