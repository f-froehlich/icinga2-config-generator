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
from icinga2confgen.Notification.MailNotificationCommand import MailNotificationCommand
from icinga2confgen.Notification.NotificationTemplate import NotificationTemplate
from icinga2confgen.Notification.ServiceNotification import ServiceNotification
from icinga2confgen.ValueChecker import ValueChecker


class MailServiceNotification(ServiceNotification):

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)

        notification = None if force_create else ConfigBuilder.get_notification(id)
        if None is notification:
            notification = MailServiceNotification(id)
            ConfigBuilder.add_notification(id, notification)

        return notification

    def get_config(self):
        config = NotificationTemplate.get_config(self)
        config += self.apply_for_all_emails('Service')

        return config

    def get_command_config(self):
        return MailNotificationCommand.create('mail')
