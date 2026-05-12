import tkinter as tk
from unittest.mock import MagicMock

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


class TestMainView:
    def test_is_instance_of_frame(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_calculate=MagicMock())

        assert isinstance(view, tk.Frame)

    def test_name_string_var_is_empty_on_init(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_calculate=MagicMock())

        assert view.name.get() == ""

    def test_year_string_var_is_empty_on_init(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_calculate=MagicMock())

        assert view.year.get() == ""

    def test_month_string_var_is_empty_on_init(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_calculate=MagicMock())

        assert view.month.get() == ""

    def test_day_string_var_is_empty_on_init(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_calculate=MagicMock())

        assert view.day.get() == ""

    def test_set_result_updates_result_text(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_calculate=MagicMock())

        view.set_result("Hi Alice, your age is 26.")

        assert view._result_text.get() == "Hi Alice, your age is 26."

    def test_set_result_accepts_empty_string(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_calculate=MagicMock())
        view.set_result("previous text")

        view.set_result("")

        assert view._result_text.get() == ""
