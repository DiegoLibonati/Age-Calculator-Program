import tkinter as tk
from unittest.mock import MagicMock

import pytest

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


class TestMainView:
    @pytest.fixture(scope="function")
    def on_calculate(self) -> MagicMock:
        return MagicMock()

    @pytest.fixture(scope="function")
    def main_view(self, root: tk.Tk, on_calculate: MagicMock) -> MainView:
        return MainView(root=root, styles=Styles(), on_calculate=on_calculate)

    def test_instantiation(self, main_view: MainView) -> None:
        assert main_view is not None

    def test_is_frame_subclass(self, main_view: MainView) -> None:
        assert isinstance(main_view, tk.Frame)

    def test_name_default_value(self, main_view: MainView) -> None:
        assert main_view.name.get() == ""

    def test_year_default_value(self, main_view: MainView) -> None:
        assert main_view.year.get() == ""

    def test_month_default_value(self, main_view: MainView) -> None:
        assert main_view.month.get() == ""

    def test_day_default_value(self, main_view: MainView) -> None:
        assert main_view.day.get() == ""

    def test_set_result_updates_result_text(self, main_view: MainView) -> None:
        main_view.set_result("Hi Alice, your age is 30.")
        assert main_view._result_text.get() == "Hi Alice, your age is 30."

    def test_set_result_overwrites_previous_value(self, main_view: MainView) -> None:
        main_view.set_result("first result")
        main_view.set_result("second result")
        assert main_view._result_text.get() == "second result"

    def test_set_result_initial_text_is_empty(self, main_view: MainView) -> None:
        assert main_view._result_text.get() == ""

    def test_on_calculate_callback_is_invoked(self, main_view: MainView, on_calculate: MagicMock) -> None:
        main_view._on_calculate()
        on_calculate.assert_called_once()

    def test_name_var_is_string_var(self, main_view: MainView) -> None:
        assert isinstance(main_view.name, tk.StringVar)

    def test_year_var_is_string_var(self, main_view: MainView) -> None:
        assert isinstance(main_view.year, tk.StringVar)

    def test_month_var_is_string_var(self, main_view: MainView) -> None:
        assert isinstance(main_view.month, tk.StringVar)

    def test_day_var_is_string_var(self, main_view: MainView) -> None:
        assert isinstance(main_view.day, tk.StringVar)
