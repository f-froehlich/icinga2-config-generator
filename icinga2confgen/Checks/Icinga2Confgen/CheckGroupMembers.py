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

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.Icinga2Confgen.GroupMembersCommand import GroupMembersCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckGroupMembers(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckGroupMembers', 'group_members')
        self.__group = 'sudo'
        self.__users = []
        self.set_check_interval('3h')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('group_members'))

    def set_group(self, group):
        ValueChecker.is_string(group)
        self.__group = group
        return self

    def get_group(self):
        return self.__group

    def append_user(self, user):
        ValueChecker.is_string(user)
        self.__users.append(user)
        return self

    def remove_user(self, user):
        self.__users.remove(user)
        return self

    def get_user(self):
        return self.__users

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckGroupMembers(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('group_members'):
            GroupMembersCommand.create('group_members')

        return check

    def validate(self):
        pass
