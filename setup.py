# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import django_eve_mon
version = django_eve_mon.__version__

setup(
    name='project_name is the title of the project.',
    version=version,
    author='',
    author_email='wengole@gmail.com',
    packages=[
        'django_eve_mon',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['django_eve_mon/manage.py'],
)