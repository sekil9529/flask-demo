# coding: utf-8

from __future__ import annotations

from flask import Response

from libs.logger import LoggerProxy
from .base import BaseExcHandler
from core.response import response_fail

logger: LoggerProxy = LoggerProxy(__name__)


class UnknownExcHandler(BaseExcHandler):
    """未知异常处理"""

    @property
    def exception(self) -> type[Exception]:
        return Exception

    def handle(self, exception: Exception) -> Response:
        logger.exception(exception)
        return response_fail()
