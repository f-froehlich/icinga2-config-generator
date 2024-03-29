#!/usr/bin/python3
# -*- coding: utf-8
import typing

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.NagiosPlugins.BreezeCommand import BreezeCommand
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

T = typing.TypeVar('T', bound='CheckBreeze')


class CheckBreeze(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckBreeze', 'nagios_plugins_breeze')
        self.__host = None
        self.__warning = None
        self.__critical = None
        self.__community = None
        self.add_service_group(ServiceGroup.create('breeze'))

    def set_host(self, host: str) -> T:
        self.__host = host
        return self

    def get_host(self) -> typing.Union[str, None]:
        return self.__host

    def set_warning(self, warning: str) -> T:
        self.__warning = warning
        return self

    def get_warning(self) -> typing.Union[str, None]:
        return self.__warning

    def set_critical(self, critical: str) -> T:
        self.__critical = critical
        return self

    def get_critical(self) -> typing.Union[str, None]:
        return self.__critical

    def set_community(self, community: typing.Union[str, None]) -> T:
        self.__community = community
        return self

    def get_community(self) -> typing.Union[str, None]:
        return self.__community

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckBreeze(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckBreeze):
            raise Exception('Id must be for an instance of CheckBreeze but other instance is returned')

        if None is ConfigBuilder.get_command('nagios_plugins_breeze'):
            BreezeCommand.create('nagios_plugins_breeze')

        return check

    def validate(self):
        if None is self.__host:
            raise Exception('You have to specify a host for ' + self.get_id())
        if None is self.__warning:
            raise Exception('You have to specify warning for ' + self.get_id())
        if None is self.__critical:
            raise Exception('You have to specify critical for ' + self.get_id())
