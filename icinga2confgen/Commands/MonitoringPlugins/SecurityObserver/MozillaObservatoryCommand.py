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

from icinga2confgen.Commands.MonitoringPlugins.MonitoringPluginCommand import MonitoringPluginCommand
from icinga2confgen.Commands.MonitoringPlugins.WebrequestCommand import WebrequestCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker


class MozillaObservatoryCommand(WebrequestCommand):

    def __init__(self, id: str):
        WebrequestCommand.__init__(self, id, 'mozilla_observatory')

    @staticmethod
    def create(id: str, force_create: bool = False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = MozillaObservatoryCommand(id)
            ConfigBuilder.add_command(id, command)
        elif not isinstance(command, MozillaObservatoryCommand):
            raise Exception('Id must be for an instance of MozillaObservatoryCommand but other instance is returned')

        return command

    def get_command(self) -> str:
        return 'check_mozilla_observatory.py'

    def get_arguments(self) -> str:
        config = """{
    "--ignore-hidden" = {
      set_if = {{ macro("$command_mozilla_observatory_ignore_hidden$") != false }}
    }
    "--ignore-rescan" = {
      set_if = {{ macro("$command_mozilla_observatory_ignore_rescan$") != false }}
    }
    "--warning" = {
      value = "$command_mozilla_observatory_warning_score$"
      set_if = {{ macro("$command_mozilla_observatory_warning_score$") != false }}
    }
    "--warning-grade" = {
      value = "$command_mozilla_observatory_warning_grade$"
      set_if = {{ macro("$command_mozilla_observatory_warning_grade$") != false }}
    }
    "--critical" = {
      value = "$command_mozilla_observatory_critical_score$"
      set_if = {{ macro("$command_mozilla_observatory_critical_score$") != false }}
    }
    "--critical-grade" = {
      value = "$command_mozilla_observatory_critical_grade$"
      set_if = {{ macro("$command_mozilla_observatory_critical_grade$") != false }}
    }
    "--config" = {
      value = "$command_mozilla_observatory_config$"
      set_if = {{ macro("$command_mozilla_observatory_config$") != false }}
      repeat_key = true
    }
    "--host" = {
      value = "$command_mozilla_observatory_host$"
      required = true
    }
   """
        config += WebrequestCommand.get_arguments(self)
        config += """  }
"""

        return config
