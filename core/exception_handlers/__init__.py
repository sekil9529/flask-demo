# coding: utf-8

from __future__ import annotations

from .base import BaseExcHandler
from .error_code import ErrorCodeExcHandler
from .unknown import UnknownExcHandler


# 异常处理元组（flask无需控制顺序）
EXC_HDL_TUPLE: tuple[type[BaseExcHandler], ...] = (
    ErrorCodeExcHandler,
    UnknownExcHandler,
)

