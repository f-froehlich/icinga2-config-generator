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
import typing

from icinga2confgen.Helpers.DefaultNames import get_default_group_name
from icinga2confgen.Helpers.Nameable import Nameable

T = typing.TypeVar('T', bound='Group')

class Group(Nameable):

    def __init__(self: T, id: str, type: str):
        Nameable.__init__(self)
        self.set_display_name(get_default_group_name(id))
        self.__id = id
        self.__type = type

    def get_id(self: T) -> str:
        return self.__id

    def get_custom_config(self: T) -> str:
        return ''

    def get_config(self: T) -> str:
        config = 'object ' + self.__type.capitalize() + 'Group "' + self.__type + 'group_' + self.get_id() + '" {\n'
        config += Nameable.get_config(self)
        config += self.get_custom_config()
        config += '  assign where "' + self.__type + 'group_' + self.get_id() + '" in ' + self.__type + '.vars.groups\n'
        config += '}\n'

        return config
