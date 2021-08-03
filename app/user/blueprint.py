# coding: utf-8

from flask import Blueprint
from .views import UsersView

bp = Blueprint('user_api', __name__, url_prefix='/users')

bp.add_url_rule('', view_func=UsersView.as_view('users'))  # 用户
