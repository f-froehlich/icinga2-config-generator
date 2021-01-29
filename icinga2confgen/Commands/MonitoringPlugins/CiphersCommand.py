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

from icinga2confgen.Commands.MonitoringPlugins.NmapCommand import NmapCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker


class CiphersCommand(NmapCommand):

    def __init__(self, id):
        NmapCommand.__init__(self, id, 'ciphers', scan_udp=False, single_host=False)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = CiphersCommand(id)
            ConfigBuilder.add_command(id, command)
        elif not isinstance(command, CiphersCommand):
            raise Exception('Id must be for an instance of CiphersCommand but other instance is returned')

        return command

    def get_command(self):
        return 'check_ciphers.py'

    def get_arguments(self):
        config = '{\n'
        config += NmapCommand.get_arguments(self)
        config += """
    "--allowed-cipher" = {
      value = "$command_ciphers_allowed_ciphers$"
      set_if = {{ macro("$command_ciphers_allowed_ciphers$") != false }}
      repeat_key = true
    }
    "--least-protocol-strength" = {
      value = "$command_ciphers_least_protocol_strength$"
      set_if = {{ macro("$command_ciphers_least_protocol_strength$") != false }}
      repeat_key = true
    }
    "--least-port-strength" = {
      value = "$command_ciphers_least_port_strength$"
      set_if = {{ macro("$command_ciphers_least_port_strength$") != false }}
      repeat_key = true
    }
    "--ignore-cipher-name" = {
      set_if = "$command_ciphers_ignore_cipher_name$"
    }
    "--ignore-protocol-strength" = {
      set_if = "$command_ciphers_ignore_protocol_strength$"
    }
    "--ignore-strength" = {
      set_if = "$command_ciphers_ignore_strength$"
    }
  }
"""
        return config
