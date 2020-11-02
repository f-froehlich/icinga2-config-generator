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


class MailNotificationCommand(NotificationCommand):

    def __init__(self, id):
        NotificationCommand.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_notification_command(id)
        if None is command:
            command = MailNotificationCommand(id)
            ConfigBuilder.add_notification_command(id, command)

        return command

    def get_command_executable_host(self):
        return 'mail-host-notification.sh'

    def get_command_executable_service(self):
        return 'mail-service-notification.sh'

    def validate(self):
        pass

    def get_arguments_host(self):
        config = '{\n' + self.get_default_arguments_host() + """
   "-r" = {
      value = "$notification_useremail$"
      required = true
    }       
}"""
        config += self.get_default_vars_host()
        config += '  vars.notification_useremail = "$email$"\n'

        return config

    def get_arguments_service(self):
        config = '{\n' + self.get_default_arguments_service() + """
   "-r" = {
      value = "$notification_useremail$"
      required = true
    }       
}"""
        config += self.get_default_vars_service()
        config += '  vars.notification_useremail = "$email$"\n'

        return config
