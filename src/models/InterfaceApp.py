from datetime import datetime
from tkinter import Button, Entry, Label, StringVar, Tk

from src.utils.constants import (
    BG_COLOR,
    BUTTON_BG,
    BUTTON_FG,
    BUTTON_FONT,
    ERROR_FUTURE_DATE,
    ERROR_INVALID_DATE,
    ERROR_MISSING_VALUES,
    ERROR_MONTH_RANGE,
    ERROR_NON_NUMERIC,
    LABEL_FG,
    LABEL_FONT,
)


class InterfaceApp:
    def __init__(self, root: Tk, bg: str = "#C98686") -> None:
        # APP Config
        self.root = root
        self.root.title = "Age Calculator"
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.config(bg=bg)

        # Create widges
        self.__create_widgets()

    def __create_widgets(self) -> None:
        self.name = StringVar()
        self.year = StringVar()
        self.month = StringVar()
        self.day = StringVar()

        Label(
            self.root, font=LABEL_FONT, text="Name: ", bg=BG_COLOR, fg=LABEL_FG
        ).place(x=10, y=10)
        Entry(self.root, font=LABEL_FONT, textvariable=self.name).place(x=100, y=10)

        Label(
            self.root, font=LABEL_FONT, text="Year: ", bg=BG_COLOR, fg=LABEL_FG
        ).place(x=10, y=50)
        Entry(self.root, font=LABEL_FONT, textvariable=self.year).place(x=100, y=50)

        Label(
            self.root, font=LABEL_FONT, text="Month: ", bg=BG_COLOR, fg=LABEL_FG
        ).place(x=10, y=90)
        Entry(self.root, font=LABEL_FONT, textvariable=self.month).place(x=100, y=90)

        Label(self.root, font=LABEL_FONT, text="Day: ", bg=BG_COLOR, fg=LABEL_FG).place(
            x=10, y=130
        )
        Entry(self.root, font=LABEL_FONT, textvariable=self.day).place(x=100, y=130)

        Button(
            self.root,
            font=BUTTON_FONT,
            bg=BUTTON_BG,
            fg=BUTTON_FG,
            text="Calculate age",
            command=self._get_current_age,
        ).place(x=200, y=200, anchor="center")

        self.final_label = Label(self.root, font=LABEL_FONT, bg=BG_COLOR, fg=LABEL_FG)
        self.final_label.place(x=200, y=250, anchor="center")

    def _get_current_age(self) -> None:
        name = self.name.get()

        try:
            year = int(self.year.get())
            month = int(self.month.get())
            day = int(self.day.get())
        except ValueError:
            self.final_label["text"] = ERROR_NON_NUMERIC
            return

        if not name or not year or not month or not day:
            self.final_label["text"] = ERROR_MISSING_VALUES
            return
        elif year > datetime.now().year:
            self.final_label["text"] = ERROR_FUTURE_DATE
            return
        elif not (1 <= month <= 12):
            self.final_label["text"] = ERROR_MONTH_RANGE
            return
        elif not self.is_valid_date(year, month, day):
            self.final_label["text"] = ERROR_INVALID_DATE
            return

        self._calculate_age(name=name, day=day, month=month, year=year)

    def _calculate_age(self, name: str, year: int, month: int, day: int) -> None:
        current_date = datetime.now()
        relative_age = (
            current_date.year - year
            if month < current_date.month
            or month == current_date.month
            and day <= current_date.day
            else current_date.year - year - 1
        )
        self.final_label["text"] = f"Hi {name}, your age is {relative_age}."

    @staticmethod
    def is_valid_date(year: int, month: int, day: int) -> bool:
        try:
            datetime(year, month, day)
            return True
        except ValueError:
            return False
