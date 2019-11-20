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
    name='seshat.parser.pckgname',
    namespace_packages=['seshat'],
    packages=find_packages(),
    install_requires=["seshat-server",
                      # add any other dependencies here
                      ],

    version="0.1",

    description='Here be your parser module description',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='King Ju (ASFH)',
    author_email='kingju@asfh.fr',
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
