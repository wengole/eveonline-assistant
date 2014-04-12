# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import eveonline-assistant
version = eveonline-assistant.__version__

setup(
    name='EVE Online Assistant',
    version=version,
    author='',
    author_email='wengole@gmail.com',
    packages=[
        'eveonline-assistant',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['eveonline-assistant/manage.py'],
)