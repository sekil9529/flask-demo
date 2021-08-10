# coding: utf-8

import time
import logging
from typing import Optional, Generator
from contextlib import contextmanager

from flask import Response, request

from .base import BaseRequestMiddleware

log = logging.getLogger()


class TimerMiddleware(BaseRequestMiddleware):
    """计时器中间件"""

    __slots__ = ('_start_time',)

    threshold: float = 1.0

    def __init__(self):
        super(TimerMiddleware, self).__init__()
        self._start_time: Optional[time.time] = None

    @contextmanager
    def _get_and_reset_start_time(self) -> Generator[Optional[float], None, None]:
        """获取重置 start_time"""
        try:
            yield self._start_time
        finally:
            self._start_time = None

    def before_request(self):
        self._start_time = time.time()

    def after_request(self, response: Response) -> Response:
        with self._get_and_reset_start_time() as start_time:
            if start_time is not None:
                diff = time.time() - start_time
                if diff > self.threshold:
                    log.warning('response timeout: %.6f' % diff)
                # else:
                #     log.info('response time: %.6f' % diff)
        return response


class NewTimerMiddleware(BaseRequestMiddleware):

    key: str = 'start_time'
    threshold: float = 1.0

    def before_request(self):
        setattr(request.ext, self.key, time.time())

    def after_request(self, response: Response) -> Response:
        if hasattr(request.ext, self.key):
            diff = time.time() - getattr(request.ext, self.key)
            if diff > self.threshold:
                log.warning('response timeout: %.6f' % diff)
        return response
