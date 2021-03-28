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
from icinga2confgen.Notification.TimePeriod import TimePeriod
from icinga2confgen.ValueMapper import ValueMapper

T = typing.TypeVar('T', bound='Dependency')


class Dependency:

    def __init__(self: T, id: str):
        self.__id = id
        self.__parent_host_name = None
        self.__disable_checks: bool = True
        self.__disable_notifications: bool = True
        self.__ignore_soft_states: bool = True
        self.__period: Union[TimePeriod, None] = None
        self.__states: List[str] = self.get_default_states()
        self.__allowed_states: List[str] = self.get_allowed_states()

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        raise Exception("You have to override create!")

    def get_id(self: T) -> str:
        return self.__id

    def get_allowed_states(self: T) -> List[str]:
        raise Exception("You have to override get_allowed_states!")

    def get_default_states(self: T) -> List[str]:
        raise Exception("You have to override get_default_states!")

    def validate(self: T):
        if None == self.__parent_host_name:
            raise Exception('You have to set a Server for the Dependency with id "' + self.__id + '"')

    def set_states(self: T, states: List[str]) -> T:
        for state in states:
            if state not in self.__allowed_states:
                raise Exception('State ' + state + ' is not allowed')
        self.__states = states
        return self

    def get_states(self: T) -> List[str]:
        return self.__states

    def set_disable_notifications(self: T, disable_notifications: bool) -> T:
        self.__disable_notifications = disable_notifications
        return self

    def get_disable_notifications(self: T) -> bool:
        return self.__disable_notifications

    def set_disable_checks(self: T, disable_checks: bool) -> T:
        self.__disable_checks = disable_checks
        return self

    def get_disable_checks(self: T) -> bool:
        return self.__disable_checks

    def set_ignore_soft_states(self: T, ignore_soft_states: bool) -> T:
        self.__ignore_soft_states = ignore_soft_states
        return self

    def get_ignore_soft_states(self: T) -> bool:
        return self.__ignore_soft_states

    def set_server(self: T, server) -> T:

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

    def get_server(self: T):
        return self.__parent_host_name

    def set_period(self: T, period: Union[TimePeriod, str]):

        if isinstance(period, str):
            period = ConfigBuilder.get_time_period(period)
            if None is period:
                raise Exception('TimePeriod does not exist yet!')
            self.__period = period
        elif isinstance(period, TimePeriod):
            self.__period = period
        else:
            raise Exception('Can only add TimePeriod or id of TimePeriod!')

        return self

    def get_period(self: T) -> Union[TimePeriod, None]:
        return self.__period

    def get_config(self: T) -> str:
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
