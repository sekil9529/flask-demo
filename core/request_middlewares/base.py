# coding: utf-8

import abc

from flask import Response


class BaseRequestMiddleware(metaclass=abc.ABCMeta):
    """Request中间件基类

    官方文档地址：https://flask.palletsprojects.com/en/2.0.x/reqcontext/
    官方文档中定义为：请求上下文（Request Context）生命周期内的回调（Callbacks）
        这里仅定义了 @app.before_request，@app.after_request 两个常用的回调
    """

    __slots__ = ()

    @abc.abstractmethod
    def before_request(self) -> None:
        """请求前"""
        pass

    @abc.abstractmethod
    def after_request(self, response: Response) -> Response:
        """请求后，响应前"""
        pass
