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
from icinga2confgen.Commands.MonitoringPlugins.MRTGtrafCommand import MRTGtrafCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckMRTGtraf(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckMRTGtraf', 'mrt_gtraf')
        self.__file = None
        self.__aggregation = None
        self.__warning = None
        self.__critical = None
        self.__expires = None
        self.add_service_group(ServiceGroup.create('mrt_gtraf'))

    def set_file(self, file):
        ValueChecker.is_string(file)
        self.__file = file
        return self

    def get_file(self):
        return self.__file

    def set_aggregation(self, aggregation):
        ValueChecker.is_string(aggregation)
        self.__aggregation = aggregation
        return self

    def get_aggregation(self):
        return self.__aggregation

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

    def set_expires(self, expires):
        ValueChecker.is_string(expires)
        self.__expires = expires
        return self

    def get_expires(self):
        return self.__expires

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckMRTGtraf(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('mrt_gtraf'):
            MRTGtrafCommand.create('mrt_gtraf')

        return check

    def validate(self):
        if None is self.__file:
            raise Exception('You have to specify a file for ' + self.get_id())
        if None is self.__aggregation:
            raise Exception('You have to specify a aggregation for ' + self.get_id())
        if None is self.__warning:
            raise Exception('You have to specify a warning for ' + self.get_id())
        if None is self.__critical:
            raise Exception('You have to specify a critical for ' + self.get_id())
