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


class ProcsCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = ProcsCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_procs'

    def get_arguments(self):
        config = """{
    "-w" = {
      value = "$command_procs_warning_range$"
    }
    "-c" = {
      value = "$command_procs_critical_range$"
    }
    "-m" = {
      value = "$command_procs_metric$"
      set_if = {{ macro("$command_procs_metric$") != false }}
    }
    "-t" = {
      value = "$command_procs_timeout$"
      set_if = {{ macro("$command_procs_timeout$") != false }}
    }
    "-T" = {
      set_if = "$command_procs_traditional$"
    }
    "-s" = {
      value = "$command_procs_state$"
      set_if = {{ macro("$command_procs_state$") != false }}
    }
    "-p" = {
      value = "$command_procs_pid$"
      set_if = {{ macro("$command_procs_pid$") != false }}
    }
    "-z" = {
      value = "$command_procs_vsz$"
      set_if = {{ macro("$command_procs_vsz$") != false }}
    }
    "-u" = {
      value = "$command_procs_user$"
      set_if = {{ macro("$command_procs_user$") != false }}
    }
    "-a" = {
      value = "$command_procs_argument$"
      set_if = {{ macro("$command_procs_argument$") != false }}
    }
    "--ereg-argument-array" = {
      value = "$command_procs_argument_ereg$"
      set_if = {{ macro("$command_procs_argument_ereg$") != false }}
    }
    "-C" = {
      value = "$command_procs_command$"
      set_if = {{ macro("$command_procs_command$") != false }}
    }
    "-k" = {
      set_if = "$command_procs_only_non_kernel$"
    }
  }
"""

        return config
