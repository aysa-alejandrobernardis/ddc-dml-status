#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# ~
# Author: Alejandro M. Bernardis
# Email: alejandro.bernardis@gmail.com
# Created: 09/ago/2016 10:49
# ~

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from os import environ


class AySA(object):
    def __init__(self, app=None, db=None):
        self.app = app or Flask(__name__)
        self.init_app()
        self.db = db or SQLAlchemy(self.app)

    def init_app(self):
        self.app.config.setdefault(
            'SECRET_KEY', environ.get('SECRET_KEY'))
        self.app.config.setdefault(
            'SQLALCHEMY_DATABASE_URI', environ.get('DATABASE_URL'))

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)
application = AySA()


if __name__ == '__main__':
    application.run(debug=True)
