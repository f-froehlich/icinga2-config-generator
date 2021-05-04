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
from typing import List

from icinga2confgen.Checks.MonitoringPlugins.SNMP.CheckSNMP import CheckSNMP
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.ServiceRunningCommand import ServiceRunningCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='CheckServiceRunning')


class CheckServiceRunning(CheckSNMP):

    def __init__(self: T, id: str):
        CheckSNMP.__init__(self, id, 'CheckServiceRunning', 'monitoring_plugins_snmp_synology_service_running')
        self.add_service_group(ServiceGroup.create('synology'))
        self.add_service_group(ServiceGroup.create('system_health'))

        self.__services: List[str] = []

    def set_services(self: T, services: List[str]) -> T:
        self.__services = services
        return self

    def get_services(self: T) -> List[str]:
        return self.__services

    def add_service(self: T, service: str) -> T:
        self.__services.append(service)
        return self

    def remove_service(self: T, service: str) -> T:
        if service in self.__services:
            self.__services.remove(service)
        return self

    def validate(self: T):
        CheckSNMP.validate(self)
        if 0 == len(self.__services):
            raise Exception('Check service running without services is useless')

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckServiceRunning(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckServiceRunning):
            raise Exception('Id must be for an instance of CheckServiceRunning but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_snmp_synology_service_running'):
            ServiceRunningCommand.create('monitoring_plugins_snmp_synology_service_running')

        return check
