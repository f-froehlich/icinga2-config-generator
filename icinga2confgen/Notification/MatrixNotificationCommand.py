#!/usr/bin/python3
# -*- coding: utf-8

#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, notifications, checks, ... in python
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


class MatrixNotificationCommand(NotificationCommand):

    def __init__(self, id: str):
        NotificationCommand.__init__(self, id)

    @staticmethod
    def create(id: str, force_create: bool = False) -> MatrixNotificationCommand:
        ValueChecker.validate_id(id)
        notification = None if force_create else ConfigBuilder.get_notification_command(id)
        if None is notification:
            notification = MatrixNotificationCommand(id)
            ConfigBuilder.add_notification_command(id, notification)

        return notification

    def get_command_executable_host(self) -> str:
        return 'matrix_notification_host.py'

    def get_command_executable_service(self) -> str:
        return 'matrix_notification_service.py'

    def validate(self):
        pass

    def get_matrix_args(self) -> str:
        return """
    "--user" = {
      value = "$notification_matrix_users$"
      repeat_key = true
    }    
    "--header" = {
      value = "$notification_matrix_header$"
      set_if = {{ macro("$notification_matrix_header$") != false }}
      repeat_key = true
    }
    "--uri" = {
      value = "$notification_matrix_uri$"
      set_if = {{ macro("$notification_matrix_uri$") != false }}
    }
    "--domain" = {
      value = "$notification_matrix_domain$"
      set_if = {{ macro("$notification_matrix_domain$") != false }}
    }
    "--port" = {
      value = "$notification_matrix_port$"
      set_if = {{ macro("$notification_matrix_port$") != false }}
    }
    "--ssl" = {
      set_if = "$notification_matrix_ssl$"
    }
    "--client-cert" = {
      value = "$notification_matrix_client_cert$"
      set_if = {{ macro("$notification_matrix_client_cert$") != false }}
    }
    "--client-key" = {
      value = "$notification_matrix_client_key$"
      set_if = {{ macro("$notification_matrix_client_key$") != false }}
    }
    "--timeout" = {
      value = "$notification_matrix_timeout$"
      set_if = {{ macro("$notification_matrix_timeout$") != false }}
    }
    "--message-template-short" = {
      value = "$notification_matrix_message_template_short$"
      set_if = {{ macro("$notification_matrix_message_template_short$") != false }}
    } 
    "--message-template-additional" = {
      value = "$notification_matrix_message_template_additional$"
      set_if = {{ macro("$notification_matrix_message_template_additional$") != false }}
    } 
"""

    def get_arguments_host(self) -> str:
        config = '{\n' + self.get_default_arguments_host() + self.get_matrix_args() + '}\n'
        config += self.get_default_vars_host()

        return config

    def get_arguments_service(self) -> str:
        config = '{\n' + self.get_default_arguments_service() + self.get_matrix_args() + '}\n'

        config += self.get_default_vars_service()

        return config
