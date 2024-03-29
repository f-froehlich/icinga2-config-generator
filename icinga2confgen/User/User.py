#!/usr/bin/python3
# -*- coding: utf-8

from __future__ import annotations

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
from typing import List

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.UserGroup import UserGroup
from icinga2confgen.Helpers.Nameable import Nameable
from icinga2confgen.Notification.NotificationFunctions import NotificationFunctions
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class User(NotificationFunctions, Nameable):

    def __init__(self, id: str):
        NotificationFunctions.__init__(self)
        Nameable.__init__(self)
        self.__id = id
        self.__display_name = None
        self.__enable_notifications = True
        self.__states = ['OK', 'Warning', 'Critical', 'Unknown', 'Down']
        self.__allowed_states = ['OK', 'Warning', 'Critical', 'Unknown', 'Down']
        self.__types = [
            'Problem', 'Acknowledgement', 'Recovery', 'Custom', 'FlappingStart',
            'FlappingEnd', 'DowntimeStart', 'DowntimeEnd', 'DowntimeRemoved'
        ]
        self.__allowed_types = [
            'Problem', 'Acknowledgement', 'Recovery', 'Custom', 'FlappingStart',
            'FlappingEnd', 'DowntimeStart', 'DowntimeEnd', 'DowntimeRemoved'
        ]
        self.__groups = []
        self.__vars = []

    @staticmethod
    def create(id: str, force_create: bool = False) -> User:
        ValueChecker.validate_id(id)

        user = None if force_create else ConfigBuilder.get_user(id)
        if None is user:
            user = User(id)
            ConfigBuilder.add_user(id, user)

        return user

    def get_id(self) -> str:
        return self.__id

    def set_types(self, types: List[str]) -> User:
        for type in types:
            if type not in self.__allowed_types:
                raise Exception('Type ' + type + ' is not allowed')
        self.__types = types
        return self

    def get_types(self) -> List[str]:
        return self.__types

    def set_states(self, states: List[str]) -> User:
        for state in states:
            if state not in self.__allowed_states:
                raise Exception('State ' + state + ' is not allowed')
        self.__states = states
        return self

    def get_states(self) -> List[str]:
        return self.__states

    def add_group(self, group: UserGroup) -> User:

        if group not in self.__groups:
            self.__groups.append(group)
        return self

    def remove_group(self, group: UserGroup) -> User:

        if group in self.__groups:
            self.__groups.remove(group)
        return self

    def get_groups(self) -> List[UserGroup]:

        return self.__groups

    def add_var(self, key: str, value: any) -> User:

        self.__vars.append((key, value))

        return self

    def get_var(self, key: str) -> any:

        for var in self.__vars:
            if var[0] == key:
                return var[0]

        return None

    def remove_var(self, key: str) -> User:

        ValueChecker.is_string(key)
        var = self.get_var(key)
        if None is not var:
            self.__vars.remove((key, var))

        return self

    def set_enable_notifications(self, enable_notifications: bool) -> User:
        self.__enable_notifications = enable_notifications
        return self

    def get_enable_notifications(self) -> bool:
        return self.__enable_notifications

    def validate(self):
        return

    def get_config(self) -> str:
        self.validate()

        config = 'object User "user_' + self.__id + '" {\n'
        config += ValueMapper.parse_var('display_name', self.__display_name)
        config += Nameable.get_config(self)
        config += NotificationFunctions.get_config(self)
        config += ValueMapper.parse_var('groups', self.__groups, value_prefix='usergroup_')
        config += ValueMapper.parse_var('states', self.__states)
        config += ValueMapper.parse_var('types', self.__types)

        for var in self.__vars:
            config += '  var.' + var[0] + ' = ' + ValueMapper.parse_value_for_var(var[1]) + '\n'
        config += '}\n'

        return config
