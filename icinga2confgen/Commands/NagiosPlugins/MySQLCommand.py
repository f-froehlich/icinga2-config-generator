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


class MySQLCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = MySQLCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_mysql'

    def get_arguments(self):
        config = """{
    "-H" = {
      value = "$command_mysql_host$"
      set_if = {{ macro("$command_mysql_host$") != false }}
    }
    "-P" = {
      value = "$command_mysql_port$"
      set_if = {{ macro("$command_mysql_port$") != false }}
    }
    "-n" = {
      set_if = "$command_mysql_ignore_auth$"
    }
    "-s" = {
      value = "$command_mysql_socket$"
      set_if = {{ macro("$command_mysql_socket$") != false }}
    }
    "-d" = {
      value = "$command_mysql_database$"
      set_if = {{ macro("$command_mysql_database$") != false }}
    }
    "-f" = {
      value = "$command_mysql_file$"
      set_if = {{ macro("$command_mysql_file$") != false }}
    }
    "-g" = {
      value = "$command_mysql_group$"
      set_if = {{ macro("$command_mysql_group$") != false }}
    }
    "-u" = {
      value = "$command_mysql_user$"
      set_if = {{ macro("$command_mysql_user$") != false }}
    }
    "-p" = {
      value = "$command_mysql_password$"
      set_if = {{ macro("$command_mysql_password$") != false }}
    }
    "-S" = {
      set_if = "$command_mysql_check_slave$"
    }
    "-w" = {
      value = "$command_mysql_slave_warning$"
      set_if = {{ macro("$command_mysql_slave_warning$") != false }}
    }
    "-c" = {
      value = "$command_mysql_slave_critical$"
      set_if = {{ macro("$command_mysql_slave_critical$") != false }}
    }
    "-l" = {
      set_if = "$command_mysql_use_ssl$"
    }
    "-L" = {
      value = "$command_mysql_ssl_ciphers$"
      set_if = {{ macro("$command_mysql_ssl_ciphers$") != false }}
    }
    "-C" = {
      value = "$command_mysql_ca_cert$"
      set_if = {{ macro("$command_mysql_ca_cert$") != false }}
    }
    "-D" = {
      value = "$command_mysql_ca_dir$"
      set_if = {{ macro("$command_mysql_ca_dir$") != false }}
    }
    "-a" = {
      value = "$command_mysql_cert$"
      set_if = {{ macro("$command_mysql_cert$") != false }}
    }
    "-k" = {
      value = "$command_mysql_key$"
      set_if = {{ macro("$command_mysql_key$") != false }}
    }
  }
"""

        return config
