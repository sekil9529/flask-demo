# coding: utf-8

from werkzeug.wsgi import ClosingIterator

from libs.logger import LoggerProxy
from .base import BaseWSGIMiddleware

logger = LoggerProxy(__name__)


class TestMiddleware(BaseWSGIMiddleware):
    """测试"""

    def before_request_context(self) -> None:
        print('before_request_context')

    def after_request_context(self, response: ClosingIterator) -> ClosingIterator:
        print('after_request_context')
        return response
