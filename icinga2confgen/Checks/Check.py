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

import typing
from ctypes import Union
from typing import List

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.Helpers import DefaultNames
from icinga2confgen.Helpers.Checkable import Checkable
from icinga2confgen.Helpers.PluginDirs import PluginDirs
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper

T = typing.TypeVar('T', bound='Check')

class Check(Checkable, PluginDirs):

    def __init__(self: T, id: str, class_name: str, command_name: str):
        Checkable.__init__(self)
        PluginDirs.__init__(self, True)
        self.__command_name = command_name
        self.__class_name = class_name
        self.__id = id
        self.__service_groups = []
        self.__check_type = "local"
        self.__allowed_check_types = ["local", "ssh"]
        self.set_display_name(DefaultNames.get_default_check_name(id, command_name))

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)

        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = Check(id, 'Check', 'check')
            ConfigBuilder.add_check(id, check)

        return check

    def validate(self: T):
        raise Exception('Each check must override validate method')

    def add_service_group(self: T, group: Union[ServiceGroup, str]) -> T:
        if isinstance(group, ServiceGroup):
            if group not in self.__service_groups:
                self.__service_groups.append(group)
        elif isinstance(group, str):
            group = ConfigBuilder.get_servicegroup(group)
            if None is group:
                raise Exception('ServiceGroup does not exist yet!')
            self.add_service_group(group)
        else:
            raise Exception('Can only add Servicegroup or id of Servicegroup!')

        return self

    def get_service_groups(self: T) -> List[ServiceGroup]:

        return self.__service_groups

    def get_id(self: T) -> str:
        return self.__id

    def set_check_type(self: T, type: str) -> T:
        if type in self.__allowed_check_types:
            self.__check_type = type
            return self
        raise Exception("Checktype must be " + ' or '.join(self.__allowed_check_types))

    def get_check_type(self) -> str:
        return self.__check_type

    def get_custom_definitions(self: T) -> List[str]:
        return []

    def get_command_name(self: T) -> str:
        return self.__command_name

    def get_config(self: T) -> str:
        self.validate()
        command_name = 'command_' + self.__command_name + '_' + self.__check_type
        if self.is_using_negation():
            command_name += '_negate'

        config = 'apply Service "' + self.get_id() + '" {\n'
        config += '  check_command = "' + command_name + '"\n'
        config += self.get_property_default_config()
        config += self.get_custom_property_config()
        config += self.get_custom_config()
        config += self.get_group_config()
        config += Checkable.get_config(self)
        config += PluginDirs.get_config(self)
        config += '  assign where "' + self.get_id() + '" in host.vars.checks\n'
        config += '}\n'

        return config

    def get_group_config(self: T) -> str:

        return ValueMapper.parse_var('vars.groups', self.__service_groups, value_prefix='servicegroup_')

    def get_custom_property_config(self: T) -> str:
        config = ''
        for line in self.get_custom_definitions():
            config += '  ' + line + '\n'

        return config

    def get_property_default_config(self: T) -> str:

        return ValueMapper.get_property_default_config(
            self,
            self.__class_name,
            ValueMapper.replace_command_prefixes(self.__command_name),
            'command'
        )

    def get_custom_config(self: T) -> str:
        return ''
