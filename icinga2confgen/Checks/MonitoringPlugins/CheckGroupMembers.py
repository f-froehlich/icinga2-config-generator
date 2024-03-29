#!/usr/bin/python3
# -*- coding: utf-8
import typing

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.MonitoringPlugins.GroupMembersCommand import GroupMembersCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

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

T = typing.TypeVar('T', bound='CheckGroupMembers')


class CheckGroupMembers(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckGroupMembers', 'monitoring_plugins_group_members')
        self.__group = 'sudo'
        self.__users = []
        self.set_check_interval('15m')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('group_members'))

    def set_group(self, group: str) -> T:
        self.__group = group
        return self

    def get_group(self) -> str:
        return self.__group

    def append_user(self, user: str) -> T:
        if user not in self.__users:
            self.__users.append(user)
        return self

    def remove_user(self, user: str) -> T:
        if user in self.__users:
            self.__users.remove(user)
        return self

    def get_user(self) -> typing.List[str]:
        return self.__users

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckGroupMembers(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckGroupMembers):
            raise Exception('Id must be for an instance of CheckGroupMembers but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_group_members'):
            GroupMembersCommand.create('monitoring_plugins_group_members')

        return check

    def validate(self):
        pass
