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
from ctypes import Union

from icinga2confgen.Checks.MonitoringPlugins.SNMP.CheckSNMP import CheckSNMP
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.ServiceUsedCommand import ServiceUsedCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='CheckServiceUsed')


class CheckServiceUsed(CheckSNMP):

    def __init__(self: T, id: str):
        CheckSNMP.__init__(self, id, 'CheckServiceUsed', 'monitoring_plugins_snmp_synology_service_used')
        self.add_service_group(ServiceGroup.create('synology'))
        self.add_service_group(ServiceGroup.create('system_health'))

        self.__service: Union[str, None] = None
        self.__warning: Union[int, None] = None
        self.__critical: Union[int, None] = None

    def set_service(self: T, service: str) -> T:
        self.__service = service
        return self

    def get_service(self: T) -> Union[str, None]:
        return self.__service

    def set_warning(self: T, warning: int) -> T:
        self.__warning = warning
        return self

    def get_warning(self: T) -> Union[int, None]:
        return self.__warning

    def set_critical(self: T, critical: int) -> T:
        self.__critical = critical
        return self

    def get_critical(self: T) -> Union[int, None]:
        return self.__critical

    def validate(self: T):
        CheckSNMP.validate(self)
        if None is self.__service:
            raise Exception('You have to set a service for ' + self.get_id())
        if None is self.__warning:
            raise Exception('You have to set a warning bound for ' + self.get_id())
        if None is self.__critical:
            raise Exception('You have to set a critical bound for ' + self.get_id())

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckServiceUsed(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckServiceUsed):
            raise Exception('Id must be for an instance of CheckServiceUsed but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_snmp_synology_service_used'):
            ServiceUsedCommand.create('monitoring_plugins_snmp_synology_service_used')

        return check
