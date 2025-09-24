from tkinter import Button, Entry, Label, StringVar, Tk

from src.utils.helpers import calculate_age, validate_inputs
from src.utils.messages import MESSAGE_HELLO
from src.utils.styles import (
    BG_COLOR,
    BUTTON_BG,
    BUTTON_FG,
    BUTTON_FONT,
    LABEL_FG,
    LABEL_FONT,
)


class InterfaceApp:
    def __init__(self, root: Tk, bg: str = BG_COLOR) -> None:
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.config(bg=bg)

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
        name, year, month, day = (
            self.name.get(),
            self.year.get(),
            self.month.get(),
            self.day.get(),
        )

        error = validate_inputs(name, year, month, day)
        if error:
            self.final_label["text"] = error
            return

        year, month, day = int(year), int(month), int(day)
        relative_age = calculate_age(year=year, month=month, day=day)
        self.final_label["text"] = MESSAGE_HELLO.format(name=name, age=relative_age)
