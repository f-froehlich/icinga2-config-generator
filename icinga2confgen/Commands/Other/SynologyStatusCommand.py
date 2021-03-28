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


class SynologyStatusCommand(Command):

    def __init__(self, id: str):
        Command.__init__(self, id)

    @staticmethod
    def create(id: str, force_create: bool = False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = SynologyStatusCommand(id)
            ConfigBuilder.add_command(id, command)
        elif not isinstance(command, SynologyStatusCommand):
            raise Exception('Id must be for an instance of SynologyStatusCommand but other instance is returned')

        return command

    def get_command_definition(self) -> str:
        return '[ "$other_plugin_dir$" + "/' + self.get_command() + '"]'

    def get_command(self) -> str:
        return 'check_snmp_synology'

    def get_arguments(self) -> str:
        config = """{
    "-h" = {
        value = "$command_synology_status_host$"
        required = true
    }
    "-u" = {
        value = "$command_synology_status_user$"
        set_if = {{ macro("$command_synology_status_user$") != false }}
    }
    "-p" = {
        value = "$command_synology_status_password$"
        set_if = {{ macro("$command_synology_status_password$") != false }}
    }
    "-W" = {
        value = "$command_synology_status_warning_temp$"
        set_if = {{ macro("$command_synology_status_warning_temp$") != false }}
    }
    "-C" = {
        value = "$command_synology_status_critical_temp$"
        set_if = {{ macro("$command_synology_status_critical_temp$") != false }}
    }
    "-w" = {
        value = "$command_synology_status_warning_storage$"
        set_if = {{ macro("$command_synology_status_warning_storage$") != false }}
    }
    "-c" = {
        value = "$command_synology_status_critical_storage$"
        set_if = {{ macro("$command_synology_status_critical_storage$") != false }}
    }
    "-2" = {
        set_if = "$command_synology_status_v2$"
    }
    "-i" = {
        set_if = "$command_synology_status_ignore_update$"
    }
    "-U" = {
        set_if = "$command_synology_status_ups$"
    }
}
"""

        return config
