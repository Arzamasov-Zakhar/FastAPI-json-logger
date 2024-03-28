"""App declaration and initialization."""
from typing import Any

from fastapi import FastAPI

from core import setup_logging


def init_app() -> Any:
    """Функция инициализации приложения."""
    app = FastAPI()
    setup_logging()
