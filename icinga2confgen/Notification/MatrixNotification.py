#!/usr/bin/python3
# -*- coding: utf-8
from __future__ import annotations

from typing import List

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.UserGroup import UserGroup
from icinga2confgen.Notification.MatrixNotificationCommand import MatrixNotificationCommand
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


class MatrixNotification(Notification):

    def __init__(self, id: str):
        Notification.__init__(self, id)

    @staticmethod
    def create(id: str, force_create: bool = False) -> MatrixNotification:
        ValueChecker.validate_id(id)

        notification = None if force_create else ConfigBuilder.get_notification(id)
        if None is notification:
            notification = MatrixNotification(id)
            ConfigBuilder.add_notification(id, notification)

        return notification

    def get_command_config(self) -> MatrixNotificationCommand:
        return MatrixNotificationCommand.create('matrix')

    def user_config_function(self, user: User) -> List[str]:
        if 0 == len(user.get_matrix_users()):
            return []

        config = [
            ValueMapper.parse_var('vars.notification_matrix_users', user.get_matrix_users()) + '\n'
        ]
        return config

    def group_config_function(self, group: UserGroup) -> List[str]:
        if 0 == len(group.get_matrix_users()):
            return []

        config = [
            ValueMapper.parse_var('vars.notification_matrix_users', group.get_matrix_users()) + '\n'
        ]
        return config
