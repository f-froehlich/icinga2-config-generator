#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, commands, checks, ... in python
#
#  Copyright (c) 2020 Fabian Fröhlich <mail@f-froehlich.de> https://f-froehlich.de
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


class DNSSECExpireCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id):
        ConfigBuilder.validate_id(id)
        command = ConfigBuilder.get_command(id)
        if None is command:
            id = 'command_' + id
            command = DNSSECExpireCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_dnssec_expiry.sh'

    def get_arguments(self):
        config = """{
    "-z" = {
      value = "$command_dnssec_expiry_zone$"
    }
    "-w" = {
      value = "$command_dnssec_expiry_warning$"
    }
    "-c" = {
      value = "$command_dnssec_expiry_critical$"
    }
    "-r" = {
      value = "$command_dnssec_expiry_resolver$"
      set_if = "$command_dnssec_expiry_resolver$"
    }
    "-f" = {
      value = "$command_dnssec_expiry_failing_domain$"
      set_if = "$command_dnssec_expiry_failing_domain$"
    }
    "-t" = {
      value = "$command_dnssec_expiry_record_type$"
      set_if = "$command_dnssec_expiry_record_type$"
    }
  }
"""
        return config