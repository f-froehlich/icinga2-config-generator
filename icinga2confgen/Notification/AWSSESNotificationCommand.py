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
from icinga2confgen.Notification.NotificationCommand import NotificationCommand
from icinga2confgen.ValueChecker import ValueChecker


class AWSSESNotificationCommand(NotificationCommand):

    def __init__(self, id: str):
        NotificationCommand.__init__(self, id)

    @staticmethod
    def create(id: str, force_create: bool = False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_notification_command(id)
        if None is command:
            command = AWSSESNotificationCommand(id)
            ConfigBuilder.add_notification_command(id, command)

        return command

    def get_command_executable_host(self) -> str:
        return 'aws_ses_notification_host.py'

    def get_command_executable_service(self) -> str:
        return 'aws_ses_notification_service.py'

    def validate(self):
        pass

    def get_aws_ses_args(self) -> str:
        return """
    "-k" = {
      value = "$notification_aws_ses_key_id$"
      required = true
    }
    "-S" = {
      value = "$notification_aws_ses_secret$"
      required = true
    }
    "-F" = {
      value = "$notification_aws_ses_sender$"
      required = true
    }
    "-R" = {
      value = "$notification_aws_ses_region$"
      set_if = {{ macro("$notification_aws_ses_region$") != false }}
    } 
    "--subject" = {
      value = "$notification_aws_ses_subject_template$"
      set_if = {{ macro("$notification_aws_ses_subject_template$") != false }}
    } 
    "--message-template-short" = {
      value = "$notification_aws_ses_message_template_short$"
      set_if = {{ macro("$notification_aws_ses_message_template_short$") != false }}
    } 
    "--message-template-additional" = {
      value = "$notification_aws_ses_message_template_additional$"
      set_if = {{ macro("$notification_aws_ses_message_template_additional$") != false }}
    } 
    "-r" = {
      value = "$notification_aws_ses_recipients$"
      set_if = {{ macro("$notification_aws_ses_recipients$") != false }}
      repeat_key = true
    }
"""

    def get_arguments_host(self) -> str:
        config = '{\n' + self.get_default_arguments_host() + self.get_aws_ses_args() + '}\n'
        config += self.get_default_vars_host()

        return config

    def get_arguments_service(self) -> str:
        config = '{\n' + self.get_default_arguments_service() + self.get_aws_ses_args() + '}\n'

        config += self.get_default_vars_service()

        return config
