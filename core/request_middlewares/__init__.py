# coding: utf-8

from .timer import TimerMiddleware


REQUEST_MIDDLEWARE_TUPLE = (
    TimerMiddleware,
)
