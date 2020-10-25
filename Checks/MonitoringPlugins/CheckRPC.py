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

from Checks.Check import Check
from Commands.MonitoringPlugins.RPCCommand import RPCCommand
from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker


class CheckRPC(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckRPC', 'rpc')
        self.__host = None
        self.__command = None
        self.__port = None
        self.__version = None
        
    def set_host(self, host):
        ValueChecker.is_string(host)
        self.__host = host
        return self

    def get_host(self):
        return self.__host
        
    def set_command(self, command):
        ValueChecker.is_string(command)
        self.__command = command
        return self

    def get_command(self):
        return self.__command

    def set_port(self, port):
        ValueChecker.is_number(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    def set_version(self, version):
        ValueChecker.is_string(version)
        self.__version = version
        return self

    def get_version(self):
        return self.__version

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckRPC(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('rpc'):
            RPCCommand.create('rpc')

        return check
