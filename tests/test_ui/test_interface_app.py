import tkinter as tk
from unittest.mock import patch

import pytest

from src.configs.testing_config import TestingConfig
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.utils.dialogs import ValidationDialogError


class TestInterfaceApp:
    def test_sets_window_title(self, root: tk.Tk) -> None:
        config: TestingConfig = TestingConfig()

        InterfaceApp(root=root, config=config, styles=Styles())

        assert root.title() == "Age Snap"

    def test_raises_validation_error_when_inputs_are_empty(self, root: tk.Tk) -> None:
        config: TestingConfig = TestingConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)

        with pytest.raises(ValidationDialogError):
            app._get_current_age()

    def test_raises_validation_error_when_year_is_not_numeric(self, root: tk.Tk) -> None:
        config: TestingConfig = TestingConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.name.set("Alice")
        app._main_view.year.set("abc")
        app._main_view.month.set("1")
        app._main_view.day.set("1")

        with pytest.raises(ValidationDialogError):
            app._get_current_age()

    def test_sets_result_on_valid_inputs(self, root: tk.Tk) -> None:
        config: TestingConfig = TestingConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.name.set("Alice")
        app._main_view.year.set("2000")
        app._main_view.month.set("1")
        app._main_view.day.set("1")

        with patch("src.ui.interface_app.calculate_age", return_value=26):
            app._get_current_age()

        result: str = app._main_view._result_text.get()
        assert "Alice" in result
        assert "26" in result
