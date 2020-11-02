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
from icinga2confgen.Commands.MonitoringPlugins.SWAPCommand import SWAPCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckSWAP(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckSWAP', 'swap')
        self.__warning = 30
        self.__critical = 15
        self.__allswaps = False
        self.__no_swap = None
        self.add_service_group(ServiceGroup.create('swap'))
        self.add_service_group(ServiceGroup.create('system_health'))

    def set_warning(self, number):
        ValueChecker.is_number(number)
        self.__warning = number
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, number):
        ValueChecker.is_number(number)
        self.__critical = number
        return self

    def get_critical(self):
        return self.__critical

    def set_allswaps(self, enable):
        ValueChecker.is_bool(enable)
        self.__allswaps = enable
        return self

    def get_allswaps(self):
        return self.__allswaps

    def set_no_swap(self, state):
        ValueChecker.is_string(state)
        self.__no_swap = state
        return self

    def get_no_swap(self):
        return self.__no_swap

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckSWAP(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('swap'):
            SWAPCommand.create('swap')

        return check

    def validate(self):
        if None is self.__warning:
            raise Exception('You have to specify a warning percentage for ' + self.get_id())
        if None is self.__critical:
            raise Exception('You have to specify a critical percentage for ' + self.get_id())
