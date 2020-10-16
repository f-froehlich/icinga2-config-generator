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
from Commands.DockerLoginCommand import DockerLoginCommand
from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker


class CheckDockerLogin(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckDockerLogin', 'docker_login')
        self.__user = None
        self.__credentials = None
        self.__address = None
        self.__port = None
        self.__as_sudo = False

    def set_as_sudo(self, as_sudo):
        ValueChecker.is_bool(as_sudo)
        self.__as_sudo = as_sudo
        return self

    def get_as_sudo(self):
        return self.__as_sudo
    
    def set_user(self, user):
        ValueChecker.is_string(user)
        self.__user = user
        return self

    def get_user(self):
        return self.__user

    def set_credentials(self, credentials):
        ValueChecker.is_string(credentials)
        self.__credentials = credentials
        return self

    def get_credentials(self):
        return self.__credentials

    def set_port(self, port):
        ValueChecker.is_string(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    def set_address(self, address):
        ValueChecker.is_string(address)
        self.__address = address
        return self

    def get_address(self):
        return self.__address

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)
        check = ConfigBuilder.get_check(id)
        if None is check:
            id = 'check_' + id
            check = CheckDockerLogin(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('docker_login'):
            DockerLoginCommand.create('docker_login')

        return check
