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
from icinga2confgen.Commands.MonitoringPlugins.RadiusCommand import RadiusCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckRadius(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckRadius', 'radius')
        self.__host = None
        self.__port = 1645
        self.__username = None
        self.__password = None
        self.__nas_id = None
        self.__nas_ip = None
        self.__config_file = None
        self.__expect = None
        self.__retries = 2
        self.__timeout = 10
        self.add_service_group(ServiceGroup.create('radius'))

    def set_host(self, host):
        ValueChecker.is_string(host)
        self.__host = host
        return self

    def get_host(self):
        return self.__host

    def set_port(self, port):
        ValueChecker.is_number(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    def set_username(self, username):
        ValueChecker.is_string(username)
        self.__username = username
        return self

    def get_username(self):
        return self.__username

    def set_password(self, password):
        ValueChecker.is_string(password)
        self.__password = password
        return self

    def get_password(self):
        return self.__password

    def set_nas_id(self, nas_id):
        ValueChecker.is_string(nas_id)
        self.__nas_id = nas_id
        return self

    def get_nas_id(self):
        return self.__nas_id

    def set_nas_ip(self, nas_ip):
        ValueChecker.is_string(nas_ip)
        self.__nas_ip = nas_ip
        return self

    def get_nas_ip(self):
        return self.__nas_ip

    def set_config_file(self, config_file):
        ValueChecker.is_string(config_file)
        self.__config_file = config_file
        return self

    def get_config_file(self):
        return self.__config_file

    def set_expect(self, expect):
        ValueChecker.is_string(expect)
        self.__expect = expect
        return self

    def get_expect(self):
        return self.__expect

    def set_retries(self, retries):
        ValueChecker.is_number(retries)
        self.__retries = retries
        return self

    def get_retries(self):
        return self.__retries

    def set_timeout(self, timeout):
        ValueChecker.is_number(timeout)
        self.__timeout = timeout
        return self

    def get_timeout(self):
        return self.__timeout

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckRadius(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('radius'):
            RadiusCommand.create('radius')

        return check

    def validate(self):
        if None is self.__host:
            raise Exception('You have to specify a host for ' + self.get_id())
        if None is self.__config_file:
            raise Exception('You have to specify a config file for ' + self.get_id())
        if None is self.__username:
            raise Exception('You have to specify a username for ' + self.get_id())
        if None is self.__password:
            raise Exception('You have to specify a password for ' + self.get_id())
