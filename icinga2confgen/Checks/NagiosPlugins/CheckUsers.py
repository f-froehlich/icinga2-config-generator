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
from icinga2confgen.Commands.NagiosPlugins.UsersCommand import UsersCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckUsers(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckUsers', 'nagios_plugins_users')
        self.__warning = 5
        self.__critical = 10
        self.add_service_group(ServiceGroup.create('user'))

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

    @staticmethod
    def create(id: str, force_create: bool = False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckUsers(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckUsers):
            raise Exception('Id must be for an instance of CheckUsers but other instance is returned')

        if None is ConfigBuilder.get_command('nagios_plugins_users'):
            UsersCommand.create('nagios_plugins_users')

        return check

    def validate(self):
        pass
