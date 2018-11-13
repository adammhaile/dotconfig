#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('./requirements.txt') as f:
    INSTALL_REQUIRES = f.read().splitlines()

setup(
    name="dotconfig",
    version="0.1",
    description="Super simple python module for parsing structured config files with overrides",
    url="https://github.com/adammhaile/dotconfig",
    license="LGPL v3.0",

    packages=['dotconfig'],
    include_package_data=True,

    install_requires=INSTALL_REQUIRES,

    dependency_links=[]
)