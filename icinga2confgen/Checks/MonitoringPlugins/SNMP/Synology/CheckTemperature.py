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

from icinga2confgen.Checks.MonitoringPlugins.SNMP.CheckSNMP import CheckSNMP
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.TemperatureCommand import TemperatureCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='CheckTemperature')


class CheckTemperature(CheckSNMP):

    def __init__(self: T, id: str):
        CheckSNMP.__init__(self, id, 'CheckTemperature', 'monitoring_plugins_snmp_synology_temperature')
        self.add_service_group(ServiceGroup.create('synology'))
        self.add_service_group(ServiceGroup.create('system_health'))

        self.__warning: int = 35
        self.__critical: int = 45

    def set_warning(self: T, warning: int) -> T:
        self.__warning = warning
        return self

    def get_warning(self: T) -> int:
        return self.__warning

    def set_critical(self: T, critical: int) -> T:
        self.__critical = critical
        return self

    def get_critical(self: T) -> int:
        return self.__critical

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckTemperature(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckTemperature):
            raise Exception('Id must be for an instance of CheckTemperature but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_snmp_synology_temperature'):
            TemperatureCommand.create('monitoring_plugins_snmp_synology_temperature')

        return check
