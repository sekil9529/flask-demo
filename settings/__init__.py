# coding: utf-8

from enum import Enum, unique
from typing import Optional, Type

from .base import BaseSettings
from .development import Settings as DevSettings
from .production import Settings as ProSettings


@unique
class EnvEnum(Enum):
    """环境枚举类"""
    DEVELOPMENT: Type[BaseSettings] = DevSettings
    PRODUCTION: Type[BaseSettings] = ProSettings


def get_settings(env: Optional[str] = None) -> Type[BaseSettings]:
    """获取配置"""
    if env is None:
        env = 'DEVELOPMENT'
    settings = getattr(EnvEnum, env.upper()).value
    return settings
