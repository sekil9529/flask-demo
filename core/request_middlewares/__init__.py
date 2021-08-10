# coding: utf-8

from .timer import TimerMiddleware, NewTimerMiddleware


REQUEST_MIDDLEWARE_TUPLE = (
    NewTimerMiddleware,
)
