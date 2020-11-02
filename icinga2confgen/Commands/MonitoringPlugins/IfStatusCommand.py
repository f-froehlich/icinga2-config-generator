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


class IfStatusCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = IfStatusCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_ifstatus'

    def get_arguments(self):
        config = """{
    "-H" = {
      value = "$command_ifstatus_host$"
      required = true
    }
    "-p" = {
      value = "$command_ifstatus_port$"
      required = true
    }
    "-C" = {
      value = "$command_ifstatus_community$"
      required = true
    }
    "-v" = {
      value = "$command_ifstatus_snmp_version$"
      set_if = {{ macro("$command_ifstatus_snmp_version$") != false }}
    }
    "-I" = {
      set_if = "$command_ifstatus_if_mib$"
    }
    "-x" = {
      value = "$command_ifstatus_snmp_exclude$"
      set_if = {{ macro("$command_ifstatus_snmp_exclude$") != false }}
    }
    "-n" = {
      value = "$command_ifstatus_unused_ports_by_name$"
      set_if = {{ macro("$command_ifstatus_unused_ports_by_name$") != false }}
    }
    "-u" = {
      value = "$command_ifstatus_unused_ports$"
      set_if = {{ macro("$command_ifstatus_unused_ports$") != false }}
    }
    "-L" = {
      value = "$command_ifstatus_seclevel$"
      set_if = {{ macro("$command_ifstatus_seclevel$") != false }}
    }
    "-U" = {
      value = "$command_ifstatus_secname$"
      set_if = {{ macro("$command_ifstatus_secname$") != false }}
    }
    "-c" = {
      value = "$command_ifstatus_context$"
      set_if = {{ macro("$command_ifstatus_context$") != false }}
    }
    "-A" = {
      value = "$command_ifstatus_authpass$"
      set_if = {{ macro("$command_ifstatus_authpass$") != false }}
    }
    "-a" = {
      value = "$command_ifstatus_authproto$"
      set_if = {{ macro("$command_ifstatus_authproto$") != false }}
    }
    "-X" = {
      value = "$command_ifstatus_privpass$"
      set_if = {{ macro("$command_ifstatus_privpass$") != false }}
    }
    "-P" = {
      value = "$command_ifstatus_privproto$"
      set_if = {{ macro("$command_ifstatus_privproto$") != false }}
    }
    "-M" = {
      value = "$command_ifstatus_max_msg_size$"
      set_if = {{ macro("$command_ifstatus_max_msg_size$") != false }}
    }
    "-t" = {
      value = "$command_ifstatus_timeout$"
      set_if = {{ macro("$command_ifstatus_timeout$") != false }}
    }
  }
"""

        return config
