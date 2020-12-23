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
from icinga2confgen.Dependency.Dependency import Dependency
from icinga2confgen.Downtimes.ScheduledDowntime import ScheduledDowntime
from icinga2confgen.Helpers.Nameable import Nameable
from icinga2confgen.Notification.Notification import Notification
from icinga2confgen.Servers.Zone import Zone
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class Checkable(Nameable):

    def __init__(self, is_check=True):
        Nameable.__init__(self)
        self.__is_check = is_check
        self.__max_check_attempts = 3
        self.__check_interval = '1m'
        self.__retry_interval = '15s'
        self.__check_timeout = 30
        self.__enable_perfdata = True
        self.__notifications = []
        self.__downtimes = []
        self.__dependencies = []
        self.__dns_zone = Zone.create('master')
        self.__override_zone = False
        self.__command_endpoint = None
        self.__override_endpoint = False

    def set_max_check_attempts(self, max_check_attempts):
        ValueChecker.is_number(max_check_attempts)
        self.__max_check_attempts = max_check_attempts
        return self

    def get_max_check_attempts(self):
        return self.__max_check_attempts

    def set_check_timeout(self, check_timeout):
        ValueChecker.is_number(check_timeout)
        self.__check_timeout = check_timeout
        return self

    def get_check_timeout(self):
        return self.__check_timeout

    def set_check_interval(self, check_interval):
        ValueChecker.is_string(check_interval)
        self.__check_interval = check_interval
        return self

    def get_check_interval(self):
        return self.__check_interval

    def set_retry_interval(self, retry_interval):
        ValueChecker.is_string(retry_interval)
        self.__retry_interval = retry_interval
        return self

    def get_retry_interval(self):
        return self.__retry_interval

    def set_enable_perfdata(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__enable_perfdata = enabled
        return self

    def get_enable_perfdata(self):
        return self.__enable_perfdata

    def add_downtime(self, downtime):
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

    def remove_downtime(self, downtime):
        if isinstance(downtime, ScheduledDowntime):
            self.__downtimes.remove(downtime)
        elif isinstance(downtime, str):
            downtime = ConfigBuilder.get_downtime(downtime)
            self.__downtimes.remove(downtime)

        return self

    def get_downtimes(self):
        return self.__downtimes

    def add_dependency(self, dependency):
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

    def remove_dependency(self, dependency):
        if isinstance(dependency, Dependency):
            self.__dependencies.remove(dependency)
        elif isinstance(dependency, str):
            dependency = ConfigBuilder.get_dependency(dependency)
            self.__dependencies.remove(dependency)

        return self

    def get_dependencies(self):
        return self.__dependencies

    def add_notification(self, notification):
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

    def remove_notification(self, notification):

        if isinstance(notification, Notification):
            self.__notifications.remove(notification)

        elif isinstance(notification, str):
            notification = ConfigBuilder.get_notification(notification)
            self.__notifications.remove(notification)

        return self

    def get_notifications(self):
        return self.__notifications

    def set_zone(self, zone):
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

    def get_zone(self):
        if self.__is_check and not self.__override_zone:
            return None

        return self.__dns_zone

    def set_endpoint(self, name):
        ValueChecker.is_string(name)
        self.__override_endpoint = True
        self.__command_endpoint = name
        return self

    def get_endpoint(self):
        return self.__command_endpoint

    def get_config(self):

        config = Nameable.get_config(self)
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

        return config
