# coding: utf-8

from .user.blueprint import bp as user_bp
from .demo.blueprint import bp as demo_bp


# 蓝图元组
BP_TUPLE = (
    user_bp,
    demo_bp,
)
