from tkinter import Tk

from src.configs.default_config import DefaultConfig
from src.constants.messages import MESSAGE_SUCCESS_AGE
from src.ui.styles import Styles
from src.ui.views.main_view import MainView
from src.utils.dialogs import ValidationDialogError
from src.utils.helpers import calculate_age, validate_inputs


class InterfaceApp:
    def __init__(self, root: Tk, config: DefaultConfig, styles: Styles = Styles()) -> None:
        self._styles = styles
        self._config = config
        self._root = root
        self._root.title("Age Calculator")
        self._root.geometry("400x300")
        self._root.resizable(False, False)
        self._root.config(background=self._styles.PRIMARY_COLOR)

        self._main_view = MainView(
            root=self._root,
            styles=self._styles,
            on_calculate=self._get_current_age,
        )
        self._main_view.grid(row=0, column=0, sticky="nsew")
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)

    def _get_current_age(self) -> None:
        name = self._main_view.name.get()
        year = self._main_view.year.get()
        month = self._main_view.month.get()
        day = self._main_view.day.get()

        error = validate_inputs(name, year, month, day)

        if error:
            raise ValidationDialogError(message=error)

        relative_age = calculate_age(year=int(year), month=int(month), day=int(day))
        self._main_view.set_result(MESSAGE_SUCCESS_AGE.format(name=name, age=relative_age))
