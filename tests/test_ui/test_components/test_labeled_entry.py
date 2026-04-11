import tkinter as tk

import pytest

from src.ui.components.labeled_entry import LabeledEntry
from src.ui.styles import Styles


class TestLabeledEntry:
    @pytest.fixture(scope="function")
    def variable(self, root: tk.Tk) -> tk.StringVar:
        return tk.StringVar(master=root)

    @pytest.fixture(scope="function")
    def labeled_entry(self, root: tk.Tk, variable: tk.StringVar) -> LabeledEntry:
        return LabeledEntry(parent=root, label_text="Test:", styles=Styles(), variable=variable)

    def test_instantiation(self, labeled_entry: LabeledEntry) -> None:
        assert labeled_entry is not None

    def test_is_frame_subclass(self, labeled_entry: LabeledEntry) -> None:
        assert isinstance(labeled_entry, tk.Frame)

    def test_variable_initial_value_is_empty(self, variable: tk.StringVar) -> None:
        assert variable.get() == ""

    def test_variable_set_updates_value(self, variable: tk.StringVar) -> None:
        variable.set("hello")
        assert variable.get() == "hello"

    def test_variable_set_overwrites_previous_value(self, variable: tk.StringVar) -> None:
        variable.set("first")
        variable.set("second")
        assert variable.get() == "second"

    def test_instantiation_with_show_parameter(self, root: tk.Tk) -> None:
        var: tk.StringVar = tk.StringVar(master=root)
        entry: LabeledEntry = LabeledEntry(
            parent=root,
            label_text="Password:",
            styles=Styles(),
            variable=var,
            show="*",
        )
        assert entry is not None

    def test_instantiation_with_empty_show_parameter(self, root: tk.Tk) -> None:
        var: tk.StringVar = tk.StringVar(master=root)
        entry: LabeledEntry = LabeledEntry(
            parent=root,
            label_text="Name:",
            styles=Styles(),
            variable=var,
            show="",
        )
        assert entry is not None
