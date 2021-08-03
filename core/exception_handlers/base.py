# coding: utf-8

import abc
from typing import Type

from flask import Response


class BaseExcHandler(metaclass=abc.ABCMeta):
    """基础异常处理

    注意：必须@property在后，@abc.abstractmethod在前
    """

    @property
    @abc.abstractmethod
    def exception(self) -> Type[Exception]:
        """获取异常"""
        pass

    @abc.abstractmethod
    def handle(self, exception: Exception) -> Response:
        """异常处理"""
        pass
