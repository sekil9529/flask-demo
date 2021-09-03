# coding: utf-8

from __future__ import annotations
from typing import Any
import os

from libs.config import Config

__all__ = (
    'BaseSettings',
    'BASE_DIR',
    'CONFIG_INFO'
)

# 项目根目录
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志文件路径
LOG_PATH: str = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

# 配置文件路径
CONFIG_INFO: dict[str, Any] = Config(os.path.join(BASE_DIR, '.env')).format()


class BaseSettings:
    """配置基类"""
    ENV: str
    DEBUG: bool = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI: str   # 连接uri
    SQLALCHEMY_COMMIT_ON_TEARDOWN: bool  # 每次请求结束后自动提交数据库改变
    SQLALCHEMY_TRACK_MODIFICATIONS: bool  # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
    SQLALCHEMY_POOL_SIZE: int  # 连接数
    SQLALCHEMY_MAX_OVERFLOW: int  # 可溢出的连接数
    SQLALCHEMY_POOL_RECYCLE: int  # 连接时长
    SQLALCHEMY_ENGINE_OPTIONS: dict[str, Any] = {}  # options

    # 日志配置
    LOGGING: dict[str, Any] = {
        'version': 1,
        'disable_existing_loggers': True,
        'loggers': {
            '': {
                'level': 'INFO',
                'handlers': ['console', 'info_file', 'error_file'],
                'propagate': False
            },
            'root': {
                'level': 'INFO',
                'handlers': ['console', 'info_file', 'error_file'],
                'propagate': False
            },
        },
        'formatters': {
            'default': {
                'format': '[%(asctime)s.%(msecs).3d] - [%(levelname)s] - [%(name)s:%(lineno)d] - [%(message)s]',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'default',
            },
            'info_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'info.log'),
                'maxBytes': 5 * 1024 * 1024,
                'backupCount': 10,
                'encoding': 'utf8',
                'level': 'INFO',
                'formatter': 'default',
            },
            'error_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'error.log'),
                'maxBytes': 5 * 1024 * 1024,
                'backupCount': 10,
                'encoding': 'utf8',
                'level': 'ERROR',
                'formatter': 'default',
            },
        },
    }
