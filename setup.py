#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(
    name='python-gist-note',
    version='0.0.7',
    keywords=('note', 'gist', 'gist-note', 'gn'),
    description='just a simple gist note',
    license='MIT License',
    install_requires=['requests'],

    scripts=['python-gist-note/gn'],

    author='Samuel Tong',
    author_email='tonghuashuai@gmail.com',

    packages=find_packages(),
    platforms='any',
)
