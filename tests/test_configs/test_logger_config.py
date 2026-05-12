import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger_instance(self) -> None:
        logger: logging.Logger = setup_logger("test-instance")

        assert isinstance(logger, logging.Logger)

    def test_returns_logger_with_default_name(self) -> None:
        logger: logging.Logger = setup_logger()

        assert logger.name == "tkinter-app"

    def test_returns_logger_with_custom_name(self) -> None:
        logger: logging.Logger = setup_logger("custom-name")

        assert logger.name == "custom-name"

    def test_logger_has_debug_level(self) -> None:
        logger: logging.Logger = setup_logger("test-level")

        assert logger.level == logging.DEBUG

    def test_logger_has_stream_handler(self) -> None:
        logger: logging.Logger = setup_logger("test-handler")
        handler_types: list[type] = [type(h) for h in logger.handlers]

        assert logging.StreamHandler in handler_types

    def test_calling_twice_does_not_add_duplicate_handlers(self) -> None:
        logger: logging.Logger = setup_logger("test-no-duplicate")
        count_first: int = len(logger.handlers)

        setup_logger("test-no-duplicate")
        count_second: int = len(logger.handlers)

        assert count_first == count_second
