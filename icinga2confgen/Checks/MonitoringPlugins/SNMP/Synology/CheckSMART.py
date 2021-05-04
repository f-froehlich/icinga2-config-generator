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
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.SMARTCommand import SMARTCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='CheckSMART')


class CheckSMART(CheckSNMP):

    def __init__(self: T, id: str):
        CheckSNMP.__init__(self, id, 'CheckSMART', 'monitoring_plugins_snmp_synology_smart')
        self.add_service_group(ServiceGroup.create('synology'))
        self.add_service_group(ServiceGroup.create('system_health'))
        self.add_service_group(ServiceGroup.create('disk'))

        self.__disk: Union[int, None] = None

    def set_disk(self, disks: int) -> T:
        self.__disk = disks
        return self

    def get_disk(self: T) -> Union[int, None]:
        return self.__disk

    def validate(self: T):
        CheckSNMP.validate(self)
        if None is self.__disk:
            raise Exception('You have to set the number of disks')

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckSMART(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckSMART):
            raise Exception('Id must be for an instance of CheckSMART but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_snmp_synology_smart'):
            SMARTCommand.create('monitoring_plugins_snmp_synology_smart')

        return check
