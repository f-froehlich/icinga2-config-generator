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
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Notification.NotificationCommand import NotificationCommand
from icinga2confgen.ValueChecker import ValueChecker


class MailNotificationCommand(NotificationCommand):

    def __init__(self, id: str):
        NotificationCommand.__init__(self, id)

    @staticmethod
    def create(id: str, force_create: bool = False) -> MailNotificationCommand:
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_notification_command(id)
        if None is command:
            command = MailNotificationCommand(id)
            ConfigBuilder.add_notification_command(id, command)

        return command

    def get_command_executable_host(self) -> str:
        return 'mail_smtp_notification_host.py'

    def get_command_executable_service(self) -> str:
        return 'mail_smtp_notification_service.py'

    def validate(self):
        pass

    def get_mail_smtp_args(self) -> str:
        return """
    "-U" = {
      value = "$notification_mail_smtp_user$"
      set_if = {{ macro("$notification_mail_smtp_user$") != false }}
    }
    "-S" = {
      value = "$notification_mail_smtp_secret$"
      set_if = {{ macro("$notification_mail_smtp_secret$") != false }}
    }
    "-H" = {
      value = "$notification_mail_smtp_host$"
      required = true
    }
    "-p" = {
      value = "$notification_mail_smtp_port$"
      required = true
    }
    "--use-ssl" = {
      set_if = "$notification_mail_smtp_use_ssl$"
    }
    "--use-starttls" = {
      set_if = "$notification_mail_smtp_use_starttls$"
    }
    "-F" = {
      value = "$notification_mail_smtp_sender$"
      required = true
    }
    "--subject" = {
      value = "$notification_mail_smtp_subject_template$"
      set_if = {{ macro("$notification_mail_smtp_subject_template$") != false }}
    } 
    "--message-template-short" = {
      value = "$notification_mail_smtp_message_template_short$"
      set_if = {{ macro("$notification_mail_smtp_message_template_short$") != false }}
    } 
    "--message-template-additional" = {
      value = "$notification_mail_smtp_message_template_additional$"
      set_if = {{ macro("$notification_mail_smtp_message_template_additional$") != false }}
    } 
    "-r" = {
      value = "$notification_mail_smtp_recipients$"
      set_if = {{ macro("$notification_mail_smtp_recipients$") != false }}
      repeat_key = true
    }
"""

    def get_arguments_host(self) -> str:
        config = '{\n' + self.get_default_arguments_host() + self.get_mail_smtp_args() + '}\n'
        config += self.get_default_vars_host()

        return config

    def get_arguments_service(self) -> str:
        config = '{\n' + self.get_default_arguments_service() + self.get_mail_smtp_args() + '}\n'

        config += self.get_default_vars_service()

        return config
