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
from icinga2confgen.Commands.Icinga2Confgen.ExistingUsersCommand import ExistingUsersCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckExistingUsers(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckExistingUsers', 'existing_users')
        self.__uid_min = None
        self.__uid_max = None
        self.__users = ["root"]
        self.__shell_filter = ["/bin/false", "/bin/sync", "/sbin/nologin", "/usr/sbin/nologin"]
        self.set_check_interval('3h')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('existing_user'))

    def set_uid_min(self, uid_min):
        ValueChecker.is_string(uid_min)
        self.__uid_min = uid_min
        return self

    def get_uid_min(self):
        return self.__uid_min

    def set_uid_max(self, uid_max):
        ValueChecker.is_string(uid_max)
        self.__uid_max = uid_max
        return self

    def get_uid_max(self):
        return self.__uid_max

    def append_existing_users(self, user):
        ValueChecker.is_string(user)
        self.__users.append(user)
        return self

    def remove_existing_users(self, user):
        self.__users.remove(user)
        return self

    def get_existing_users(self):
        return self.__users

    def append_shell_filter(self, shell):
        ValueChecker.is_string(shell)
        self.__shell_filter.append(shell)
        return self

    def remove_shell_filter(self, shell):
        self.__shell_filter.remove(shell)
        return self

    def get_shell_filter(self):
        return self.__shell_filter

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckExistingUsers(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('existing_users'):
            ExistingUsersCommand.create('existing_users')

        return check

    def validate(self):
        pass
