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

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker


class TimePeriod:

    def __init__(self, id):
        self.__id = id
        self.__display_name = None
        self.__ranges = []

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)

        period = None if force_create else ConfigBuilder.get_time_period(id)
        if None is period:
            period = TimePeriod(id)
            ConfigBuilder.add_time_period(id, period)

        return period

    def get_id(self):
        return self.__id

    def set_display_name(self, display_name):
        ValueChecker.is_string(display_name)
        self.__display_name = display_name
        return self

    def get_display_name(self):
        return self.__display_name

    def add_period(self, day, range):
        ValueChecker.is_string(day)
        ValueChecker.is_string(range)
        self.__ranges.append((day, range))
        return self

    def remove_period(self, day, range):
        ValueChecker.is_string(day)
        ValueChecker.is_string(range)
        self.__ranges.remove((day, range))
        return self

    def get_config(self):
        config = 'object TimePeriod "time_period_' + self.__id + '" {\n'

        if None is not self.__display_name:
            config += '  display_name = "' + self.__display_name + '"\n'

        config += '  ranges = {\n'
        for range in self.__ranges:
            config += '    "' + range[0] + '" = "' + range[1] + '"\n'
        config += '  }\n'
        config += '}\n'

        return config
