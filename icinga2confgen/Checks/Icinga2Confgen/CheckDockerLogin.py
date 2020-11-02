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

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.Icinga2Confgen.DockerLoginCommand import DockerLoginCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckDockerLogin(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckDockerLogin', 'docker_login')
        self.__user = None
        self.__credentials = None
        self.__address = None
        self.__port = None
        self.__as_sudo = False
        self.add_service_group(ServiceGroup.create('docker'))

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
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckDockerLogin(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('docker_login'):
            DockerLoginCommand.create('docker_login')

        return check

    def validate(self):
        if None is self.__user:
            raise Exception('You have to specify a user for ' + self.get_id())
        if None is self.__credentials:
            raise Exception('You have to specify credentials for ' + self.get_id())
        if None is self.__port:
            raise Exception('You have to specify a port for ' + self.get_id())
        if None is self.__address:
            raise Exception('You have to specify an address for ' + self.get_id())
