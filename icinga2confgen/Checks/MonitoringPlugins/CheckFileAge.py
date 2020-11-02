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
from icinga2confgen.Commands.MonitoringPlugins.FileAgeCommand import FileAgeCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckFileAge(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckFileAge', 'file_age')
        self.__file = None
        self.__warning_seconds = None
        self.__critical_seconds = None
        self.__warning_size = None
        self.__critical_size = None
        self.__ignore_missing = False
        self.add_service_group(ServiceGroup.create('file_age'))

    def set_file(self, file):
        ValueChecker.is_string(file)
        self.__file = file
        return self

    def get_file(self):
        return self.__file

    def set_warning_seconds(self, seconds):
        ValueChecker.is_number(seconds)
        self.__warning_seconds = seconds
        return self

    def get_warning_seconds(self):
        return self.__warning_seconds

    def set_critical_seconds(self, seconds):
        ValueChecker.is_number(seconds)
        self.__critical_seconds = seconds
        return self

    def get_critical_seconds(self):
        return self.__critical_seconds

    def set_warning_size(self, size):
        ValueChecker.is_number(size)
        self.__warning_size = size
        return self

    def get_warning_size(self):
        return self.__warning_size

    def set_critical_size(self, size):
        ValueChecker.is_number(size)
        self.__critical_size = size
        return self

    def get_critical_size(self):
        return self.__critical_size

    def set_ignore_missing(self, ignore_missing):
        ValueChecker.is_bool(ignore_missing)
        self.__ignore_missing = ignore_missing
        return self

    def get_critical_ignore_missing(self):
        return self.__ignore_missing

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckFileAge(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('file_age'):
            FileAgeCommand.create('file_age')

        return check

    def validate(self):
        if None is self.__file:
            raise Exception('You have to specify a file for ' + self.get_id())
        if None is self.__warning_seconds:
            raise Exception('You have to specify warning seconds for ' + self.get_id())
        if None is self.__critical_seconds:
            raise Exception('You have to specify critical seconds for ' + self.get_id())
