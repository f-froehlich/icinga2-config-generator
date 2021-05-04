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

from typing import Union

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.ClaudioKuenzler.StorcenterCommand import StorcenterCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckStorcenter(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckStorcenter', 'claudio_kuenzler_storcenter')
        self.__host: Union[str, None] = None
        self.__user: Union[str, None] = None
        self.__password: Union[str, None] = None

        self.__type: Union[str, None] = None
        self.__warning: Union[int, None] = None
        self.__critical: Union[int, None] = None

        self.add_service_group(ServiceGroup.create('storcenter'))

    def set_host(self, host: str) -> CheckStorcenter:
        self.__host = host
        return self

    def get_host(self) -> Union[str, None]:
        return self.__host

    def set_user(self, user: str) -> CheckStorcenter:
        self.__user = user
        return self

    def get_user(self) -> Union[str, None]:
        return self.__user

    def set_password(self, password: str) -> CheckStorcenter:
        self.__password = password
        return self

    def get_password(self) -> Union[str, None]:
        return self.__password

    def set_type(self, type: str) -> CheckStorcenter:
        types = ['disk', 'raid', 'cpu', 'mem', 'info']
        if type not in types:
            raise Exception('Type must be in ' + ', '.join(types))

        self.__type = type
        return self

    def get_type(self) -> Union[str, None]:
        return self.__type

    def set_warning(self, warning: int) -> CheckStorcenter:
        self.__warning = warning
        return self

    def get_warning(self) -> Union[int, None]:
        return self.__warning

    def set_critical(self, critical: int) -> CheckStorcenter:
        self.__critical = critical
        return self

    def get_critical(self) -> Union[int, None]:
        return self.__critical

    def validate(self):

        if None is self.__host:
            raise Exception('Host must be set')

        if None is self.__user:
            raise Exception('User must be set')

        if None is self.__password:
            raise Exception('Password must be set')

        if None is self.__type:
            raise Exception('Type must be set')

    @staticmethod
    def create(id: str, force_create: bool = False) -> CheckStorcenter:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckStorcenter(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckStorcenter):
            raise Exception('Id must be for an instance of CheckStorecnter but other instance is returned')

        if None is ConfigBuilder.get_command('claudio_kuenzler_storcenter'):
            StorcenterCommand.create('claudio_kuenzler_storcenter')

        return check
