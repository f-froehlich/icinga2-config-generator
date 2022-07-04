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
from icinga2confgen.Notification.AWSSESNotificationCommand import AWSSESNotificationCommand
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class AWSSESNotification(Notification):

    def __init__(self, id: str):
        Notification.__init__(self, id)
        self.__key_id = None
        self.__secret = None
        self.__sender = None
        self.__region = None
        self.__subject_template = None
        self.__message_template_short = None
        self.__message_template_additional = None

    def set_key_id(self, key_id):
        ValueChecker.is_string(key_id)
        self.__key_id = key_id

        return self

    def get_key_id(self):
        return self.__key_id

    def set_secret(self, secret):
        ValueChecker.is_string(secret)
        self.__secret = secret

        return self

    def get_secret(self):
        return self.__secret

    def set_sender(self, sender):
        ValueChecker.is_string(sender)
        self.__sender = sender

        return self

    def get_sender(self):
        return self.__sender

    def set_region(self, region):
        ValueChecker.is_string(region)
        self.__region = region

        return self

    def get_region(self):
        return self.__region

    def set_subject_template(self, subject_template):
        ValueChecker.is_string(subject_template)
        self.__subject_template = subject_template

        return self

    def get_subject_template(self):
        return self.__subject_template

    def set_message_template_short(self, message_template_short):
        ValueChecker.is_string(message_template_short)
        self.__message_template_short = message_template_short

        return self

    def get_message_template_short(self):
        return self.__message_template_short

    def set_message_template_additional(self, message_template_additional):
        ValueChecker.is_string(message_template_additional)
        self.__message_template_additional = message_template_additional

        return self

    def get_message_template_additional(self):
        return self.__message_template_additional

    @staticmethod
    def create(id: str, force_create: bool = False):
        ValueChecker.validate_id(id)

        notification = None if force_create else ConfigBuilder.get_notification(id)
        if None is notification:
            notification = AWSSESNotification(id)
            ConfigBuilder.add_notification(id, notification)

        return notification

    def get_command_config(self):
        return AWSSESNotificationCommand.create('aws_ses')

    def aws_ses_config_function(self, emails):

        if None is self.__key_id:
            raise Exception('AWS SES key id not set in ' + self.get_id())

        if None is self.__secret:
            raise Exception('AWS SES key secret not set in ' + self.get_id())
        if None is self.__sender:
            raise Exception('AWS SES sender not set in ' + self.get_id())

        config = [
            ValueMapper.parse_var('vars.notification_aws_ses_recipients', emails) + '\n' +
            ValueMapper.parse_var('vars.notification_aws_ses_key_id', self.__key_id) + '\n' +
            ValueMapper.parse_var('vars.notification_aws_ses_secret', self.__secret) + '\n' +
            ValueMapper.parse_var('vars.notification_aws_ses_sender', self.__sender) + '\n' +
            ValueMapper.parse_var('vars.notification_aws_ses_region', self.__region) + '\n' +
            ValueMapper.parse_var('vars.notification_aws_ses_subject_template', self.__subject_template) + '\n' +
            ValueMapper.parse_var('vars.notification_aws_ses_message_template_short',
                                  self.__message_template_short) + '\n' +
            ValueMapper.parse_var('vars.notification_aws_ses_message_template_additional',
                                  self.__message_template_additional) + '\n'
        ]
        return config

    def user_config_function(self, user):
        if 0 == len(user.get_email()):
            return []

        return self.aws_ses_config_function(user.get_email())

    def group_config_function(self, group):
        if 0 == len(group.get_email()):
            return []

        return self.aws_ses_config_function(group.get_email())
