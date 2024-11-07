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


class DigCommand(Command):

    def __init__(self, id: str):
        Command.__init__(self, id)

    @staticmethod
    def create(id: str, force_create: bool = False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = DigCommand(id)
            ConfigBuilder.add_command(id, command)
        elif not isinstance(command, DigCommand):
            raise Exception('Id must be for an instance of DigCommand but other instance is returned')

        return command

    def get_command(self) -> str:
        return 'check_dig'

    def get_arguments(self) -> str:
        config = """{
    "--hostname" = {
      value = "$command_dig_dnsserver_hostname$"
      set_if = {{ macro("$command_dig_dnsserver_hostname$") != false }}
    }
    "--port" = {
      value = "$command_dig_dnsserver_port$"
      set_if = {{ macro("$command_dig_dnsserver_port$") != false }}
    }
    "--use-ipv4" = {
      set_if = "$command_dig_only_ipv4$"
    }
    "--use-ipv6" = {
      set_if = "$command_dig_only_ipv6$"
    }
    "--query_address" = {
      value = "$command_dig_question$"
      required = true
    }
    "--record_type" = {
      value = "$command_dig_record_type$"
      required = true
    }
    "--expected_address" = {
      value = "$command_dig_expected_address$"
      required = true
    }
    "--dig-arguments" = {
      value = "$command_dig_question_arguments$"
      set_if = {{ macro("$command_dig_question_arguments$") != false }}
    }
    "--timeout" = {
      value = "$command_dig_timeout$"
      required = true
    }
    "--warning" = {
      value = "$command_dig_warning_time$"
      required = true
    }
    "--critical" = {
      value = "$command_dig_critical_time$"
      required = true
    }
  }
"""

        return config
