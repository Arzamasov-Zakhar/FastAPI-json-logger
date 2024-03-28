"""Представление для работы с пользователями."""
from loguru import logger
from fastapi_utils.inferring_router import InferringRouter
from starlette import status
from starlette.responses import Response

user_router = InferringRouter()

@user_router.get("/get-ok-result")
async def get_ok_result() -> Response:
    """Вывод стандартных логов 200 ответа."""
    return Response(status_code=status.HTTP_200_OK)

@user_router.get("/get-loguru-info")
async def get_info_logs() -> None:
    """Вывод информационных логов."""
    text = "BIG TEXT FYI"
    logger.info(text)


@user_router.get("/raise-exception-logs-with-traceback")
async def get_raise_exception() -> None:
    """Вывод логов ошибки и traceback."""
    exc = "Some error"
    logger.error(exc)
    raise Exception(exc)
