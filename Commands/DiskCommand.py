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
from ValueChecker import ValueChecker


class DiskCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)
        command = ConfigBuilder.get_command(id)
        if None is command:
            id = 'command_' + id
            command = DiskCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_disk'

    def get_arguments(self):
        config = """{
    "--warning" = {
      value = "$command_disk_warning$"
    }
    "--critical" = {
      value = "$command_disk_critical$"
    }
    "--iwarning" = {
      value = "$command_disk_inode_warning$%"
    }
    "--icritical" = {
      value = "$command_disk_inode_critical$%"
    }
    "--combined-thresholds" = {
      set_if = "$command_disk_combined_thresholds$"
    }
    "--path" = {
      value = "$command_disk_path$"
    }
    "--partition" = {
      value = "$command_disk_partition$"
    }
    "--exclude_device" = {
      value = "$command_disk_exclude_device$"
      set_if = "$command_disk_exclude_device$"
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
      set_if = "$command_disk_group$"
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
      set_if = "$command_disk_eregi_path$"
    }
    "--eregi-partition" = {
      value = "$command_disk_eregi_partition$"
      set_if = "$command_disk_eregi_partition$"
    }
    "--ignore-eregi-path" = {
      value = "$command_disk_ignore_eregi_path$"
      set_if = "$command_disk_ignore_eregi_path$"
    }
    "--ignore-eregi-partition" = {
      value = "$command_disk_ignore_eregi_partition$"
      set_if = "$command_disk_ignore_eregi_partition$"
    }
    "--ereg-path" = {
      value = "$command_disk_ereg_path$"
      set_if = "$command_disk_ereg_path$"
    }
    "--ereg-partition" = {
      value = "$command_disk_ereg_partition$"
      set_if = "$command_disk_ereg_partition$"
    }
    "--ignore-ereg-path" = {
      value = "$command_disk_ignore_ereg_path$"
      set_if = "$command_disk_ignore_ereg_path$"
    }
    "--ignore-ereg-partition" = {
      value = "$command_disk_ignore_ereg_partition$"
      set_if = "$command_disk_ignore_ereg_partition$"
    }
    "--timeout" = {
      value = "$command_disk_timeout$"
      set_if = "$command_disk_timeout$"
    }
    "--units" = {
      value = "$command_disk_units$"
      set_if = "$command_disk_units$"
    }
    "--exclude-type" = {
      value = "$command_disk_exclude_type$"
      set_if = "$command_disk_exclude_type$"
    }
    "--include-type" = {
      value = "$command_disk_include_type$"
      set_if = "$command_disk_include_type$"
    }
    "--newlines" = {
      set_if = "$command_disk_newlines$"
    }
  }
"""

        return config
