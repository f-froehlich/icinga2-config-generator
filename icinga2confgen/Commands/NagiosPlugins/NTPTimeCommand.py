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


class NTPTimeCommand(Command):

    def __init__(self, id: str):
        Command.__init__(self, id)

    @staticmethod
    def create(id: str, force_create: bool = False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = NTPTimeCommand(id)
            ConfigBuilder.add_command(id, command)
        elif not isinstance(command, NTPTimeCommand):
            raise Exception('Id must be for an instance of NTPTimeCommand but other instance is returned')

        return command

    def get_command(self) -> str:
        return 'check_ntp_time'

    def get_arguments(self) -> str:
        config = """{
    "--use-ipv4" = {
      value = "$command_ntp_time_force_ipv4$"
      set_if = {{ macro("$command_ntp_time_force_ipv4$") != false }}
    }
    "--use-ipv6" = {
      value = "$command_ntp_time_force_ipv6$"
      set_if = {{ macro("$command_ntp_time_force_ipv6$") != false }}
    }
    "--hostname" = {
      value = "$command_ntp_time_ntp_server$"
      required = true
    }
    "--port" = {
      value = "$command_ntp_time_ntp_server_port$"
      set_if = {{ macro("$command_ntp_time_ntp_server_port$") != false }}
    }
    "--quiet" = {
      set_if = "$command_ntp_time_quiet$"
    }
    "--warning" = {
      value = "$command_ntp_time_warning$"
    }
    "--critical" = {
      value = "$command_ntp_time_critical$"
    }
    "--time_offset" = {
      value = "$command_ntp_time_time_offset$"
      set_if = {{ macro("$command_ntp_time_time_offset$") != false }}
    }
    "--delay" = {
      value = "$command_ntp_time_delay$"
      set_if = "$command_ntp_time_delay$"
    }
    "--stratum-warn" = {
      value = "$command_ntp_time_stratum_warn$"
      set_if = {{ macro("$command_ntp_time_stratum_warn$") != false }}
    }
    "--stratum-crit" = {
      value = "$command_ntp_time_stratum_crit$"
      set_if = {{ macro("$command_ntp_time_stratum_crit$") != false }}
    }
    "--timeout" = {
      value = "$command_ntp_time_timeout$"
      set_if = {{ macro("$command_ntp_time_timeout$") != false }}
    }
  }
"""

        return config
