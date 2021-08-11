# coding: utf-8

from importlib import import_module
from typing import Optional
from logging.config import dictConfig

from flask import Flask
from flask_cors import CORS
from flask_apidoc import ApiDoc

# from core.request import ExtRequest
from core.response import ExtJSONEncoder
from settings import get_settings


def create_app(env: Optional[str] = None) -> Flask:
    """创建app"""

    # 配置
    settings = get_settings(env)

    # 配置日志
    dictConfig(settings.LOGGING)

    # # Request扩展
    # Flask.request_class = ExtRequest
    # JSONEncoder扩展
    Flask.json_encoder = ExtJSONEncoder

    # app
    app: Flask = Flask(__name__)
    app.config.from_object(settings)

    # 注册Request中间件
    register_request_middleware(app)
    # 注册WSGI中间件
    # register_wsgi_middleware(app)
    # 注册异常处理
    register_exception_handler(app)
    # 注册蓝图
    register_blueprint(app)
    # 注册数据库
    register_db(app)

    # 跨域
    CORS(app)
    # ApiDoc
    ApiDoc(app)

    return app


def register_request_middleware(app: Flask) -> None:
    """注册Request中间件"""
    request_middleware_tuple = getattr(import_module('core.request_middlewares'), 'REQUEST_MIDDLEWARE_TUPLE')
    for request_middleware_cls in request_middleware_tuple:
        request_middleware = request_middleware_cls()
        if hasattr(request_middleware, 'before_request'):
            app.before_request(request_middleware.before_request)
        if hasattr(request_middleware, 'after_request'):
            app.after_request(request_middleware.after_request)
    return None


def register_wsgi_middleware(app: Flask) -> None:
    """注册WSGI中间件"""
    wsgi_middleware_tuple = getattr(import_module('core.wsgi_middlewares'), 'WSGI_MIDDLEWARE_TUPLE')
    for wsgi_middleware_cls in wsgi_middleware_tuple:
        app.wsgi_app = wsgi_middleware_cls(app.wsgi_app)
    return None


def register_blueprint(app: Flask, prefix: Optional[str] = '/api') -> None:
    """注册蓝图"""
    bp_tuple = getattr(import_module('app.blueprint'), 'BP_TUPLE')
    for bp in bp_tuple:
        bp.url_prefix = ''.join(url for url in (prefix, bp.url_prefix) if url)
        app.register_blueprint(bp)
    return None


def register_exception_handler(app: Flask) -> None:
    """注册异常处理"""
    exc_hdl_tuple = getattr(import_module('core.exception_handlers'), 'EXC_HDL_TUPLE')
    for exc_hdl_cls in exc_hdl_tuple:
        exc_hdl = exc_hdl_cls()
        app.register_error_handler(exc_hdl.exception, exc_hdl.handle)
    return None


def register_db(app: Flask) -> None:
    """注册数据库"""
    db = getattr(import_module('app.models'), 'db')
    db.init_app(app)
    return None
