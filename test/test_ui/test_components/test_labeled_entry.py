from unittest.mock import MagicMock, patch

import pytest

from src.ui.components.labeled_entry import LabeledEntry


@pytest.fixture
def labeled_entry(mock_styles: MagicMock, variable: MagicMock) -> LabeledEntry:
    with (
        patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
        patch("src.ui.components.labeled_entry.Label"),
        patch("src.ui.components.labeled_entry.Entry"),
        patch.object(LabeledEntry, "columnconfigure"),
    ):
        instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
        instance._styles = mock_styles
        return instance


class TestLabeledEntryInit:
    def test_stores_styles(self, labeled_entry: LabeledEntry, mock_styles: MagicMock) -> None:
        assert labeled_entry._styles == mock_styles

    def test_label_is_created_with_label_text(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label") as mock_label,
            patch("src.ui.components.labeled_entry.Entry"),
            patch.object(LabeledEntry, "columnconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            instance._styles = mock_styles
            LabeledEntry.__init__(
                instance,
                parent=MagicMock(),
                label_text="Name",
                styles=mock_styles,
                variable=variable,
            )

        _, kwargs = mock_label.call_args
        assert kwargs.get("text") == "Name"

    def test_entry_is_created_with_variable(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label") as mock_label,
            patch("src.ui.components.labeled_entry.Entry") as mock_entry,
            patch.object(LabeledEntry, "columnconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            mock_entry.return_value.grid = MagicMock()
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            instance._styles = mock_styles
            LabeledEntry.__init__(
                instance,
                parent=MagicMock(),
                label_text="Name",
                styles=mock_styles,
                variable=variable,
            )

        _, kwargs = mock_entry.call_args
        assert kwargs.get("textvariable") == variable

    def test_entry_show_is_set_when_provided(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label") as mock_label,
            patch("src.ui.components.labeled_entry.Entry") as mock_entry,
            patch.object(LabeledEntry, "columnconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            mock_entry.return_value.grid = MagicMock()
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            instance._styles = mock_styles
            LabeledEntry.__init__(
                instance,
                parent=MagicMock(),
                label_text="Password",
                styles=mock_styles,
                variable=variable,
                show="*",
            )

        _, kwargs = mock_entry.call_args
        assert kwargs.get("show") == "*"

    def test_entry_show_is_not_set_when_not_provided(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label") as mock_label,
            patch("src.ui.components.labeled_entry.Entry") as mock_entry,
            patch.object(LabeledEntry, "columnconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            mock_entry.return_value.grid = MagicMock()
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            instance._styles = mock_styles
            LabeledEntry.__init__(
                instance,
                parent=MagicMock(),
                label_text="Name",
                styles=mock_styles,
                variable=variable,
            )

        _, kwargs = mock_entry.call_args
        assert "show" not in kwargs

    def test_columnconfigure_called_for_both_columns(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label") as mock_label,
            patch("src.ui.components.labeled_entry.Entry") as mock_entry,
            patch.object(LabeledEntry, "columnconfigure") as mock_columnconfigure,
        ):
            mock_label.return_value.grid = MagicMock()
            mock_entry.return_value.grid = MagicMock()
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            instance._styles = mock_styles
            LabeledEntry.__init__(
                instance,
                parent=MagicMock(),
                label_text="Name",
                styles=mock_styles,
                variable=variable,
            )

        assert mock_columnconfigure.call_count == 2
