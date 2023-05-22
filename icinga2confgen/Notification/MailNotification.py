#!/usr/bin/python3
# -*- coding: utf-8
from __future__ import annotations

from ctypes import Union
from typing import List

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.UserGroup import UserGroup
from icinga2confgen.Notification.MailNotificationCommand import MailNotificationCommand
from icinga2confgen.Notification.Notification import Notification
from icinga2confgen.User.User import User
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


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

class MailNotification(Notification):

    def __init__(self, id: str):
        Notification.__init__(self, id)
        self.__user = None
        self.__secret = None
        self.__sender = None
        self.__host = "localhost"
        self.__port = 25
        self.__use_ssl = False
        self.__use_starttls = False

        self.__subject_template = None
        self.__message_template_short = None
        self.__message_template_additional = None

    def set_user(self, user: Union[str, None]) -> MailNotification:
        self.__user = user

        return self

    def get_user(self) -> Union[str, None]:
        return self.__user

    def set_secret(self, secret: Union[str, None]) -> MailNotification:
        self.__secret = secret

        return self

    def get_secret(self) -> Union[str, None]:
        return self.__secret

    def set_sender(self, sender: Union[str, None]) -> MailNotification:
        self.__sender = sender

        return self

    def get_sender(self):
        return self.__sender

    def set_host(self, host: str) -> MailNotification:
        self.__host = host

        return self

    def get_host(self) -> str:
        return self.__host

    def set_port(self, port: int) -> MailNotification:
        self.__port = port

        return self

    def get_port(self) -> int:
        return self.__port

    def set_use_ssl(self, use_ssl: bool) -> MailNotification:
        self.__use_ssl = use_ssl

        return self

    def get_use_ssl(self) -> bool:
        return self.__use_ssl

    def set_use_starttls(self, use_starttls: bool) -> MailNotification:
        self.__use_starttls = use_starttls

        return self

    def get_use_starttls(self) -> bool:
        return self.__use_starttls

    def set_subject_template(self, subject_template: Union[str, None]) -> MailNotification:
        self.__subject_template = subject_template

        return self

    def get_subject_template(self) -> Union[str, None]:
        return self.__subject_template

    def set_message_template_short(self, message_template_short: Union[str, None]) -> MailNotification:
        self.__message_template_short = message_template_short

        return self

    def get_message_template_short(self) -> Union[str, None]:
        return self.__message_template_short

    def set_message_template_additional(self, message_template_additional: Union[str, None]) -> MailNotification:
        self.__message_template_additional = message_template_additional

        return self

    def get_message_template_additional(self) -> Union[str, None]:
        return self.__message_template_additional

    @staticmethod
    def create(id: str, force_create: bool = False) -> MailNotification:
        ValueChecker.validate_id(id)

        notification = None if force_create else ConfigBuilder.get_notification(id)
        if None is notification:
            notification = MailNotification(id)
            ConfigBuilder.add_notification(id, notification)

        return notification

    def get_command_config(self) -> MailNotificationCommand:
        return MailNotificationCommand.create('mail_smtp')

    def mail_smtp_config_function(self, emails: List[str]) -> List[str]:

        if None is not self.__user and None is self.__secret:
            raise Exception('If user is set you have to set secret as well in ' + self.get_id())
        if None is self.__user and None is not self.__secret:
            raise Exception('If secret is set you have to set user as well in ' + self.get_id())

        if None is self.__sender:
            raise Exception('Sender not set in ' + self.get_id())

        config = [
            ValueMapper.parse_var('vars.notification_mail_smtp_recipients', emails) + '\n' +
            ValueMapper.parse_var('vars.notification_mail_smtp_user', self.__user) + '\n' +
            ValueMapper.parse_var('vars.notification_mail_smtp_secret', self.__secret) + '\n' +
            ValueMapper.parse_var('vars.notification_mail_smtp_sender', self.__sender) + '\n' +
            ValueMapper.parse_var('vars.notification_mail_smtp_host', self.__host) + '\n' +
            ValueMapper.parse_var('vars.notification_mail_smtp_port', self.__port) + '\n' +
            ValueMapper.parse_var('vars.notification_mail_smtp_port', self.__port) + '\n' +
            ValueMapper.parse_var('vars.notification_mail_smtp_use_ssl', self.__use_ssl) + '\n' +
            ValueMapper.parse_var('vars.notification_mail_smtp_use_starttls', self.__use_starttls) + '\n' +
            ValueMapper.parse_var('vars.notification_mail_smtp_subject_template', self.__subject_template) + '\n' +
            ValueMapper.parse_var('vars.notification_mail_smtp_message_template_short',
                                  self.__message_template_short) + '\n' +
            ValueMapper.parse_var('vars.notification_mail_smtp_message_template_additional',
                                  self.__message_template_additional) + '\n'
        ]
        return config

    def user_config_function(self, user: User) -> List[str]:
        if 0 == len(user.get_email()):
            return []

        return self.mail_smtp_config_function(user.get_email())

    def group_config_function(self, group: UserGroup) -> List[str]:
        if 0 == len(group.get_email()):
            return []

        return self.mail_smtp_config_function(group.get_email())
