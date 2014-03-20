#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Flask-Debug',
    version='0.2',
    description='Shows reflection/configuration to aid the development of '
                'Flask applications.',
    long_description=read('README.rst'),
    include_package_data=True,
    author='Marc Brinkmann',
    author_email='git@marcbrinkmann.de',
    url='http://github.com/mbr/flask-debug',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=['flask'],
)
