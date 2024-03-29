#!/usr/bin/python3
# -*- coding: utf-8
import typing

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
from icinga2confgen.Commands.MonitoringPlugins.SPFCommand import SPFCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='CheckSPF')

class CheckSPF(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckSPF', 'monitoring_plugins_spf')
        self.__domain = None
        self.__expected = None
        self.__resolver = '1.1.1.1'
        self.__timeout = 10
        self.set_check_interval('15m')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('dns'))
        self.add_service_group(ServiceGroup.create('spf'))

    def set_timeout(self, timeout:int) -> T:
        self.__timeout = timeout
        return self

    def get_timeout(self) -> int:
        return self.__timeout

    def set_resolver(self, resolver: str) -> T:
        self.__resolver = resolver
        return self

    def get_resolver(self) -> str:
        return self.__resolver

    def set_expected(self, expected: str) -> T:
        self.__expected = expected
        return self

    def get_expected(self) -> typing.Union[str, None]:
        return self.__expected

    def set_domain(self, domain: str) -> T:
        self.__domain = domain
        return self

    def get_domain(self) -> typing.Union[str, None]:
        return self.__domain

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckSPF(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckSPF):
            raise Exception('Id must be for an instance of CheckSPF but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_spf'):
            SPFCommand.create('monitoring_plugins_spf')

        return check

    def validate(self):
        if None is self.__expected:
            raise Exception('You have to set expected SPF policy in ' + self.get_id())
        if None is self.__domain:
            raise Exception('You have to set a domain in ' + self.get_id())
