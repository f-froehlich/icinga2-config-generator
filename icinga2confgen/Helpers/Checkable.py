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
from icinga2confgen.Downtimes.ScheduledDowntime import ScheduledDowntime
from icinga2confgen.Helpers.Namable import Nameable
from icinga2confgen.Notification.Notification import Notification
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class Checkable(Nameable):

    def __init__(self):
        Nameable.__init__(self)
        self.__max_check_attempts = 3
        self.__check_interval = '1m'
        self.__retry_interval = '15s'
        self.__enable_perfdata = True
        self.__notifications = []
        self.__downtimes = []

    def set_max_check_attempts(self, max_check_attempts):
        ValueChecker.is_number(max_check_attempts)
        self.__max_check_attempts = max_check_attempts
        return self

    def get_max_check_attempts(self):
        return self.__max_check_attempts

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

    def set_enable_perfdata(self, enable_perfdata):
        ValueChecker.is_bool(enable_perfdata)
        self.__enable_perfdata = enable_perfdata
        return self

    def get_enable_perfdata(self):
        return self.__enable_perfdata

    def add_downtime(self, downtime):
        if isinstance(downtime, ScheduledDowntime):
            self.__downtimes.append(downtime)
        elif isinstance(downtime, str):
            downtime = ConfigBuilder.get_downtime(downtime)
            if None is downtime:
                raise Exception('Downtime does not exist yet!')
            self.__downtimes.append(downtime)
        else:
            raise Exception('Can only add Downtime or id of Downtime!')

        return self

    def remove_downtime(self, downtime):
        if isinstance(downtime, ScheduledDowntime):
            self.__downtimes.remove(downtime.get_id())
        elif isinstance(downtime, str):
            self.__downtimes.remove('downtime_' + downtime)

        return self

    def add_notification(self, notification):
        if isinstance(notification, Notification):
            self.__notifications.append(notification)
        elif isinstance(notification, str):
            notification = ConfigBuilder.get_notification(notification)
            if None is notification:
                raise Exception('Notification does not exist yet!')

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

    def get_config(self):
        config = Nameable.get_config(self)
        config += '  check_interval = ' + self.__check_interval + '\n'
        config += '  retry_interval = ' + self.__retry_interval + '\n'
        config += ValueMapper.parse_var('max_check_attempts', self.__max_check_attempts)
        config += ValueMapper.parse_var('enable_perfdata', self.__enable_perfdata)
        config += ValueMapper.parse_var('vars.notification', self.__notifications, value_prefix='notification_')
        config += ValueMapper.parse_var('vars.downtime', self.__downtimes, value_prefix='downtime_')

        return config
