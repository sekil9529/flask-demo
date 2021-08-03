# coding: utf-8

import abc
from typing import Callable

from werkzeug.wsgi import ClosingIterator


class BaseWSGIMiddleware(metaclass=abc.ABCMeta):
    """WSGI中间件基类

    注意：WSGI中间件不在 Request上下文生命周期中无法使用 request对象
    """

    __slots__ = ('_wsgi_app',)

    def __init__(self, wsgi_app: Callable):
        self._wsgi_app: Callable = wsgi_app

    @abc.abstractmethod
    def before_request_context(self) -> None:
        """request_context前"""
        pass

    @abc.abstractmethod
    def after_request_context(self, response: ClosingIterator) -> ClosingIterator:
        """request_context后"""
        pass

    def __call__(self, environ: dict, start_response: Callable):
        self.before_request_context()
        response: ClosingIterator = self._wsgi_app(environ, start_response)
        return self.after_request_context(response)
