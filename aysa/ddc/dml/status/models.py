#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# ~
# Author: Alejandro M. Bernardis
# Email: alejandro.bernardis@gmail.com
# Created: 09/Aug/2016 22:49
# ~

import datetime
from app import root

db = root.db
Base = db.make_declarative_base()


class BaseClass(Base):
    available = db.Column(db.Boolean(default=False))
    enabled = db.Column(db.Boolean(default=False))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    modified = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class User(BaseClass):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(256), unique=True)
    external = db.Column(db.Boolean(default=False))


class Task(BaseClass):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    reception_date = db.Column(db.DateTime)
    delivery_date = db.Column(db.DateTime)
    notes = db.Column(db.String(256 * 5))


class Municipality(BaseClass):
    __tablename__ = 'municipalities'
    id = db.Column(db.Integer, primary_key=True)
    iso2 = db.Column(db.String(2))
    iso3 = db.Column(db.String(3))
    name = db.Column(db.String(256 * 5))


class Module(BaseClass):
    __tablename__ = 'modules'
    id = db.Column(db.Integer, primary_key=True)
    municipality_id = db.Column(db.Integer)
    name = db.Column(db.String(256))


class Activity(BaseClass):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    modified_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    modified_date = db.Column(db.DateTime)
    modified_note = db.Column(db.String(256))
