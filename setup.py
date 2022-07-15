#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

setup(
    author='Holiest of Hand Grenades',
    author_email='holiestofhandgrenades@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Natural Language :: English',      
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Basic Python NZBGet API client.",
    install_requires=[],
    license="Apache Software License 2.0",
    include_package_data=True,
    keywords='pynzbgetapi',
    name='pynzbgetapi',
    packages=find_packages(include=['pynzbgetapi']),
    url='https://github.com/holiestofhandgrenades/pynzbgetapi',
    version='0.3.0',
    zip_safe=True,
)
