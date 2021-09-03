# coding: utf-8

import os
from app import create_app
from flask import Flask
from flask_script import Manager
from flask_apidoc.commands import GenerateApiDoc


app: Flask = create_app(os.environ.get('ENV', 'development'))
manager: Manager = Manager(app)
manager.add_command('apidoc', GenerateApiDoc())


if __name__ == '__main__':
    manager.run()
