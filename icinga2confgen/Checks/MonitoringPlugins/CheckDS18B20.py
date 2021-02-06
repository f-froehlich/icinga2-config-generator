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
from icinga2confgen.Commands.MonitoringPlugins.DS18B20Command import DS18B20Command
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckDS18B20(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckDS18B20', 'sensor_ds18b20')
        self.__device = None
        self.__path = None
        self.__name = None
        self.__warning = None
        self.__critical = None
        self.add_service_group(ServiceGroup.create('temperature'))

    def set_device(self, device):
        ValueChecker.is_string(device)
        self.__device = device
        return self

    def get_device(self):
        return self.__device

    def set_path(self, path):
        ValueChecker.is_string(path)
        self.__path = path
        return self

    def get_path(self):
        return self.__path

    def set_name(self, name):
        ValueChecker.is_string(name)
        self.__name = name
        return self

    def get_name(self):
        return self.__name

    def set_warning(self, warning):
        ValueChecker.is_number(warning)
        self.__warning = warning
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, critical):
        ValueChecker.is_number(critical)
        self.__critical = critical
        return self

    def get_critical(self):
        return self.__critical

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckDS18B20(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckDS18B20):
            raise Exception('Id must be for an instance of CheckDS18B20 but other instance is returned')

        if None is ConfigBuilder.get_command('sensor_ds18b20'):
            DS18B20Command.create('sensor_ds18b20')

        return check

    def validate(self):
        if None == self.__device:
            raise Exception("You have to set up a device")
