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

from Commands.Command import Command
from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker


class UPSCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)
        command = ConfigBuilder.get_command(id)
        if None is command:
            id = 'command_' + id
            command = UPSCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'ups'

    def get_arguments(self):
        config = """{
    "-H" = {
      value = "$command_ups_host$"
    }
    "-p" = {
      value = "$command_ups_port$"
      set_if = {{ macro("$command_ups_port$") != false }}
    }
    "-u" = {
      value = "$command_ups_ups$"
    }
    "-T" = {
      value = "$command_ups_temperature$"
    }
    "-v" = {
      value = "$command_ups_variable$"
      set_if = {{ macro("$command_ups_variable$") != false }}
    }
    "-w" = {
      value = "$command_ups_warning$"
      set_if = {{ macro("$command_ups_warning$") != false }}
    }
    "-c" = {
      value = "$command_ups_critical$"
      set_if = {{ macro("$command_ups_critical$") != false }}
    }
    "-t" = {
      value = "$command_ups_timeout$"
      set_if = {{ macro("$command_ups_timeout$") != false }}
    }
  }
"""

        return config