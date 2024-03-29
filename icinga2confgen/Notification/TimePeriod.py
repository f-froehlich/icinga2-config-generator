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

from __future__ import annotations

from typing import List, Tuple

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Helpers.Nameable import Nameable
from icinga2confgen.ValueChecker import ValueChecker


class TimePeriod(Nameable):

    def __init__(self, id: str):
        Nameable.__init__(self)
        self.__id = id
        self.__ranges = []

    @staticmethod
    def create(id: str, force_create: bool = False) -> TimePeriod:
        ValueChecker.validate_id(id)

        period = None if force_create else ConfigBuilder.get_time_period(id)
        if None is period:
            period = TimePeriod(id)
            ConfigBuilder.add_time_period(id, period)

        return period

    def get_id(self) -> str:
        return self.__id

    def add_period(self, day: str, range: str) -> TimePeriod:
        self.__ranges.append((day, range))
        return self

    def remove_period(self, day: str, range: str) -> TimePeriod:
        self.__ranges.remove((day, range))
        return self

    def get_period(self) -> List[Tuple[str, str]]:
        return self.__ranges

    def get_config(self) -> str:
        config = 'object TimePeriod "time_period_' + self.__id + '" {\n'
        config += Nameable.get_config(self)
        config += '  ranges = {\n'
        for range in self.__ranges:
            config += '    "' + range[0] + '" = "' + range[1] + '"\n'
        config += '  }\n'
        config += '}\n'

        return config
