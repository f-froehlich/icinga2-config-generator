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
from typing import Tuple

from icinga2confgen.Checks.MonitoringPlugins.SNMP.CheckSNMP import CheckSNMP
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.StorageIOCommand import StorageIOCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='CheckStorageIO')


class CheckStorageIO(CheckSNMP):

    def __init__(self: T, id: str):
        CheckSNMP.__init__(self, id, 'CheckStorageIO', 'monitoring_plugins_snmp_synology_storage_io')
        self.add_service_group(ServiceGroup.create('synology'))
        self.add_service_group(ServiceGroup.create('system_health'))

        self.__disk: Union[int, None] = None
        self.__warning: Union[str, None] = None
        self.__critical: Union[str, None] = None

    def set_disk(self: T, number: int) -> T:
        self.__disk = number
        return self

    def get_disk(self: T) -> Union[int, None]:
        return self.__disk

    def set_warning(self: T, load1: int, load5: int, load15: int) -> T:
        self.__warning = str(f"{load1},{load5},{load15}")
        return self

    def get_warning(self: T) -> Union[Tuple[int, int, int], None]:
        if None is self.__warning:
            return None
        warning = self.__warning.split(',')
        return tuple((int(warning[0]), int(warning[1]), int(warning[2])))

    def set_critical(self: T, load1: int, load5: int, load15: int) -> T:
        self.__critical = str(f"{load1},{load5},{load15}")
        return self

    def get_critical(self: T) -> Union[Tuple[int, int, int], None]:
        if None is self.__critical:
            return None
        critical = self.__critical.split(',')
        return tuple((int(critical[0]), int(critical[1]), int(critical[2])))

    def validate(self: T):
        CheckSNMP.validate(self)
        if self.__disk is None:
            raise Exception('You have to set the number of disk!')

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckStorageIO(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckStorageIO):
            raise Exception('Id must be for an instance of CheckStorageIO but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_snmp_synology_storage_io'):
            StorageIOCommand.create('monitoring_plugins_snmp_synology_storage_io')

        return check
