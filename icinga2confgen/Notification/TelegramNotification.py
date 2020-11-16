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
from icinga2confgen.Notification.Notification import Notification
from icinga2confgen.Notification.TelegramNotificationCommand import TelegramNotificationCommand
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class TelegramNotification(Notification):

    def __init__(self, id):
        Notification.__init__(self, id)
        self.__api_token = None

    def set_api_token(self, token):
        ValueChecker.is_string(token)
        self.__api_token = token

        return self

    def get_api_token(self):
        return self.__api_token

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)

        notification = None if force_create else ConfigBuilder.get_notification(id)
        if None is notification:
            notification = TelegramNotification(id)
            ConfigBuilder.add_notification(id, notification)

        return notification

    def get_command_config(self):
        return TelegramNotificationCommand.create('telegram')

    def user_config_function(self, user):
        if 0 == len(user.get_telegram_id()):
            return []

        if None is self.__api_token:
            raise Exception('Telegram API token not set in ' + self.get_id())
        config = [
            ValueMapper.parse_var('vars.notification_telegram_users', user.get_telegram_id()) + '\n' +
            ValueMapper.parse_var('vars.notification_telegram_token', self.__api_token) + '\n'
        ]
        return config

    def group_config_function(self, group):
        if 0 == len(group.get_telegram_id()):
            return []

        if None is self.__api_token:
            raise Exception('Telegram API token not set in ' + self.get_id())
        config = [
            ValueMapper.parse_var('vars.notification_telegram_groups', group.get_telegram_id()) + '\n' +
            ValueMapper.parse_var('vars.notification_telegram_token', self.__api_token) + '\n'
        ]
        return config
