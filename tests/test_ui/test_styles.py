from src.ui.styles import Styles


class TestStyles:
    def test_primary_color_value(self) -> None:
        assert Styles.PRIMARY_COLOR == "#C98686"

    def test_secondary_color_value(self) -> None:
        assert Styles.SECONDARY_COLOR == "#dfc3c3"

    def test_white_color_value(self) -> None:
        assert Styles.WHITE_COLOR == "#FFFFFF"

    def test_black_color_value(self) -> None:
        assert Styles.BLACK_COLOR == "#000000"

    def test_font_roboto_value(self) -> None:
        assert Styles.FONT_ROBOTO == "Roboto"

    def test_font_roboto_12_contains_size(self) -> None:
        assert "12" in Styles.FONT_ROBOTO_12

    def test_font_roboto_13_contains_size(self) -> None:
        assert "13" in Styles.FONT_ROBOTO_13

    def test_font_roboto_15_contains_size(self) -> None:
        assert "15" in Styles.FONT_ROBOTO_15

    def test_font_roboto_12_contains_font_name(self) -> None:
        assert "Roboto" in Styles.FONT_ROBOTO_12

    def test_instantiation_succeeds(self) -> None:
        styles: Styles = Styles()

        assert styles is not None
