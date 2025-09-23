from tkinter import Tk

from pytest import fixture

from src.ui.interface_app import InterfaceApp


@fixture
def interface_app() -> InterfaceApp:
    root = Tk()
    return InterfaceApp(root=root)
