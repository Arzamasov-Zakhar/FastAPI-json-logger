"""Модуль с настройками проекта."""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Класс с переменными окружения."""
    LOGGER_RESPONSE_FORMAT: str = (
        '{{"message": "{message}", "time": "{time:YYYY-MM-DD HH:mm:ss}",'
        ' "level": "{level}", "location": "{name}:{function}:{line}"}}'
    )
    ENVIRONMENT: str = "local"


settings = Settings()
