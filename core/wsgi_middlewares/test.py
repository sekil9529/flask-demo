# coding: utf-8

import time
import logging

from flask import Response
from werkzeug.wsgi import ClosingIterator

from .base import BaseWSGIMiddleware

log = logging.getLogger(__name__)


class TestMiddleware(BaseWSGIMiddleware):
    """测试"""

    def before_request_context(self) -> None:
        print('before_request_context')

    def after_request_context(self, response: ClosingIterator) -> ClosingIterator:
        print('after_request_context')
        return response
