# coding: utf-8

from core.error_code import ECEnum
from libs.error_code.exception import ECException


def error_test():
    """test error"""
    raise ECException(ECEnum.TestError)


def error_unknown():
    """unknown error"""
    raise
