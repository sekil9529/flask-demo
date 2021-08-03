# coding: utf-8

import logging
from typing import Type

from flask import Response

from .base import BaseExcHandler
from core.response import response_fail

log = logging.getLogger()


class UnknownExcHandler(BaseExcHandler):
    """未知异常处理"""

    @property
    def exception(self) -> Type[Exception]:
        return Exception

    def handle(self, exception: Exception) -> Response:
        log.exception(exception)
        return response_fail()
