# coding: utf-8

from flask import Blueprint
from .views import error_test, error_unknown

bp = Blueprint('demo_api', __name__, url_prefix='/demos')

bp.add_url_rule('error/test', view_func=error_test)
bp.add_url_rule('error/unknown', view_func=error_unknown)
