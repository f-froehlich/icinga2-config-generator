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
from typing import Union, List

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Dependency.Dependency import Dependency
from icinga2confgen.Downtimes.ScheduledDowntime import ScheduledDowntime
from icinga2confgen.Helpers.CustomVars import CustomVars
from icinga2confgen.Helpers.Nameable import Nameable
from icinga2confgen.Notification.Notification import Notification
from icinga2confgen.Servers.Zone import Zone
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper

T = typing.TypeVar('T', bound='Checkable')


class Checkable(Nameable, CustomVars):

    def __init__(self: T, is_check: bool = True):
        Nameable.__init__(self)
        CustomVars.__init__(self)
        self.__is_check = is_check
        self.__max_check_attempts = 3
        self.__check_interval = '1m'
        self.__retry_interval = '15s'
        self.__check_timeout = 30
        self.__enable_perfdata = True
        self.__notifications = []
        self.__downtimes: List[ScheduledDowntime] = []
        self.__dependencies = []
        self.__dns_zone = Zone.create('master')
        self.__override_zone = False
        self.__command_endpoint = None
        self.__override_endpoint = False
        self.__generated = False
        self.__use_negation: bool = False
        self.__negation_ok_status: Union[str, None] = None
        self.__negation_warning_status: Union[str, None] = None
        self.__negation_critical_status: Union[str, None] = None
        self.__negation_unknown_status: Union[str, None] = None
        self.__negation_substitute: Union[bool, None] = None
        self.__negation_timeout: Union[int, None] = None
        self.__allowed_negation_states = ['OK', 'WARNING', 'CRITICAL', 'UNKNOWN']

    def check_negation_status(self: T, status: Union[str, None]) -> T:
        if None is status:
            return self
        if status not in self.__allowed_negation_states:
            raise Exception('Negation status must be in {allowed} but {given} was given'.format(
                allowed=', '.join(self.__allowed_negation_states), given=status))
        return self

    def use_negation(self: T, enabled: bool) -> T:
        self.__use_negation = enabled
        return self

    def is_using_negation(self: T) -> bool:
        return self.__use_negation

    def use_negation_substitute(self: T, enabled: bool) -> T:
        self.__negation_substitute = enabled
        return self

    def is_using_negation_substitute(self: T) -> bool:
        return self.__negation_substitute

    def set_ok_status(self: T, status: Union[str, None]) -> T:
        self.check_negation_status(status)
        self.__negation_ok_status = status
        return self

    def get_ok_status(self: T) -> Union[str, None]:
        return self.__negation_ok_status

    def set_warning_status(self: T, status: Union[str, None]) -> T:
        self.check_negation_status(status)
        self.__negation_warning_status = status
        return self

    def get_warning_status(self: T) -> Union[str, None]:
        return self.__negation_warning_status

    def set_critical_status(self: T, status: Union[str, None]) -> T:
        self.check_negation_status(status)
        self.__negation_critical_status = status
        return self

    def get_critical_status(self: T) -> Union[str, None]:
        return self.__negation_critical_status

    def set_unknown_status(self: T, status: Union[str, None]) -> T:
        self.check_negation_status(status)
        self.__negation_unknown_status = status
        return self

    def get_unknown_status(self: T) -> Union[str, None]:
        return self.__negation_unknown_status

    def set_negation_timeout(self: T, timeout: Union[int, None]) -> T:
        self.__negation_timeout = timeout
        return self

    def get_negation_timeout(self: T) -> Union[int, None]:
        return self.__negation_timeout

    def set_max_check_attempts(self: T, max_check_attempts) -> T:
        ValueChecker.is_number(max_check_attempts)
        self.__max_check_attempts = max_check_attempts
        return self

    def get_max_check_attempts(self: T) -> int:
        return self.__max_check_attempts

    def set_generated(self: T, generated: bool) -> T:
        self.__generated = generated
        return self

    def is_generated(self: T) -> bool:
        return self.__generated

    def set_check_timeout(self: T, check_timeout: int) -> T:
        self.__check_timeout = check_timeout
        return self

    def get_check_timeout(self: T) -> int:
        return self.__check_timeout

    def set_check_interval(self: T, check_interval: str) -> T:
        self.__check_interval = check_interval
        return self

    def get_check_interval(self: T) -> str:
        return self.__check_interval

    def set_retry_interval(self: T, retry_interval: str) -> T:
        self.__retry_interval = retry_interval
        return self

    def get_retry_interval(self: T) -> str:
        return self.__retry_interval

    def set_enable_perfdata(self: T, enabled: bool) -> T:
        self.__enable_perfdata = enabled
        return self

    def get_enable_perfdata(self: T) -> bool:
        return self.__enable_perfdata

    def add_downtime(self: T, downtime: Union[ScheduledDowntime, str]) -> T:
        if isinstance(downtime, ScheduledDowntime):
            if downtime not in self.__downtimes:
                self.__downtimes.append(downtime)
        elif isinstance(downtime, str):
            downtime = ConfigBuilder.get_downtime(downtime)
            if None is downtime:
                raise Exception('Downtime does not exist yet!')
            if downtime not in self.__downtimes:
                self.__downtimes.append(downtime)
        else:
            raise Exception('Can only add Downtime or id of Downtime!')

        return self

    def remove_downtime(self: T, downtime: Union[ScheduledDowntime, str]) -> T:
        if isinstance(downtime, ScheduledDowntime):
            if downtime in self.__downtimes:
                self.__downtimes.remove(downtime)
        elif isinstance(downtime, str):
            downtime = ConfigBuilder.get_downtime(downtime)
            if downtime in self.__downtimes:
                self.__downtimes.remove(downtime)

        return self

    def get_downtimes(self: T) -> List[ScheduledDowntime]:
        return self.__downtimes

    def add_dependency(self: T, dependency: Union[Dependency, str]) -> T:
        if isinstance(dependency, Dependency):
            if dependency not in self.__dependencies:
                self.__dependencies.append(dependency)
        elif isinstance(dependency, str):
            dependency = ConfigBuilder.get_dependency(dependency)
            if None is dependency:
                raise Exception('Dependency does not exist yet!')
            if dependency not in self.__dependencies:
                self.__dependencies.append(dependency)
        else:
            raise Exception('Can only add Dependency or id of Dependency!')

        return self

    def remove_dependency(self: T, dependency: Union[Dependency, str]) -> T:
        if isinstance(dependency, Dependency):
            self.__dependencies.remove(dependency)
        elif isinstance(dependency, str):
            dependency = ConfigBuilder.get_dependency(dependency)
            self.__dependencies.remove(dependency)

        return self

    def get_dependencies(self: T) -> List[Dependency]:
        return self.__dependencies

    def add_notification(self: T, notification: Union[Notification, str]) -> T:
        if isinstance(notification, Notification):
            if notification not in self.__notifications:
                self.__notifications.append(notification)
        elif isinstance(notification, str):
            notification = ConfigBuilder.get_notification(notification)
            if None is notification:
                raise Exception('Notification does not exist yet!')
            if notification not in self.__notifications:
                self.__notifications.append(notification)
        else:
            raise Exception('Can only add Notification or id of Notification!')
        return self

    def remove_notification(self: T, notification: Union[Notification, str]) -> T:

        if isinstance(notification, Notification):
            if notification in self.__notifications:
                self.__notifications.remove(notification)

        elif isinstance(notification, str):
            notification = ConfigBuilder.get_notification(notification)
            if notification in self.__notifications:
                self.__notifications.remove(notification)

        return self

    def get_notifications(self: T) -> List[Notification]:
        return self.__notifications

    def set_zone(self: T, zone: Union[Zone, str]) -> T:
        if isinstance(zone, Zone):
            self.__dns_zone = zone
            self.__override_zone = True
        elif isinstance(zone, str):
            zone = ConfigBuilder.get_zone(zone)
            if None is zone:
                raise Exception('Zone does not exist yet!')
            self.__dns_zone = zone
            self.__override_zone = True
        else:
            raise Exception('Can only add Zone or id of Zone!')
        return self

    def get_zone(self: T) -> Union[Zone, None]:
        if self.__is_check and not self.__override_zone:
            return None

        return self.__dns_zone

    def set_endpoint(self: T, name: str) -> T:
        self.__override_endpoint = True
        self.__command_endpoint = name
        return self

    def get_endpoint(self: T) -> Union[str, None]:
        return self.__command_endpoint

    def get_config(self: T) -> str:

        config = Nameable.get_config(self)
        config += CustomVars.get_config(self)
        if not self.__is_check:
            config += ValueMapper.parse_var('vars.zone_name', self.__dns_zone)
        elif self.__override_zone:
            config += ValueMapper.parse_var('zone', self.__dns_zone)
        else:
            config += '  zone = host.vars.zone_name\n'

        if not self.__is_check:
            config += ValueMapper.parse_var('vars.endpoint_name', self.__command_endpoint)
        elif self.__override_endpoint:
            config += ValueMapper.parse_var('command_endpoint', self.__command_endpoint)
        else:
            config += '  command_endpoint = host.vars.endpoint_name\n'

        config += '  check_interval = ' + self.__check_interval + '\n'
        config += '  retry_interval = ' + self.__retry_interval + '\n'
        config += ValueMapper.parse_var('max_check_attempts', self.__max_check_attempts)
        config += ValueMapper.parse_var('enable_perfdata', self.__enable_perfdata)
        config += ValueMapper.parse_var('check_timeout', self.__check_timeout)
        config += ValueMapper.parse_var('vars.notification', self.__notifications, value_prefix='notification_')
        config += ValueMapper.parse_var('vars.downtime', self.__downtimes, value_prefix='downtime_')
        config += ValueMapper.parse_var('vars.dependencies', self.__dependencies, value_prefix='dependency_')
        if self.__use_negation:
            config += ValueMapper.parse_var('vars.negation_ok_status', self.__negation_ok_status)
            config += ValueMapper.parse_var('vars.negation_warning_status', self.__negation_warning_status)
            config += ValueMapper.parse_var('vars.negation_critical_status', self.__negation_critical_status)
            config += ValueMapper.parse_var('vars.negation_unknown_status', self.__negation_unknown_status)
            config += ValueMapper.parse_var('vars.negation_substitute', self.__negation_substitute)
            config += ValueMapper.parse_var('vars.negation_timeout', self.__negation_timeout)

        return config
