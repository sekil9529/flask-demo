# coding: utf-8

from __future__ import annotations

from flask import Blueprint

from .user.blueprint import bp as user_bp
from .demo.blueprint import bp as demo_bp


# 蓝图元组
BP_TUPLE: tuple[Blueprint, ...] = (
    user_bp,
    demo_bp,
)
