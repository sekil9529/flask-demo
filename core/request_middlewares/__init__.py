# coding: utf-8

from .timer import TimerMiddleware, NewTimerMiddleware, ContextVarTimerMiddleware


REQUEST_MIDDLEWARE_TUPLE = (
    ContextVarTimerMiddleware,
)
