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
from icinga2confgen.Commands.MonitoringPlugins.UPSCommand import UPSCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckUPS(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckUPS', 'ups')
        self.__host = None
        self.__port = 3493
        self.__ups = None
        self.__temperature = True
        self.__variable = None
        self.__timeout = None
        self.__warning = None
        self.__critical = None
        self.add_service_group(ServiceGroup.create('ups'))
        self.add_service_group(ServiceGroup.create('system_health'))

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

    def set_ups(self, ups):
        ValueChecker.is_string(ups)
        self.__ups = ups
        return self

    def get_ups(self):
        return self.__ups

    def set_temperature(self, temperature):
        ValueChecker.is_bool(temperature)
        self.__temperature = temperature
        return self

    def get_temperature(self):
        return self.__temperature

    def set_variable(self, variable):
        ValueChecker.is_string(variable)
        self.__variable = variable
        return self

    def get_variable(self):
        return self.__variable

    def set_warning(self, warning):
        ValueChecker.is_string(warning)
        self.__warning = warning
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, critical):
        ValueChecker.is_string(critical)
        self.__critical = critical
        return self

    def get_critical(self):
        return self.__critical

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckUPS(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('ups'):
            UPSCommand.create('ups')

        return check

    def validate(self):
        if None is self.__host:
            raise Exception('You have to specify a host for ' + self.get_id())
        if None is self.__ups:
            raise Exception('You have to specify a ups for ' + self.get_id())
