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
from icinga2confgen.Commands.MonitoringPlugins.SNMP.UCD_SNMP_MIB.MemoryCommand import MemoryCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='CheckMemory')


class CheckMemory(CheckSNMP):

    def __init__(self: T, id: str):
        CheckSNMP.__init__(self, id, 'CheckMemory', 'monitoring_plugins_snmp_ucd_snmp_mib_memory')
        self.add_service_group(ServiceGroup.create('memory'))
        self.add_service_group(ServiceGroup.create('system_health'))

        self.__memory: Union[int, None] = None

        self.__warning_total: Union[int, None] = None
        self.__critical_total: Union[int, None] = None
        self.__ignore_total: Union[bool, None] = None

        self.__warning_swap: Union[int, None] = None
        self.__critical_swap: Union[int, None] = None
        self.__ignore_swap: Union[bool, None] = None

        self.__warning_swap_txt: Union[int, None] = None
        self.__critical_swap_txt: Union[int, None] = None
        self.__ignore_swap_txt: Union[bool, None] = None

        self.__warning_real: Union[int, None] = None
        self.__critical_real: Union[int, None] = None
        self.__ignore_real: Union[bool, None] = None

        self.__warning_real_txt: Union[int, None] = None
        self.__critical_real_txt: Union[int, None] = None
        self.__ignore_real_txt: Union[bool, None] = None

        self.__warning_shared: Union[int, None] = None
        self.__critical_shared: Union[int, None] = None
        self.__ignore_shared: Union[bool, None] = None

        self.__warning_buffer: Union[int, None] = None
        self.__critical_buffer: Union[int, None] = None
        self.__ignore_buffer: Union[bool, None] = None

        self.__warning_cache: Union[int, None] = None
        self.__critical_cache: Union[int, None] = None
        self.__ignore_cache: Union[bool, None] = None

        self.__warning_min_swap: Union[int, None] = None
        self.__critical_min_swap: Union[int, None] = None
        self.__ignore_min_swap: Union[bool, None] = None

    def set_memory(self: T, memory: int) -> T:
        self.__memory = memory
        return self

    def get_memory(self: T) -> Union[int, None]:
        return self.__memory

    def set_warning_total(self: T, warning: int) -> T:
        self.__warning_total = warning
        return self

    def get_warning_total(self: T) -> Union[int, None]:
        return self.__warning_total

    def set_critical_total(self: T, critical: int) -> T:
        self.__critical_total = critical
        return self

    def get_critical_total(self: T) -> Union[int, None]:
        return self.__critical_total

    def set_ignore_total(self: T, ignore: bool) -> T:
        self.__ignore_total = ignore
        return self

    def get_ignore_total(self: T) -> Union[bool, None]:
        return self.__ignore_total

    def set_warning_swap(self: T, warning: int) -> T:
        self.__warning_swap = warning
        return self

    def get_warning_swap(self: T) -> Union[int, None]:
        return self.__warning_swap

    def set_critical_swap(self: T, critical: int) -> T:
        self.__critical_swap = critical
        return self

    def get_critical_swap(self: T) -> Union[int, None]:
        return self.__critical_swap

    def set_ignore_swap(self: T, ignore: bool) -> T:
        self.__ignore_swap = ignore
        return self

    def get_ignore_swap(self: T) -> Union[bool, None]:
        return self.__ignore_swap

    def set_warning_swap_txt(self: T, warning: int) -> T:
        self.__warning_swap_txt = warning
        return self

    def get_warning_swap_txt(self: T) -> Union[int, None]:
        return self.__warning_swap_txt

    def set_critical_swap_txt(self: T, critical: int) -> T:
        self.__critical_swap_txt = critical
        return self

    def get_critical_swap_txt(self: T) -> Union[int, None]:
        return self.__critical_swap_txt

    def set_ignore_swap_txt(self: T, ignore: bool) -> T:
        self.__ignore_swap_txt = ignore
        return self

    def get_ignore_swap_txt(self: T) -> Union[bool, None]:
        return self.__ignore_swap_txt

    def set_warning_real(self: T, warning: int) -> T:
        self.__warning_real = warning
        return self

    def get_warning_real(self: T) -> Union[int, None]:
        return self.__warning_real

    def set_critical_real(self: T, critical: int) -> T:
        self.__critical_real = critical
        return self

    def get_critical_real(self: T) -> Union[int, None]:
        return self.__critical_real

    def set_ignore_real(self: T, ignore: bool) -> T:
        self.__ignore_real = ignore
        return self

    def get_ignore_real(self: T) -> Union[bool, None]:
        return self.__ignore_real

    def set_warning_real_txt(self: T, warning: int) -> T:
        self.__warning_real_txt = warning
        return self

    def get_warning_real_txt(self: T) -> Union[int, None]:
        return self.__warning_real_txt

    def set_critical_real_txt(self: T, critical: int) -> T:
        self.__critical_real_txt = critical
        return self

    def get_critical_real_txt(self: T) -> Union[int, None]:
        return self.__critical_real_txt

    def set_ignore_real_txt(self: T, ignore: bool) -> T:
        self.__ignore_real_txt = ignore
        return self

    def get_ignore_real_txt(self: T) -> Union[bool, None]:
        return self.__ignore_real_txt

    def set_warning_shared(self: T, warning: int) -> T:
        self.__warning_shared = warning
        return self

    def get_warning_shared(self: T) -> Union[int, None]:
        return self.__warning_shared

    def set_critical_shared(self: T, critical: int) -> T:
        self.__critical_shared = critical
        return self

    def get_critical_shared(self: T) -> Union[int, None]:
        return self.__critical_shared

    def set_ignore_shared(self: T, ignore: bool) -> T:
        self.__ignore_shared = ignore
        return self

    def get_ignore_shared(self: T) -> Union[bool, None]:
        return self.__ignore_shared

    def set_warning_buffer(self: T, critical: int) -> T:
        self.__warning_buffer = critical
        return self

    def get_warning_buffer(self: T) -> Union[int, None]:
        return self.__warning_buffer

    def set_critical_buffer(self: T, critical: int) -> T:
        self.__critical_buffer = critical
        return self

    def get_critical_buffer(self: T) -> Union[int, None]:
        return self.__critical_buffer

    def set_ignore_buffer(self: T, ignore: bool) -> T:
        self.__ignore_buffer = ignore
        return self

    def get_ignore_buffer(self: T) -> Union[bool, None]:
        return self.__ignore_buffer

    def set_warning_cache(self: T, critical: int) -> T:
        self.__warning_cache = critical
        return self

    def get_warning_cache(self: T) -> Union[int, None]:
        return self.__warning_cache

    def set_critical_cache(self: T, critical: int) -> T:
        self.__critical_cache = critical
        return self

    def get_critical_cache(self: T) -> Union[int, None]:
        return self.__critical_cache

    def set_ignore_cache(self: T, ignore: bool) -> T:
        self.__ignore_cache = ignore
        return self

    def get_ignore_cache(self: T) -> Union[bool, None]:
        return self.__ignore_cache

    def set_warning_min_swap(self: T, critical: int) -> T:
        self.__warning_min_swap = critical
        return self

    def get_warning_min_swap(self: T) -> Union[int, None]:
        return self.__warning_min_swap

    def set_critical_min_swap(self: T, critical: int) -> T:
        self.__critical_min_swap = critical
        return self

    def get_critical_min_swap(self: T) -> Union[int, None]:
        return self.__critical_min_swap

    def set_ignore_min_swap(self: T, ignore: bool) -> T:
        self.__ignore_min_swap = ignore
        return self

    def get_ignore_min_swap(self: T) -> Union[bool, None]:
        return self.__ignore_min_swap

    def validate(self: T):
        CheckSNMP.validate(self)
        if self.__memory is None:
            raise Exception('You have to set the number of memory!')

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckMemory(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckMemory):
            raise Exception('Id must be for an instance of CheckMemory but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_snmp_ucd_snmp_mib_memory'):
            MemoryCommand.create('monitoring_plugins_snmp_ucd_snmp_mib_memory')

        return check
