# coding: utf-8

from typing import Type

from flask import Response

from .base import BaseExcHandler
from libs.error_code.exception import ECException
from core.response import response_fail


class ErrorCodeExcHandler(BaseExcHandler):
    """错误码异常处理"""

    @property
    def exception(self) -> Type[Exception]:
        return ECException

    def handle(self, exception: ECException) -> Response:
        return response_fail(enum=exception.enum)
