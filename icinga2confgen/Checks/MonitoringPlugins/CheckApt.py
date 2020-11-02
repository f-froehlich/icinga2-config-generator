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
from icinga2confgen.Commands.MonitoringPlugins.AptCommand import AptCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckApt(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckApt', 'apt')
        self.__timeout = 10
        self.__upgrade = None
        self.__dist_upgrade = None
        self.__no_upgrade = None
        self.__include = None
        self.__exclude = None
        self.__critical = None
        self.__only_critical = None
        self.__packages_warning = None
        self.__update = None
        self.set_check_interval('1h')
        self.add_service_group(ServiceGroup.create('updates'))
        self.add_service_group(ServiceGroup.create('apt'))

    def set_timeout(self, seconds):
        ValueChecker.is_number(seconds)
        self.__timeout = seconds
        return self

    def get_timeout(self):
        return self.__timeout

    def set_upgrade(self, opts):
        ValueChecker.is_string(opts)
        self.__upgrade = opts
        return self

    def get_upgrade(self):
        return self.__upgrade

    def set_dist_upgrade(self, opts):
        ValueChecker.is_string(opts)
        self.__dist_upgrade = opts
        return self

    def get_dist_upgrade(self):
        return self.__dist_upgrade

    def set_no_upgrade(self, opts):
        ValueChecker.is_string(opts)
        self.__no_upgrade = opts
        return self

    def get_no_upgrade(self):
        return self.__no_upgrade

    def set_include(self, expr):
        ValueChecker.is_string(expr)
        self.__include = expr
        return self

    def get_include(self):
        return self.__include

    def set_exclude(self, expr):
        ValueChecker.is_string(expr)
        self.__exclude = expr
        return self

    def get_exclude(self):
        return self.__exclude

    def set_critical(self, expr):
        ValueChecker.is_string(expr)
        self.__critical = expr
        return self

    def get_critical(self):
        return self.__critical

    def set_only_critical(self, enable):
        ValueChecker.is_bool(enable)
        self.__only_critical = enable
        return self

    def get_only_critical(self):
        return self.__only_critical

    def set_packages_warning(self, count):
        ValueChecker.is_number(count)
        self.__packages_warning = count
        return self

    def get_packages_warning(self):
        return self.__packages_warning

    def set_update(self, opts):
        ValueChecker.is_string(opts)
        self.__update = opts
        return self

    def get_update(self):
        return self.__update

    def get_custom_definitions(self):
        return []

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckApt(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('apt'):
            AptCommand.create('apt')

        return check

    def validate(self):
        pass
