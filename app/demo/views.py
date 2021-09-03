# coding: utf-8

from flask import request, Response

from core.error_code import ECEnum
from libs.error_code.exception import ECException


def error_test() -> Response:
    """test error"""
    raise ECException(ECEnum.TestError)


def error_unknown() -> Response:
    """unknown error"""
    raise
