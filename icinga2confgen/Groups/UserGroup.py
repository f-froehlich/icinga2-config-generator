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

import typing

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.Group import Group
from icinga2confgen.Notification.NotificationFunctions import NotificationFunctions
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='UserGroup')


class UserGroup(Group, NotificationFunctions):

    def __init__(self: T, id: str):
        Group.__init__(self, id, 'user')
        NotificationFunctions.__init__(self)

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        usergroup = None if force_create else ConfigBuilder.get_usergroup(id)
        if None is usergroup:
            usergroup = UserGroup(id)
            ConfigBuilder.add_usergroup(id, usergroup)

        return usergroup

    def get_config(self: T) -> str:
        config = Group.get_config(self)
        config += 'object User "user_group_notification_sender_' + self.get_id() + '" {\n'
        config += '  display_name = "Notification sender of group ' + self.get_display_name() + '"\n'
        config += NotificationFunctions.get_config(self)
        config += '}\n'

        return config
