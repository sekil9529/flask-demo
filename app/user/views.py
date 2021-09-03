# coding: utf-8

import time
from flask.views import MethodView
from flask import request, Response

from app.models import db, User
from core.response import response_ok
from libs.sqlalchemy.result import result_format


class UsersView(MethodView):
    """用户"""

    def get(self) -> Response:
        page: int = 1
        per_page: int = 10
        result = db.session.query(User.user_id, User.name, User.create_time). \
            where(User.is_deleted == 0).order_by(db.desc(User.create_time)). \
            offset((page - 1) * per_page).limit(per_page).all()
        result = result_format(result)
        # 测试慢日志记录
        time.sleep(1)
        return response_ok(result)

    # def post(self) -> Response:
    #     return response_ok()
