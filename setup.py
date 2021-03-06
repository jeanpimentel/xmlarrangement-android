#!/usr/bin/env python
# coding: utf-8
#
# <XML Arrangement Rules Generator for Android CodeStyle>
# Copyright (C) 2016  Jean Pimentel <contato@jeanpimentel.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

from setuptools import setup, find_packages

from xmlarrangementandroid import __version__

local_file = lambda f: \
    open(os.path.join(os.path.dirname(__file__), f)).read()

if __name__ == '__main__':
    setup(
        name='xmlarrangement-android',
        version=__version__,
        description='XML Arrangement Rules Generator for Android CodeStyle',
        long_description=local_file('README.md'),
        author='Jean Pimentel',
        author_email='contato@jeanpimentel.com.br',
        url='https://github.com/jeanpimentel/xmlarrangement-android',
        packages=find_packages(),
        entry_points={
            'console_scripts': ['xmlarrangement-android = xmlarrangementandroid:main'],
        }
    )
