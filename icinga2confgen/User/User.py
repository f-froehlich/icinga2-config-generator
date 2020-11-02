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
from icinga2confgen.Groups.UserGroup import UserGroup
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class User:

    def __init__(self, id):
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
        self.__phone = None
        self.__pager = None
        self.__email = []
        self.__pager = None
        self.__groups = []
        self.__vars = []

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)

        user = None if force_create else ConfigBuilder.get_user(id)
        if None is user:
            user = User(id)
            ConfigBuilder.add_user(id, user)

        return user

    def get_id(self):
        return self.__id

    def set_display_name(self, display_name):
        ValueChecker.is_string(display_name)
        self.__display_name = display_name
        return self

    def get_display_name(self):
        return self.__display_name

    def add_email(self, email):
        ValueChecker.is_string(email)
        self.__email.append(email)
        return self

    def remove_email(self, email):
        ValueChecker.is_string(email)
        self.__email.remove(email)
        return self

    def get_email(self):
        return self.__email

    def set_pager(self, pager):
        ValueChecker.is_string(pager)
        self.__pager = pager
        return self

    def get_pager(self):
        return self.__pager

    def set_phone(self, phone):
        ValueChecker.is_string(phone)
        self.__phone = phone
        return self

    def get_phone(self):
        return self.__phone

    def set_types(self, types):
        for type in types:
            if type not in self.__allowed_types:
                raise Exception('Type ' + type + ' is not allowed')
        self.__types = types
        return self

    def get_types(self):
        return self.__types

    def set_states(self, states):
        for state in states:
            if state not in self.__allowed_states:
                raise Exception('State ' + state + ' is not allowed')
        self.__states = states
        return self

    def get_states(self):
        return self.__states

    def add_group(self, group):

        if isinstance(group, UserGroup):
            self.__groups.append(group)

        elif isinstance(group, str):
            group = ConfigBuilder.get_usergroup(group)
            if None is group:
                raise Exception('UserGroup does not exist yet!')
            self.__groups.append(group)
        else:
            raise Exception('Can only add UserGroup or id of UserGroup!')

        return self

    def remove_group(self, group):

        if isinstance(group, UserGroup):
            self.__groups.remove(group)

        elif isinstance(group, str):
            group = ConfigBuilder.get_usergroup(group)
            self.__groups.remove(group)

        return self

    def get_groups(self):

        return self.__groups

    def add_var(self, key, value):

        ValueChecker.is_string(key)
        self.__vars.append((key, value))

        return self

    def set_enable_notifications(self, enable_notifications):
        ValueChecker.is_bool(enable_notifications)
        self.__enable_notifications = enable_notifications
        return self

    def get_enable_notifications(self):
        return self.__enable_notifications

    def validate(self):
        if None is self.__email:
            raise Exception('Email is required for User ' + self.get_id())

    def get_config(self):
        self.validate()

        config = 'object User "user_' + self.__id + '" {\n'
        config += ValueMapper.parse_var('vars.email_addresses', self.__email)
        config += ValueMapper.parse_var('pager', self.__pager)
        config += ValueMapper.parse_var('vars.phone', self.__phone)
        config += ValueMapper.parse_var('display_name', self.__display_name)
        config += ValueMapper.parse_var('enable_notifications', self.__enable_notifications)
        config += ValueMapper.parse_var('groups', self.__groups, value_prefix='usergroup_')
        config += ValueMapper.parse_var('states', self.__states)
        config += ValueMapper.parse_var('types', self.__types)

        for var in self.__vars:
            config += '  var.' + var[0] + ' = ' + ValueMapper.parse_value_for_var(var[1]) + '\n'
        config += '}\n'

        return config
