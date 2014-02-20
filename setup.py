#!/usr/bin/env python
#
#   Copyright (C) 2014 Rackspace, US Inc.
#
#   Author: Nate House <nathan.house@rackspace.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
from setuptools import setup

setup(
    name='horde',
    version='0.1.0',
    author='Nathan House',
    author_email='nathan.house@rackspace.com',
    packages=['horde', 'horde.BitTornado', 'horde.BitTornado.BT1'],
    scripts=[],
    url='http://github.com/naterh/Horde',
    description='Torrent distribution.',
    long_description=open('README.md').read(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'horde = horde.horde:entry_point',
        ],
    },
    data_files=[('horde', ['horde/bittornado.tar.gz'])]
)
