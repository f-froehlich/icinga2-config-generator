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


class PgSQLCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = PgSQLCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_pgsql'

    def get_arguments(self):
        config = """{
    
    "-H" = {
      value = "$command_pgsql_host$"
      set_if = {{ macro("$command_pgsql_host$") != false }}
    }
    "-P" = {
      value = "$command_pgsql_port$"
      set_if = {{ macro("$command_pgsql_port$") != false }}
    }
    "-d" = {
      value = "$command_pgsql_database$"
      set_if = {{ macro("$command_pgsql_database$") != false }}
    }
    "-l" = {
      value = "$command_pgsql_logname$"
      set_if = {{ macro("$command_pgsql_logname$") != false }}
    }
    "-p" = {
      value = "$command_pgsql_password$"
      set_if = {{ macro("$command_pgsql_password$") != false }}
    }
    "-o" = {
      value = "$command_pgsql_option$"
      set_if = {{ macro("$command_pgsql_option$") != false }}
    }
    "-w" = {
      value = "$command_pgsql_warning$"
      set_if = {{ macro("$command_pgsql_warning$") != false }}
    }
    "-c" = {
      value = "$command_pgsql_critical$"
      set_if = {{ macro("$command_pgsql_critical$") != false }}
    }
    "-t" = {
      value = "$command_pgsql_timeout$"
      set_if = {{ macro("$command_pgsql_timeout$") != false }}
    }
    "-q" = {
      value = "$command_pgsql_query$"
      set_if = {{ macro("$command_pgsql_query$") != false }}
    }
    "-W" = {
      value = "$command_pgsql_warning_range$"
      set_if = {{ macro("$command_pgsql_warning_range$") != false }}
    }
    "-C" = {
      value = "$command_pgsql_critical_range$"
      set_if = {{ macro("$command_pgsql_critical_range$") != false }}
    }
  }
"""

        return config
