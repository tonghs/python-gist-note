#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from setuptools import setup, find_packages


# Read the long description from the README file.
_setup_folder = os.path.dirname(__file__)
with open(os.path.join(_setup_folder, 'README.rst')) as readme_file:
        long_description = readme_file.read()


setup(
    name='python-gist-note',
    version='0.1.0',
    keywords=('note', 'gist', 'gist-note', 'gn', 'code share'),
    description='just a simple code sharing tool powered by gist.',
    long_description=long_description,
    url='https://github.com/tonghuashuai/python-gist-note',
    license='MIT License',
    install_requires=['requests'],
    scripts=['python-gist-note/gn'],
    author='tonghs',
    author_email='tonghuashuai@gmail.com',
    packages=find_packages(),
    platforms='any',
)
