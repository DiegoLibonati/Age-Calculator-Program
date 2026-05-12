import tkinter as tk

from src.ui.components.labeled_entry import LabeledEntry
from src.ui.styles import Styles


class TestLabeledEntry:
    def test_is_instance_of_frame(self, root: tk.Tk) -> None:
        variable: tk.StringVar = tk.StringVar(root)
        styles: Styles = Styles()

        widget: LabeledEntry = LabeledEntry(
            parent=root,
            label_text="Name:",
            styles=styles,
            variable=variable,
        )

        assert isinstance(widget, tk.Frame)

    def test_initializes_without_error(self, root: tk.Tk) -> None:
        variable: tk.StringVar = tk.StringVar(root)
        styles: Styles = Styles()

        widget: LabeledEntry = LabeledEntry(
            parent=root,
            label_text="Email:",
            styles=styles,
            variable=variable,
        )

        assert widget is not None

    def test_variable_binding_reflects_changes(self, root: tk.Tk) -> None:
        variable: tk.StringVar = tk.StringVar(root)
        styles: Styles = Styles()
        LabeledEntry(parent=root, label_text="Field:", styles=styles, variable=variable)

        variable.set("test value")

        assert variable.get() == "test value"

    def test_show_parameter_is_accepted(self, root: tk.Tk) -> None:
        variable: tk.StringVar = tk.StringVar(root)
        styles: Styles = Styles()

        widget: LabeledEntry = LabeledEntry(
            parent=root,
            label_text="Password:",
            styles=styles,
            variable=variable,
            show="*",
        )

        assert widget is not None

    def test_initializes_with_empty_variable_by_default(self, root: tk.Tk) -> None:
        variable: tk.StringVar = tk.StringVar(root)
        styles: Styles = Styles()
        LabeledEntry(parent=root, label_text="Field:", styles=styles, variable=variable)

        assert variable.get() == ""
