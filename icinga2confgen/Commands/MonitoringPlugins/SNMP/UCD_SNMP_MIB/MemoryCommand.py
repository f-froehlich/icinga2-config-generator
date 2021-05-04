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

import typing

from icinga2confgen.Commands.MonitoringPlugins.SNMP.SNMPCommand import SNMPCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='MemoryCommand')


class MemoryCommand(SNMPCommand):

    def __init__(self: T, id: str):
        SNMPCommand.__init__(self, id)

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = MemoryCommand(id)
            ConfigBuilder.add_command(id, command)
        elif not isinstance(command, MemoryCommand):
            raise Exception('Id must be for an instance of MemoryCommand but other instance is returned')

        return command

    def get_command(self: T) -> str:
        return 'snmp/UCD_SNMP_MIB/check_memory.py'

    def get_specific_arguments(self: T):
        return """
    "-m" = {
      value = "$command_memory_memory$"
      required = true
    }
    "--warning-total" = {
      value = "$command_memory_warning_total$"
      set_if = {{ macro("$command_memory_warning_total$") != false }}
    }
    "--critical-total" = {
      value = "$command_memory_critical_total$"
      set_if = {{ macro("$command_memory_critical_total$") != false }}
    }
    "--ignore-total" = {
      value = "$command_memory_critical_total$"
      set_if = {{ macro("$command_memory_critical_total$") != false }}
    }
    "--warning-swap" = {
      value = "$command_memory_warning_swap$"
      set_if = {{ macro("$command_memory_warning_swap$") != false }}
    }
    "--critical-swap" = {
      value = "$command_memory_critical_swap$"
      set_if = {{ macro("$command_memory_critical_swap$") != false }}
    }
    "--ignore-swap" = {
      value = "$command_memory_critical_swap$"
      set_if = {{ macro("$command_memory_critical_swap$") != false }}
    }
    "--warning-swap-txt" = {
      value = "$command_memory_warning_swap_txt$"
      set_if = {{ macro("$command_memory_warning_swap_txt$") != false }}
    }
    "--critical-swap-txt" = {
      value = "$command_memory_critical_swap_txt$"
      set_if = {{ macro("$command_memory_critical_swap_txt$") != false }}
    }
    "--ignore-swap-txt" = {
      value = "$command_memory_critical_swap_txt$"
      set_if = {{ macro("$command_memory_critical_swap_txt$") != false }}
    }
    "--warning-real" = {
      value = "$command_memory_warning_real$"
      set_if = {{ macro("$command_memory_warning_real$") != false }}
    }
    "--critical-real" = {
      value = "$command_memory_critical_real$"
      set_if = {{ macro("$command_memory_critical_real$") != false }}
    }
    "--ignore-real" = {
      value = "$command_memory_critical_real$"
      set_if = {{ macro("$command_memory_critical_real$") != false }}
    }
    "--warning-real-txt" = {
      value = "$command_memory_warning_real_txt$"
      set_if = {{ macro("$command_memory_warning_real_txt$") != false }}
    }
    "--critical-real-txt" = {
      value = "$command_memory_critical_real_txt$"
      set_if = {{ macro("$command_memory_critical_real_txt$") != false }}
    }
    "--ignore-real-txt" = {
      value = "$command_memory_critical_real_txt$"
      set_if = {{ macro("$command_memory_critical_real_txt$") != false }}
    }
    "--warning-shared" = {
      value = "$command_memory_warning_shared$"
      set_if = {{ macro("$command_memory_warning_shared$") != false }}
    }
    "--critical-shared" = {
      value = "$command_memory_critical_shared$"
      set_if = {{ macro("$command_memory_critical_shared$") != false }}
    }
    "--ignore-shared" = {
      value = "$command_memory_critical_shared$"
      set_if = {{ macro("$command_memory_critical_shared$") != false }}
    }
    "--warning-buffer" = {
      value = "$command_memory_warning_buffer$"
      set_if = {{ macro("$command_memory_warning_buffer$") != false }}
    }
    "--critical-buffer" = {
      value = "$command_memory_critical_buffer$"
      set_if = {{ macro("$command_memory_critical_buffer$") != false }}
    }
    "--ignore-buffer" = {
      value = "$command_memory_critical_buffer$"
      set_if = {{ macro("$command_memory_critical_buffer$") != false }}
    }
    "--warning-cache" = {
      value = "$command_memory_warning_cache$"
      set_if = {{ macro("$command_memory_warning_cache$") != false }}
    }
    "--critical-cache" = {
      value = "$command_memory_critical_cache$"
      set_if = {{ macro("$command_memory_critical_cache$") != false }}
    }
    "--ignore-cache" = {
      value = "$command_memory_critical_cache$"
      set_if = {{ macro("$command_memory_critical_cache$") != false }}
    }
    "--warning-min-swap" = {
      value = "$command_memory_warning_min_swap$"
      set_if = {{ macro("$command_memory_warning_min_swap$") != false }}
    }
    "--critical-min-swap" = {
      value = "$command_memory_critical_min_swap$"
      set_if = {{ macro("$command_memory_critical_min_swap$") != false }}
    }
    "--ignore-min-swap" = {
      value = "$command_memory_critical_min_swap$"
      set_if = {{ macro("$command_memory_critical_min_swap$") != false }}
    }
"""
