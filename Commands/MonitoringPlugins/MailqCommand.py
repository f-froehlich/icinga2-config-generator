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


class MailqCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)
        command = ConfigBuilder.get_command(id)
        if None is command:
            id = 'command_' + id
            command = MailqCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'mailq'

    def get_arguments(self):
        config = """{
    "-w" = {
      value = "$command_mailq_warning$"
    }
    "-c" = {
      value = "$command_mailq_critical$"
    }
    "-W" = {
      value = "$command_mailq_warning_same_domain$"
      set_if = {{ macro("$command_mailq_warning_same_domain$") != false }}
    }
    "-C" = {
      value = "$command_mailq_critical_same_domain$"
      set_if = {{ macro("$command_mailq_critical_same_domain$") != false }}
    }
    "-s" = {
      value = "$command_mailq_sudo$"
      set_if = {{ macro("$command_mailq_sudo$") != false }}
    }
  }
"""

        return config