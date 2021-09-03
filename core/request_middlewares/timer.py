# coding: utf-8

import time
from contextvars import ContextVar

from flask import Response

from libs.logger import LoggerProxy
from .base import BaseRequestMiddleware

logger: LoggerProxy = LoggerProxy(__name__)

# 上下文变量
_TIME_VAR: ContextVar = ContextVar('time')


class TimerMiddleware(BaseRequestMiddleware):
    """计时器中间件"""

    threshold: float = 1.0

    def before_request(self) -> None:
        _TIME_VAR.set(time.time())

    def after_request(self, response: Response) -> Response:
        diff = time.time() - _TIME_VAR.get()
        if diff > self.threshold:
            logger.warning('response timeout: %.6f' % diff)
        return response
