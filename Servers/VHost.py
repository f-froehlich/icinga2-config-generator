#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, commands, checks, ... in python
#
#  Copyright (c) 2020 Fabian Fröhlich <mail@f-froehlich.de> https://f-froehlich.de
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

from Checks.Check import Check
from Checks.CheckHttp import CheckHttp
from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker


class VHost:

    def __init__(self, id):
        self.__id = id
        self.__hostname = None
        self.__checks = []

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)

        vhost = ConfigBuilder.get_vhost(id)
        if None is vhost:
            id = 'vhost_' + id
            vhost = VHost(id)
            ConfigBuilder.add_vhost(id, vhost)

        return vhost

    def get_id(self):
        return self.__id

    def set_hostname(self, hostname):
        ValueChecker.is_string(hostname)
        self.__hostname = hostname
        return self

    def get_hostname(self):
        return self.__hostname

    def add_check(self, check):
        if isinstance(check, CheckHttp):
            check.set_vhost(self.__hostname)
            self.__checks.append(check.get_id())

        elif isinstance(check, Check):
            self.__checks.append(check.get_id())

        elif isinstance(check, str):
            check = ConfigBuilder.get_check(check)
            if None is check:
                raise Exception('Check does not exist yet!')

            return self.add_check(check)
        else:
            raise Exception('Can only add Check or id of Check!')

        return self

    def get_check_ids(self):

        return self.__checks

    def get_config(self):
        config = 'template Host "' + self.__id + '" {\n'
        for check in self.__checks:
            config += '  vars.' + check + ' = true\n'
        config += '}\n'

        return config
