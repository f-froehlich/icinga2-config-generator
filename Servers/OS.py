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

class OS:

    def __init__(self, id):
        self.__id = id
        self.__os = None

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)

        os = ConfigBuilder.get_os(id)
        if None is os:
            id = 'os_' + id
            os = OS(id)
            ConfigBuilder.add_os(id, os)

        return os

    def get_id(self):
        return self.__id

    def set_os(self, os):
        ValueChecker.is_string(os)
        HostGroup.create('hg_' + self.__id).set_display_name(os)
        self.__os = os
        return self

    def get_os(self):
        return self.__os


    def get_config(self):
        if None is self.__os:
            raise Exception('You have to specify OS for ' + self.__id)
        
        config = 'template Host "' + self.__id + '" {\n'
        config += '  vars.os = "' + self.__os + '"\n'
        config += '  vars.hostgroup_hg_' + self.__id + ' = true\n'
        config += '}\n'

        return config
