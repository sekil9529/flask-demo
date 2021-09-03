# coding: utf-8

from __future__ import annotations
from typing import Any, Optional
from datetime import datetime, date

from flask import jsonify, Response
from flask.json import JSONEncoder

from core.error_code import ECEnum
from libs.datetime import to_unix_timestamp


class ExtJSONEncoder(JSONEncoder):
    """扩展JSONEncoder"""

    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):  # datetime类型
            return to_unix_timestamp(o)  # unix时间戳
        elif isinstance(o, date):  # 日期类型
            return to_unix_timestamp(o)
        return super(ExtJSONEncoder, self).default(o)


def response_ok(data: Any = None) -> Response:
    """成功返回

    :param data: 数据
    :return:
    """
    # 错误码
    code: str = '0'
    # 内容
    content: dict[str, Any] = dict(code=code, data=data)
    return jsonify(content)


def response_fail(
        enum: Optional[ECEnum] = None,
        desc: Any = '') -> Response:
    """失败返回

    :param enum: 错误码枚举类
    :param desc: 错误详情
    :return:
    """
    if enum is None:
        enum = ECEnum.ServerError
    # 错误码
    code: str = str(enum.code)
    # error码
    error: str = enum.error
    # 错误信息
    message: str = enum.message
    # 内容
    content: dict[str, Any] = dict(code=code, error=error, message=message, desc=desc)
    # 响应状态码
    status_code = 500 if code == '500' else 400
    response: Response = jsonify(content)
    response.status_code = status_code
    return response
