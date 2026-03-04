from src.configs.default_config import DefaultConfig


class TestDefaultConfig:
    def test_debug_is_false(self) -> None:
        assert DefaultConfig.DEBUG is False

    def test_testing_is_false(self) -> None:
        assert DefaultConfig.TESTING is False

    def test_tz_has_default_value(self) -> None:
        assert DefaultConfig.TZ == "America/Argentina/Buenos_Aires"

    def test_env_name_has_default_value(self) -> None:
        assert DefaultConfig.ENV_NAME == "template tkinter python"

    def test_tz_is_string(self) -> None:
        assert isinstance(DefaultConfig.TZ, str)

    def test_env_name_is_string(self) -> None:
        assert isinstance(DefaultConfig.ENV_NAME, str)
