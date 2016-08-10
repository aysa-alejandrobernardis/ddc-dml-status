#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# ~
# Author: Alejandro M. Bernardis
# Email: alejandro.bernardis@gmail.com
# Created: 09/ago/2016 10:49
# ~

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ, path
from aysa.ddc.dml.status import services

def abspath(*args):
    return path.abspath(path.join(*args))

root = None
ROOT_PATH = abspath(path.dirname(__file__))

class AySA(object):
    def __init__(self):
        self.db = None
        self.app = Flask('aysa_ddc_dml_status')
        self.init_app()

    def init_app(self):
        self.app.config.setdefault(
            'ROOT_PATH', ROOT_PATH)
        self.app.config.setdefault(
            'PUBLIC_PATH', abspath(ROOT_PATH, 'public'))

        self.app.config.setdefault(
            'SECRET_KEY', environ.get('SECRET_KEY'))

        self.app.config.setdefault(
            'SQLALCHEMY_DATABASE_URI', environ.get('DATABASE_URL'))
        self.app.config.setdefault(
            'SQLALCHEMY_TRACK_MODIFICATIONS',
            environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', True))

        self.app.static_url_path = '/static'
        self.app.static_folder = abspath(ROOT_PATH, 'public', 'static')
        self.db = SQLAlchemy(self.app)
        self.app.config['db'] = self.db

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

if __name__ == '__main__':
    root = AySA()
    root.app.register_blueprint(services.root)
    root.app.run(debug=True)
