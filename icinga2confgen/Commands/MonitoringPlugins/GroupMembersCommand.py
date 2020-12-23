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
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker


class GroupMembersCommand(MonitoringPluginCommand):

    def __init__(self, id):
        MonitoringPluginCommand.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = GroupMembersCommand(id)
            ConfigBuilder.add_command(id, command)
        elif not isinstance(command, GroupMembersCommand):
            raise Exception('Id must be for an instance of GroupMembersCommand but other instance is returned')

        return command

    def get_command(self):
        return 'check_group_members.py'

    def get_arguments(self):
        config = """{
    "--group" = {
      value = "$command_group_members_group$"
      set_if = {{ macro("$command_group_members_group$") != false }}
    }
    "--user" = {
      value = "$command_group_members_users$"
      set_if = {{ macro("$command_group_members_users$") != false }}
      repeat_key = true
    }
  }
"""
        return config
