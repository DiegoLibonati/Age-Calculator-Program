from tkinter import StringVar
from unittest.mock import MagicMock, patch

import pytest

from src.ui.views.main_view import MainView


@pytest.fixture
def main_view(mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> MainView:
    with (
        patch("src.ui.views.main_view.Frame.__init__", return_value=None),
        patch("src.ui.views.main_view.LabeledEntry"),
        patch("src.ui.views.main_view.Button"),
        patch("src.ui.views.main_view.Label"),
        patch("src.ui.views.main_view.StringVar"),
        patch.object(MainView, "columnconfigure"),
    ):
        instance: MainView = MainView.__new__(MainView)
        instance._styles = mock_styles
        instance._on_calculate = mock_on_calculate
        instance._result_text = MagicMock(spec=StringVar)
        instance.name = MagicMock(spec=StringVar)
        instance.year = MagicMock(spec=StringVar)
        instance.month = MagicMock(spec=StringVar)
        instance.day = MagicMock(spec=StringVar)
        return instance


class TestMainViewInit:
    def test_stores_styles(self, main_view: MainView, mock_styles: MagicMock) -> None:
        assert main_view._styles == mock_styles

    def test_stores_on_calculate(self, main_view: MainView, mock_on_calculate: MagicMock) -> None:
        assert main_view._on_calculate == mock_on_calculate

    def test_name_variable_is_created(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar") as mock_string_var,
            patch.object(MainView, "columnconfigure"),
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        assert mock_string_var.call_count >= 5

    def test_labeled_entry_created_for_name(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        calls: list[str | None] = [call.kwargs.get("label_text") for call in mock_labeled_entry.call_args_list]
        assert "Name" in calls

    def test_labeled_entry_created_for_year(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        calls: list[str | None] = [call.kwargs.get("label_text") for call in mock_labeled_entry.call_args_list]
        assert "Year" in calls

    def test_labeled_entry_created_for_month(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        calls: list[str | None] = [call.kwargs.get("label_text") for call in mock_labeled_entry.call_args_list]
        assert "Month" in calls

    def test_labeled_entry_created_for_day(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        calls: list[str | None] = [call.kwargs.get("label_text") for call in mock_labeled_entry.call_args_list]
        assert "Day" in calls

    def test_button_command_is_on_calculate(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        _, kwargs = mock_button.call_args
        assert kwargs.get("command") == mock_on_calculate


class TestMainViewSetResult:
    def test_set_result_updates_result_text(self, main_view: MainView) -> None:
        main_view.set_result("some result")
        main_view._result_text.set.assert_called_once_with("some result")

    def test_set_result_with_empty_string(self, main_view: MainView) -> None:
        main_view.set_result("")
        main_view._result_text.set.assert_called_once_with("")

    def test_set_result_with_error_message(self, main_view: MainView) -> None:
        main_view.set_result("Error occurred")
        main_view._result_text.set.assert_called_once_with("Error occurred")
