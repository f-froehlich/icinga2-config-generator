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


class DiskCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = DiskCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_disk'

    def get_arguments(self):
        config = """{
    "--warning" = {
      value = "$command_disk_warning$"
      required = true
    }
    "--critical" = {
      value = "$command_disk_critical$"
      required = true
    }
    "--iwarning" = {
      value = "$command_disk_inode_warning$%"
      required = true
    }
    "--icritical" = {
      value = "$command_disk_inode_critical$%"
      required = true
    }
    "--combined-thresholds" = {
      set_if = "$command_disk_combined_thresholds$"
    }
    "--path" = {
      value = "$command_disk_path$"
      set_if = {{ macro("$command_disk_path$") != false }}
      repeat_key = true
    }
    "--partition" = {
      value = "$command_disk_partition$"
      set_if = {{ macro("$command_disk_partition$") != false }}
    }
    "--exclude_device" = {
      value = "$command_disk_exclude_device$"
      set_if = {{ macro("$command_disk_exclude_device$") != false }}
    }
    "--clear" = {
      set_if = "$command_disk_clear_thresholds$"
    }
    "--exact-match" = {
      set_if = "$command_disk_exact_match$"
    }
    "--errors-only" = {
      set_if = "$command_disk_errors_only$"
    }
    "--freespace-ignore-reserved" = {
      set_if = "$command_disk_freespace_ignore_reserved$"
    }
    "--group" = {
      value = "$command_disk_group$"
      set_if = {{ macro("$command_disk_group$") != false }}
    }
    "--local" = {
      set_if = "$command_disk_local$"
    }
    "--skip-fake-fs" = {
      set_if = "$command_disk_skip_fake_fs$"
    }
    "--inode-perfdata" = {
      set_if = "$command_disk_inode_perfdata$"
    }
    "--stat-remote-fs" = {
      set_if = "$command_disk_stat_remote_fs$"
    }
    "--mountpoint" = {
      set_if = "$command_disk_display_mountpoint$"
    }
    "--all" = {
      set_if = "$command_disk_all$"
    }
    "--eregi-path" = {
      value = "$command_disk_eregi_path$"
      set_if = {{ macro("$command_disk_eregi_path$") != false }}
      repeat_key = true
    }
    "--eregi-partition" = {
      value = "$command_disk_eregi_partition$"
      set_if = {{ macro("$command_disk_eregi_partition$") != false }}
    }
    "--ignore-eregi-path" = {
      value = "$command_disk_ignore_eregi_path$"
      set_if = {{ macro("$command_disk_ignore_eregi_path$") != false }}
      repeat_key = true
    }
    "--ignore-eregi-partition" = {
      value = "$command_disk_ignore_eregi_partition$"
      set_if = {{ macro("$command_disk_ignore_eregi_partition$") != false }}
    }
    "--ereg-path" = {
      value = "$command_disk_ereg_path$"
      set_if = {{ macro("$command_disk_ereg_path$") != false }}
      repeat_key = true
    }
    "--ereg-partition" = {
      value = "$command_disk_ereg_partition$"
      set_if = {{ macro("$command_disk_ereg_partition$") != false }}
    }
    "--ignore-ereg-path" = {
      value = "$command_disk_ignore_ereg_path$"
      set_if = {{ macro("$command_disk_ignore_ereg_path$") != false }}
      repeat_key = true
    }
    "--ignore-ereg-partition" = {
      value = "$command_disk_ignore_ereg_partition$"
      set_if = {{ macro("$command_disk_ignore_ereg_partition$") != false }}
    }
    "--timeout" = {
      value = "$command_disk_timeout$"
      set_if = {{ macro("$command_disk_timeout$") != false }}
    }
    "--units" = {
      value = "$command_disk_units$"
      set_if = {{ macro("$command_disk_units$") != false }}
    }
    "--exclude-type" = {
      value = "$command_disk_exclude_type$"
      set_if = {{ macro("$command_disk_exclude_type$") != false }}
      repeat_key = true
  }
    "--include-type" = {
      value = "$command_disk_include_type$"
      set_if = {{ macro("$command_disk_include_type$") != false }}
      repeat_key = true
    }
    "--newlines" = {
      set_if = "$command_disk_newlines$"
    }
  }
"""

        return config
