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
from icinga2confgen.Commands.Other.SynologyStatusCommand import SynologyStatusCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckSynologyStatus(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckSynologyStatus', 'other_synology_status')
        self.__host: Union[str, None] = None
        self.__user: Union[str, None] = None
        self.__password: Union[str, None] = None
        self.__warning_temp: Union[int, None] = None
        self.__critical_temp: Union[int, None] = None
        self.__warning_storage: Union[int, None] = None
        self.__critical_storage: Union[int, None] = None
        self.__v2: bool = False
        self.__ignore_update: bool = False
        self.__ups: bool = False

        self.add_service_group(ServiceGroup.create('synology'))

    def set_host(self, host: str) -> CheckSynologyStatus:
        self.__host = host
        return self

    def get_host(self) -> Union[str, None]:
        return self.__host

    def set_user(self, user: str) -> CheckSynologyStatus:
        self.__user = user
        return self

    def get_user(self) -> Union[str, None]:
        return self.__user

    def set_password(self, password: str) -> CheckSynologyStatus:
        self.__password = password
        return self

    def get_password(self) -> Union[str, None]:
        return self.__password

    def set_warning_temp(self, warning_temp: int) -> CheckSynologyStatus:
        self.__warning_temp = warning_temp
        return self

    def get_warning_temp(self) -> Union[int, None]:
        return self.__warning_temp

    def set_critical_temp(self, critical_temp: int) -> CheckSynologyStatus:
        self.__critical_temp = critical_temp
        return self

    def get_critical_temp(self) -> Union[int, None]:
        return self.__critical_temp

    def set_warning_storage(self, warning_storage: int) -> CheckSynologyStatus:
        self.__warning_storage = warning_storage
        return self

    def get_warning_storage(self) -> Union[int, None]:
        return self.__warning_storage

    def set_critical_storage(self, critical_storage: int) -> CheckSynologyStatus:
        self.__critical_storage = critical_storage
        return self

    def get_critical_storage(self) -> Union[int, None]:
        return self.__critical_storage

    def set_v2(self, enabled: bool) -> CheckSynologyStatus:
        self.__v2 = enabled
        return self

    def get_v2(self) -> bool:
        return self.__v2

    def set_ignore_update(self, enabled: bool) -> CheckSynologyStatus:
        self.__ignore_update = enabled
        return self

    def get_ignore_update(self) -> bool:
        return self.__ignore_update

    def set_ups(self, enabled: bool) -> CheckSynologyStatus:
        self.__ups = enabled
        return self

    def get_ups(self) -> bool:
        return self.__ups

    def validate(self):

        if None is self.__host:
            raise Exception('Host must be set')

        if not self.__v2:
            if None is self.__user:
                raise Exception('User must be set')

            if None is self.__password:
                raise Exception('Password must be set')

    @staticmethod
    def create(id: str, force_create: bool = False) -> CheckSynologyStatus:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckSynologyStatus(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckSynologyStatus):
            raise Exception('Id must be for an instance of CheckSynologyStatus but other instance is returned')

        if None is ConfigBuilder.get_command('other_synology_status'):
            SynologyStatusCommand.create('other_synology_status')

        return check
