#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# ~
# Author: Alejandro M. Bernardis
# Email: alejandro.bernardis@gmail.com
# Created: 09/ago/2016 10:35
# ~

from setuptools import setup


setup(
    name='ddc-dml-status',
    version='0.0.1',
    url='https://github.com/aysa-alejandrobernardis/ddc-dml-status',
    license='MIT',
    author='Alejandro M. Bernardis',
    author_email='alejandro_m_bernardis@aysa.com.ar',
    maintainer='Alejandro M. Bernardis',
    maintainer_email='alejandro_m_bernardis@aysa.com.ar',
    description=u'Dirección Desarrollo de la Comunidad, Departemente de '
                u'Materiales y Logística. Seguimiento de Ordenes de Entrega.-',
    long_description=__doc__,
    py_modules=['aysa'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
