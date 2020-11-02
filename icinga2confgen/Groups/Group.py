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

from icinga2confgen.Utils.DefaultNames import get_default_group_name
from icinga2confgen.ValueChecker import ValueChecker


class Group:

    def __init__(self, id, type):
        self.__id = id
        self.__type = type
        self.__display_name = get_default_group_name(id)

    def set_display_name(self, name):
        ValueChecker.is_string(name)
        self.__display_name = name
        return self

    def get_display_name(self):
        return self.__display_name

    def get_id(self):
        return self.__id

    def get_config(self):
        config = 'object ' + self.__type.capitalize() + 'Group "' + self.__type + 'group_' + self.get_id() + '" {\n'
        if None is not self.__display_name:
            config += '  display_name = "' + self.__display_name + '"\n'
        config += '  assign where "' + self.__type + 'group_' + self.get_id() + '" in ' + self.__type + '.groups\n'
        config += '}\n'

        return config
