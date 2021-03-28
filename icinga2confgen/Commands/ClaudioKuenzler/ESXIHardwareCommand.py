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

from icinga2confgen.Commands.Command import Command
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker


class ESXIHardwareCommand(Command):

    def __init__(self, id: str):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False) -> ESXIHardwareCommand:
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = ESXIHardwareCommand(id)
            ConfigBuilder.add_command(id, command)
        elif not isinstance(command, ESXIHardwareCommand):
            raise Exception('Id must be for an instance of ESXIHardwareCommand but other instance is returned')

        return command

    def get_command_definition(self) -> str:
        return '[ "$claudio_kuenzler_plugin_dir$" + "/' + self.get_command() + '"]'

    def get_command(self) -> str:
        return 'check_esxi_hardware.py'

    def get_arguments(self) -> str:
        config = """{
    "-H" = {
      value = "$command_esxi_hardware_host$"
      required = true
      description = "report on HOST"
    }
    "-U" = {
      value = "$command_esxi_hardware_user$"
      required = true
      description = "user to connect as"
    }
    "-P" = {
      value = "$command_esxi_hardware_password$"
      required = true
      description = "password"
    }
    "-C" = {
      value = "$command_esxi_hardware_port$"
      description = "cim port"
    }
    "-S" = {
      value = "$command_esxi_hardware_sslproto$"
      description = "ssl/tls protocol"
    }
    "-V" = {
      value = "$command_esxi_hardware_vendor$"
      description = "Vendor code: auto, dell, hp, ibm, intel, or unknown"
    }
    "-I" = {
      value = "$command_esxi_hardware_html$"
      set_if = {{ macro("$command_esxi_hardware_html$") != false }}
      description = "generate html links for country XX"
    }
    "-i" = {
      value = "$command_esxi_hardware_ignore$"
      description = "comma-separated list of elements to ignore"
    }
    "-r" = {
      set_if = "$command_esxi_hardware_regex$"
      description = "Allow regular expression lookups of elements in ignore list"
    }
    "-p" = {
      set_if = "$command_esxi_hardware_perfdata$"
      description = "collect performance data for pnp4nagios"
    }
    "--no-power" = {
      set_if = "$command_esxi_hardware_nopower$"
      description = "don't collect power performance data"
    }
    "--no-volts" = {
      set_if = "$command_esxi_hardware_novolts$"
      description = "don't collect voltage performance data"
    }
    "--no-current" = {
      set_if = "$command_esxi_hardware_nocurrent$"
      description = "don't collect current performance data"
    }
    "--no-temp" = {
      set_if = "$command_esxi_hardware_notemp$"
      description = "don't collect temperature performance data"
    }
    "--no-fan" = {
      set_if = "$command_esxi_hardware_nofan$"
      description = "don't collect fan performance data"
    }
    "--no-lcd" = {
      set_if = "$command_esxi_hardware_nolcd$"
      description = "don't collect lcd/front display status data"
    }
    "--no-intrusion" = {
      set_if = "$command_esxi_hardware_nointrusion$"
      description = "don't collect chassic intrusion status data"
    }
}
"""

        return config
