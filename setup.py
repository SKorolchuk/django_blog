#!/usr/bin/env python

from setuptools import setup

setup(
    name='MyPythonRestPit',
    version='0.1',
    description='Django Web Application hosted by OpenShift',
    author='Sergey Korolchuk',
    author_email='sergey.korolchuk.dev@gmil.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django<=1.5','djangorestframework<=10.0','markdown<=10.0','django-filter<=10.0'],
)