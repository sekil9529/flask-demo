# coding: utf-8

from __future__ import annotations

from .base import BaseWSGIMiddleware
from .test import TestMiddleware

WSGI_MIDDLEWARE_TUPLE: tuple[type[BaseWSGIMiddleware, ...]] = (
    TestMiddleware,
)
