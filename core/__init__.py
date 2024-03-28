"""Основные core методы."""
import json
import logging
import re
import sys
import traceback

import json_logging
from loguru import logger

from app.config import settings

# Стандартная настройка для loguru.logger,
# нет необходимости везде добавлять logger.add без явной на это нужды
logger.configure(
    handlers=[{"sink": sys.stdout, "format": settings.LOGGER_RESPONSE_FORMAT}]
)


class CustomFormatter(logging.Formatter):
    """Класс формата для логов Fast API."""

    def format(self, record: logging.LogRecord) -> str:  # noqa  A003
        """Метод создания формата догов."""
        message = record.getMessage()
        match = re.match(
            r'^(?P<address>[\d.:]+) - "(?P<method>\w+) (?P<path>[^"]+) (?P<protocol>[^"]+)" (?P<status>\d+)$',
            message,
        )
        log_message = {}
        if match:
            log_message.update(
                {
                    "message": (
                        f"{match.group('address')} {match.group('method')} "
                        f"{match.group('path')} {match.group('protocol')} "
                        f"{int(match.group('status'))}"
                    ),
                    "address": match.group("address"),
                    "method": match.group("method"),
                    "path": match.group("path"),
                    "protocol": match.group("protocol"),
                    "status": int(match.group("status")),
                }
            )
        else:
            log_message["message"] = message
        log_message.update(
            {
                "time": self.formatTime(record),
                "level": record.levelname,
            }
        )
        if "NoneType" not in traceback.format_exc():
            log_message["traceback"] = traceback.format_exc()
            if settings.ENVIRONMENT == "local":
                logger.error(traceback.format_exc())
        return json.dumps(log_message)


def setup_logging() -> None:
    """Установка потоковой передачи FastAPI в json формате на стандартный вывод."""
    if json_logging._current_framework is None:
        json_logging.init_fastapi(
            enable_json=True, custom_formatter=CustomFormatter
        )
