#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# ~
# Author: Alejandro M. Bernardis
# Email: alejandro.bernardis@gmail.com
# Created: 09/Aug/2016 22:26
# ~

from flask import Blueprint, current_app, render_template

#
root = Blueprint('services', __name__, template_folder='templates')


#
@root.route('/')
def main():
    return render_template('index.html')
