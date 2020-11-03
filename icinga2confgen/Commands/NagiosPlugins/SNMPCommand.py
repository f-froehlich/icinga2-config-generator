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

from icinga2confgen.Commands.Command import Command
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker


class SNMPCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = SNMPCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_snmp'

    def get_arguments(self):
        config = """{
    "-4" = {
      set_if = "$command_snmp_over_ipv4$"
    }
    "-6" = {
      set_if = "$command_snmp_over_ipv6$"
    }
    "-H" = {
      value = "$command_snmp_host$"
      required = true
    }
    "-p" = {
      value = "$command_snmp_port$"
      set_if = {{ macro("$command_snmp_port$") != false }}
    }
    "-n" = {
      set_if = "$command_snmp_snmp_getnext$"
    }
    "-P" = {
      value = "$command_snmp_protocol$"
      set_if = {{ macro("$command_snmp_protocol$") != false }}
    }
    "-N" = {
      value = "$command_snmp_context$"
      set_if = {{ macro("$command_snmp_context$") != false }}
    }
    "-L" = {
      value = "$command_snmp_seclevel$"
      set_if = {{ macro("$command_snmp_seclevel$") != false }}
    }
    "-a" = {
      value = "$command_snmp_authproto$"
      set_if = {{ macro("$command_snmp_authproto$") != false }}
    }
    "-x" = {
      value = "$command_snmp_privproto$"
      set_if = {{ macro("$command_snmp_privproto$") != false }}
    }
    "-C" = {
      value = "$command_snmp_community$"
      set_if = {{ macro("$command_snmp_community$") != false }}
    }
    "-U" = {
      value = "$command_snmp_username$"
      set_if = {{ macro("$command_snmp_username$") != false }}
    }
    "-A" = {
      value = "$command_snmp_authpassword$"
      set_if = {{ macro("$command_snmp_authpassword$") != false }}
    }
    "-X" = {
      value = "$command_snmp_privpassword$"
      set_if = {{ macro("$command_snmp_privpassword$") != false }}
    }
    "-o" = {
      value = "$command_snmp_oids$"
      required = true
    }
    "-d" = {
      value = "$command_snmp_delimiter$"
      set_if = {{ macro("$command_snmp_delimiter$") != false }}
    }
    "-w" = {
      value = "$command_snmp_warning$"
      set_if = {{ macro("$command_snmp_warning$") != false }}
    }
    "-c" = {
      value = "$command_snmp_critical$"
      set_if = {{ macro("$command_snmp_critical$") != false }}
    }
    "--rate" = {
      set_if = "$command_snmp_rate$"
    }
    "--rate-multiplier" = {
      value = "$command_snmp_rate_multiplier$"
      set_if = {{ macro("$command_snmp_rate_multiplier$") != false }}
    }
    "--offset" = {
      value = "$command_snmp_offset$"
      set_if = {{ macro("$command_snmp_offset$") != false }}
    }
    "--string" = {
      value = "$command_snmp_string$"
      set_if = {{ macro("$command_snmp_string$") != false }}
    }
    "--ereg" = {
      value = "$command_snmp_ereg$"
      set_if = {{ macro("$command_snmp_ereg$") != false }}
    }
    "--invert-search" = {
      set_if = "$command_snmp_invert$"
    }
    "--label" = {
      value = "$command_snmp_label$"
      set_if = {{ macro("$command_snmp_label$") != false }}
    }
    "--units" = {
      value = "$command_snmp_units$"
      set_if = {{ macro("$command_snmp_units$") != false }}
    }
    "--output-delimiter" = {
      value = "$command_snmp_output_delimiter$"
      set_if = {{ macro("$command_snmp_output_delimiter$") != false }}
    }
    "--timeout" = {
      value = "$command_snmp_timeout$"
      set_if = {{ macro("$command_snmp_timeout$") != false }}
    }
    "--retries" = {
      value = "$command_snmp_retries$"
      set_if = {{ macro("$command_snmp_retries$") != false }}
    }
    "--perf-oids" = {
      set_if = "$command_snmp_perf_oids$"
    }
  }
"""

        return config
