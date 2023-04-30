#!/usr/bin/python3
# -*- coding: utf-8
import typing

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.MonitoringPlugins.ExistingUsersCommand import ExistingUsersCommand
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

T = typing.TypeVar('T', bound='CheckExistingUsers')


class CheckExistingUsers(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckExistingUsers', 'monitoring_plugins_existing_users')
        self.__uid_min = None
        self.__uid_max = None
        self.__users = ["root"]
        self.__shell_filter = ["/bin/false", "/bin/sync", "/sbin/nologin", "/usr/sbin/nologin"]
        self.set_check_interval('15m')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('existing_user'))

    def set_uid_min(self, uid_min: typing.Union[int, None]) -> T:
        self.__uid_min = uid_min
        return self

    def get_uid_min(self) -> typing.Union[int, None]:
        return self.__uid_min

    def set_uid_max(self, uid_max: typing.Union[int, None]) -> T:
        self.__uid_max = uid_max
        return self

    def get_uid_max(self) -> typing.Union[int, None]:
        return self.__uid_max

    def append_existing_users(self, user: str) -> T:
        if user not in self.__users:
            self.__users.append(user)
        return self

    def remove_existing_users(self, user: str) -> T:
        if user in self.__users:
            self.__users.remove(user)
        return self

    def get_existing_users(self) -> typing.List[str]:
        return self.__users

    def append_shell_filter(self, shell:str) -> T:
        if shell not in self.__shell_filter:
            self.__shell_filter.append(shell)
        return self

    def remove_shell_filter(self, shell: str) -> T:
        if shell in self.__shell_filter:
            self.__shell_filter.remove(shell)
        return self

    def get_shell_filter(self) -> typing.List[str]:
        return self.__shell_filter

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckExistingUsers(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckExistingUsers):
            raise Exception('Id must be for an instance of CheckExistingUsers but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_existing_users'):
            ExistingUsersCommand.create('monitoring_plugins_existing_users')

        return check

    def validate(self):
        pass
