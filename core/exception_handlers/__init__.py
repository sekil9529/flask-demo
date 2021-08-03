# coding: utf-8

from .error_code import ErrorCodeExcHandler
from .unknown import UnknownExcHandler


# 异常处理元组
EXC_HDL_TUPLE = (
    UnknownExcHandler,
    ErrorCodeExcHandler
)

