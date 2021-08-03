# coding: utf-8

from .test import TestMiddleware

WSGI_MIDDLEWARE_TUPLE = (
    TestMiddleware,
)
