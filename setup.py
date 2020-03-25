#!/usr/bin/env python
#
# Copyright (c) 2019 CoML
# Licensed Under EUPL 1.2

# AUTHORS
# Hadrien Titeux


from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='seshat-parser-sampa',
    packages=find_packages(),
    install_requires=["seshat-server",
                      "voxpopuli"],

    version="0.2",

    description='Parsers to check if some phonemic form is a valid SAMPA string',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Hadrien Titeux',
    author_email='hadrien.titeux@ens.fr',
    url='https://github.com/github/seshat-parser-template',

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering"
    ],
)
