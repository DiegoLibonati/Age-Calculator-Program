from tkinter import Button, Frame, Label, StringVar, Tk

from src.ui.components.labeled_entry import LabeledEntry
from src.ui.styles import Styles


class MainView(Frame):
    def __init__(self, root: Tk, styles: Styles, on_calculate: callable) -> None:
        super().__init__(root, bg=styles.PRIMARY_COLOR)
        self._styles = styles
        self._on_calculate = on_calculate

        self.name = StringVar()
        self.year = StringVar()
        self.month = StringVar()
        self.day = StringVar()
        self._result_text = StringVar()

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.columnconfigure(0, weight=1)

        LabeledEntry(
            parent=self,
            label_text="Name",
            styles=self._styles,
            variable=self.name,
        ).grid(row=0, column=0, pady=(20, 5), sticky="ew")

        LabeledEntry(
            parent=self,
            label_text="Year",
            styles=self._styles,
            variable=self.year,
        ).grid(row=1, column=0, pady=5, sticky="ew")

        LabeledEntry(
            parent=self,
            label_text="Month",
            styles=self._styles,
            variable=self.month,
        ).grid(row=2, column=0, pady=5, sticky="ew")

        LabeledEntry(
            parent=self,
            label_text="Day",
            styles=self._styles,
            variable=self.day,
        ).grid(row=3, column=0, pady=5, sticky="ew")

        Button(
            self,
            font=self._styles.FONT_ROBOTO_15,
            bg=self._styles.BLACK_COLOR,
            fg=self._styles.WHITE_COLOR,
            text="Calculate age",
            command=self._on_calculate,
        ).grid(row=4, column=0, pady=(20, 5))

        Label(
            self,
            font=self._styles.FONT_ROBOTO_12,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
            textvariable=self._result_text,
        ).grid(row=5, column=0, pady=5)

    def set_result(self, text: str) -> None:
        self._result_text.set(text)
