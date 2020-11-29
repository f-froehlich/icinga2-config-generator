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
        NmapCommand.__init__(self, id, 'ciphers', only_tcp=True)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = CiphersCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_ciphers.py'

    def get_arguments(self):
        config = '{\n'
        config += NmapCommand.get_arguments(self)
        config += """
    "--allowed-tlsv1-0-ciphers" = {
      value = "$command_ciphers_allowed_tlsv1_0_ciphers$"
      set_if = {{ macro("$command_ciphers_allowed_tlsv1_0_ciphers$") != false }}
      repeat_key = true
    }
    "--allowed-tlsv1-1-ciphers" = {
      value = "$command_ciphers_allowed_tlsv1_1_ciphers$"
      set_if = {{ macro("$command_ciphers_allowed_tlsv1_1_ciphers$") != false }}
      repeat_key = true
    }
    "--allowed-tlsv1-2-ciphers" = {
      value = "$command_ciphers_allowed_tlsv1_2_ciphers$"
      set_if = {{ macro("$command_ciphers_allowed_tlsv1_2_ciphers$") != false }}
      repeat_key = true
    }
    "--allowed-tlsv1-3-ciphers" = {
      value = "$command_ciphers_allowed_tlsv1_3_ciphers$"
      set_if = {{ macro("$command_ciphers_allowed_tlsv1_3_ciphers$") != false }}
      repeat_key = true
    }
    "--least-tlsv1-0-strength" = {
      value = "$command_ciphers_least_tlsv1_0_strength$"
      set_if = {{ macro("$command_ciphers_least_tlsv1_0_strength$") != false }}
      repeat_key = true
    }
    "--least-tlsv1-1-strength" = {
      value = "$command_ciphers_least_tlsv1_1_strength$"
      set_if = {{ macro("$command_ciphers_least_tlsv1_1_strength$") != false }}
      repeat_key = true
    }
    "--least-tlsv1-2-strength" = {
      value = "$command_ciphers_least_tlsv1_2_strength$"
      set_if = {{ macro("$command_ciphers_least_tlsv1_2_strength$") != false }}
      repeat_key = true
    }
    "--least-tlsv1-3-strength" = {
      value = "$command_ciphers_least_tlsv1_3_strength$"
      set_if = {{ macro("$command_ciphers_least_tlsv1_3_strength$") != false }}
      repeat_key = true
    }
    "--least-strength" = {
      value = "$command_ciphers_least_strength$"
      set_if = {{ macro("$command_ciphers_least_strength$") != false }}
      repeat_key = true
    }
    "--least-strength-overall" = {
      value = "$command_ciphers_least_strength_overall$"
      set_if = {{ macro("$command_ciphers_least_strength_overall$") != false }}
      repeat_key = true
    }
    "--ignore-cipher-name" = {
      set_if = "$command_ciphers_ignore_cipher_name$"
    }
    "--ignore-cipher-strength" = {
      set_if = "$command_ciphers_ignore_cipher_strength$"
    }
    "--ignore-strength" = {
      set_if = "$command_ciphers_ignore_strength$"
    }
    "--ignore-port" = {
      value = "$command_ciphers_ignore_port$"
      set_if = {{ macro("$command_ciphers_ignore_port$") != false }}
      repeat_key = true
    }
  }
"""
        return config
