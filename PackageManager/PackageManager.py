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

from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker
from Groups.HostGroup import HostGroup

class PackageManager:

    def __init__(self, id):
        self.__id = id
        self.__manager = None

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)

        pm = ConfigBuilder.get_package_manager(id)
        if None is pm:
            id = 'package_manager_' + id
            pm = PackageManager(id)
            ConfigBuilder.add_package_manager(id, pm)

        return pm

    def get_id(self):
        return self.__id

    def set_manager(self, manager):
        ValueChecker.is_string(manager)
        self.__manager = manager
        return self

    def get_manager(self):
        return self.__manager

    def get_config(self):
        if None is self.__manager:
            raise Exception('You have to specify Manager for ' + self.__id)

        config = 'template Host "' + self.__id + '" {\n'
        config += '  vars.' + self.__id + ' = true\n'
        config += '}\n'

        return config


apt = PackageManager.create('apt').set_manager('apt')
yum = PackageManager.create('yum').set_manager('yum')
apk = PackageManager.create('apk').set_manager('apk')
rpm = PackageManager.create('rpm').set_manager('rpm')
dpkg = PackageManager.create('dpkg').set_manager('dpkg')
