import os
from unittest.mock import patch

from src.configs.default_config import DefaultConfig


class TestDefaultConfig:
    def test_debug_is_false_by_default(self) -> None:
        config: DefaultConfig = DefaultConfig()

        assert config.DEBUG is False

    def test_testing_is_false_by_default(self) -> None:
        config: DefaultConfig = DefaultConfig()

        assert config.TESTING is False

    def test_tz_defaults_to_argentina(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            config: DefaultConfig = DefaultConfig()

        assert config.TZ == "America/Argentina/Buenos_Aires"

    def test_tz_reads_from_environment(self) -> None:
        with patch.dict(os.environ, {"TZ": "UTC"}):
            config: DefaultConfig = DefaultConfig()

        assert config.TZ == "UTC"

    def test_env_name_defaults_to_template(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            config: DefaultConfig = DefaultConfig()

        assert config.ENV_NAME == "template tkinter python"

    def test_env_name_reads_from_environment(self) -> None:
        with patch.dict(os.environ, {"ENV_NAME": "my-app"}):
            config: DefaultConfig = DefaultConfig()

        assert config.ENV_NAME == "my-app"
