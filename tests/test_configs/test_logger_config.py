import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-returns")
        assert isinstance(logger, logging.Logger)

    def test_logger_has_handlers(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-handlers")
        assert len(logger.handlers) > 0

    def test_logger_name_matches(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-name")
        assert logger.name == "test-logger-name"

    def test_logger_default_name(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.name == "tkinter-app"

    def test_logger_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-level")
        assert logger.level == logging.DEBUG

    def test_no_duplicate_handlers_on_repeated_call(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-no-dup")
        count_first: int = len(logger.handlers)
        setup_logger("test-logger-no-dup")
        count_second: int = len(logger.handlers)
        assert count_first == count_second
