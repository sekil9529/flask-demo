# coding: utf-8

from __future__ import annotations

from .base import BaseRequestMiddleware
from .timer import TimerMiddleware


REQUEST_MIDDLEWARE_TUPLE: tuple[type[BaseRequestMiddleware], ...] = (
    TimerMiddleware,
)
