# coding: utf-8

from __future__ import annotations
from typing import Any
from urllib.parse import quote_plus

from .base import *


class Settings(BaseSettings):
    """生产环境配置"""

    ENV: str = 'production'
    DEBUG: bool = False

    # SQLAlchemy配置
    SQLALCHEMY_DATABASE_URI: str = f"mysql+pymysql://{CONFIG_INFO['db']['user']}" \
                                   f":{quote_plus(CONFIG_INFO['db']['password'])}" \
                                   f"@{CONFIG_INFO['db']['host']}" \
                                   f":{CONFIG_INFO['db']['port']}" \
                                   f"/{CONFIG_INFO['db']['database']}" \
                                   f"?charset=utf8mb4"
    SQLALCHEMY_COMMIT_ON_TEARDOWN: bool = True  # 每次请求结束后自动提交数据库改变
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False  # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
    SQLALCHEMY_POOL_SIZE: int = 10  # 连接数
    SQLALCHEMY_MAX_OVERFLOW: int = 0  # 可溢出的连接数
    SQLALCHEMY_POOL_RECYCLE: int = 60 * 60 * 2  # 连接时长
    SQLALCHEMY_ENGINE_OPTIONS: dict[str, Any] = {
        'isolation_level': 'READ COMMITTED'  # RC隔离级别
    }
