#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# ~
# Author: Alejandro M. Bernardis
# Email: alejandro.bernardis@gmail.com
# Created: 09/Aug/2016 22:49
# ~

from app import root
from flask_sqlalchemy import declarative_base

db = root.db
Base = declarative_base()


class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


class Task(Base):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer)
    reception_date = db.Column(db.DateTime)
    delivery_date = db.Column(db.DateTime)
    notes = db.Column(db.String(256 * 5))


class Municipality(Base):
    id = db.Column(db.Integer, primary_key=True)
    iso2 = db.Column(db.String(2))
    iso3 = db.Column(db.String(3))
    name = db.Column(db.String(256 * 5))


class Module(Base):
    id = db.Column(db.Integer, primary_key=True)
    municipality_id = db.Column(db.Integer)
    name = db.Column(db.String(256))
