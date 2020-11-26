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
from icinga2confgen.ValueMapper import ValueMapper


class Dependency:

    def __init__(self, id):
        self.__id = id
        self.__parent_host_name = None
        self.__disable_checks = True
        self.__disable_notifications = True
        self.__ignore_soft_states = True
        self.__period = None
        self.__states = self.get_default_states()
        self.__allowed_states = self.get_allowed_states()

    @staticmethod
    def create(id, force_create=False):
        raise Exception("You have to override create!")

    def get_id(self):
        return self.__id

    def get_allowed_states(self):
        raise Exception("You have to override get_allowed_states!")

    def get_default_states(self):
        raise Exception("You have to override get_default_states!")

    def validate(self):
        if None == self.__parent_host_name:
            raise Exception('You have to set a Server for the Dependency with id "' + self.__id + '"')

    def set_states(self, states):
        for state in states:
            if state not in self.__allowed_states:
                raise Exception('State ' + state + ' is not allowed')
        self.__states = states
        return self

    def get_states(self):
        return self.__states

    def set_disable_notifications(self, disable_notifications):
        ValueChecker.is_bool(disable_notifications)
        self.__disable_notifications = disable_notifications
        return self

    def get_disable_notifications(self):
        return self.__disable_notifications

    def set_disable_checks(self, disable_checks):
        ValueChecker.is_bool(disable_checks)
        self.__disable_checks = disable_checks
        return self

    def get_disable_checks(self):
        return self.__disable_checks

    def set_ignore_soft_states(self, ignore_soft_states):
        ValueChecker.is_bool(ignore_soft_states)
        self.__ignore_soft_states = ignore_soft_states
        return self

    def get_ignore_soft_states(self):
        return self.__ignore_soft_states

    def set_server(self, server):

        if isinstance(server, str):
            server = ConfigBuilder.get_server(server)
            if None is server:
                raise Exception('Server does not exist yet!')
            self.__parent_host_name = server
        elif callable(getattr(server, 'get_id', None)):
            return self.set_server(server.get_id())

        else:
            raise Exception('Can only add Server or id of Server!')

        return self

    def get_server(self):
        return self.__parent_host_name

    def set_period(self, period):

        if isinstance(period, str):
            period = ConfigBuilder.get_time_period(period)
            if None is period:
                raise Exception('TimePeriod does not exist yet!')
            self.__period = period
        elif callable(getattr(period, 'get_id', None)):
            return self.set_period(period.get_id())
        else:
            raise Exception('Can only add TimePeriod or id of TimePeriod!')

        return self

    def get_period(self):
        return self.__period

    def get_config(self):
        self.validate()

        config = 'template Dependency "dependency_' + self.__id + '" {\n'
        config += ValueMapper.parse_var('parent_host_name', self.__parent_host_name)
        config += ValueMapper.parse_var('disable_checks', self.__disable_checks)
        config += ValueMapper.parse_var('disable_notifications', self.__disable_notifications)
        config += ValueMapper.parse_var('ignore_soft_states', self.__ignore_soft_states)
        config += ValueMapper.parse_var('period', self.__period, value_prefix='time_period_')
        config += ValueMapper.parse_var('states', self.__states)
        config += '}\n'

        return config
