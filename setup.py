#!/usr/bin/python3
# -*- coding: utf-8

#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, commands, checks, ... in python
#
#  Copyright (c) 2020 Fabian Fröhlich <mail@icinga2.confgen.org> https://icinga2.confgen.org
#
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  For all license terms see README.md and LICENSE Files in root directory of this Project.

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='icinga2confgen',
    version='0.0.4',
    description='Icinga2 configuration file generator for hosts, commands, checks, ... in python',
    long_description_content_type="text/markdown",
    long_description=README,
    license='AGPLv3',
    packages=find_packages(),
    author='Fabian Fröhlich',
    author_email='mail@confgen.org',
    keywords=['icinga', 'icinga2', 'icinga2-configuration', 'icinga2-plugin', 'configuration',
              'configuration-management', 'monitoring', 'check', 'nagios', 'nagios-plugin', 'nrpe', 'healthcheck',
              'serverstatus', 'security', 'security-tools'],
    url='https://github.com/f-froehlich/icinga2-config-generator',
    download_url='https://pypi.org/project/icinga2confgen/'

)

install_requires = [
    'tqdm',
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
