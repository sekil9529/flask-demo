# coding: utf-8

from types import SimpleNamespace

from flask import Request


class ExtRequest(Request):

    def __init__(self, *args, **kwargs):
        super(ExtRequest, self).__init__(*args, **kwargs)
        self.ext = SimpleNamespace()
