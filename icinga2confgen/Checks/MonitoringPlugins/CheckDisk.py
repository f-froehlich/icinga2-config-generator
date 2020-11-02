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

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.MonitoringPlugins.DiskCommand import DiskCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckDisk(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckDisk', 'disk')
        self.__warning = '20%'
        self.__critical = '10%'
        self.__inode_warning = 20
        self.__inode_critical = 10
        self.__combined_thresholds = None
        self.__path = None
        self.__partition = None
        self.__exclude_device = None
        self.__clear_thresholds = None
        self.__exact_match = None
        self.__errors_only = None
        self.__freespace_ignore_reserved = None
        self.__group = None
        self.__local = None
        self.__skip_fake_fs = None
        self.__inode_perfdata = None
        self.__stat_remote_fs = None
        self.__display_mountpoint = None
        self.__all = None
        self.__eregi_path = None
        self.__eregi_partition = None
        self.__ignore_eregi_path = None
        self.__ignore_eregi_partition = None
        self.__ereg_path = None
        self.__ereg_partition = None
        self.__ignore_ereg_path = None
        self.__ignore_ereg_partition = None
        self.__timeout = None
        self.__units = None
        self.__exclude_type = None
        self.__include_type = None
        self.__newlines = None
        self.set_check_interval('30m')
        self.add_service_group(ServiceGroup.create('disk'))

    def set_warning_units(self, number):
        ValueChecker.is_number(number)
        self.__warning = str(number)
        return self

    def get_warning_units(self):
        return self.__warning

    def set_warning_percent(self, number):
        ValueChecker.is_number(number)
        self.__warning = str(number) + '%'
        return self

    def get_warning_percent(self):
        return self.__warning

    def set_critical_units(self, number):
        ValueChecker.is_number(number)
        self.__critical = str(number)
        return self

    def get_critical_units(self):
        return self.__critical

    def set_critical_percent(self, number):
        ValueChecker.is_number(number)
        self.__critical = str(number) + '%'
        return self

    def get_critical_percent(self):
        return self.__critical

    def set_warning_inode_percent(self, number):
        ValueChecker.is_number(number)
        self.__inode_warning = number
        return self

    def get_warning_inode_percent(self):
        return self.__inode_warning

    def set_critical_inode_percent(self, number):
        ValueChecker.is_number(number)
        self.__inode_critical = number
        return self

    def get_critical_inode_percent(self):
        return self.__inode_critical

    def set_timeout(self, number):
        ValueChecker.is_number(number)
        self.__timeout = number
        return self

    def get_timeout(self):
        return self.__timeout

    def set_newlines(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__newlines = enabled
        return self

    def get_newlines(self):
        return self.__newlines

    def set_combined_thresholds(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__combined_thresholds = enabled
        return self

    def get_combined_thresholds(self):
        return self.__combined_thresholds

    def set_clear_thresholds(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__clear_thresholds = enabled
        return self

    def get_clear_thresholds(self):
        return self.__clear_thresholds

    def set_freespace_ignore_reserved(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__freespace_ignore_reserved = enabled
        return self

    def get_freespace_ignore_reserved(self):
        return self.__freespace_ignore_reserved

    def set_errors_only(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__errors_only = enabled
        return self

    def get_errors_only(self):
        return self.__errors_only

    def set_local(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__local = enabled
        return self

    def get_local(self):
        return self.__local

    def set_all(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__all = enabled
        return self

    def get_all(self):
        return self.__all

    def set_display_mountpoint(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__display_mountpoint = enabled
        return self

    def get_display_mountpoint(self):
        return self.__display_mountpoint

    def set_stat_remote_fs(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__stat_remote_fs = enabled
        return self

    def get_stat_remote_fs(self):
        return self.__stat_remote_fs

    def set_inode_perfdata(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__inode_perfdata = enabled
        return self

    def get_inode_perfdata(self):
        return self.__inode_perfdata

    def set_skip_fake_fs(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__skip_fake_fs = enabled
        return self

    def get_skip_fake_fs(self):
        return self.__skip_fake_fs

    def set_path(self, path):
        ValueChecker.is_string(path)
        if None is self.__path:
            self.__path = []

        self.__path.append(path)
        return self

    def get_path(self):
        return self.__path

    def set_exclude_device(self, exclude_device):
        ValueChecker.is_string(exclude_device)
        self.__exclude_device = exclude_device
        return self

    def get_exclude_device(self):
        return self.__exclude_device

    def set_partition(self, partition):
        ValueChecker.is_string(partition)
        self.__partition = partition
        return self

    def get_partition(self):
        return self.__partition

    def set_group(self, group):
        ValueChecker.is_string(group)
        self.__group = group
        return self

    def get_group(self):
        return self.__group

    def set_units(self, units):
        ValueChecker.is_string(units)
        self.__units = units
        return self

    def get_units(self):
        return self.__units

    def set_include_type(self, include_type):
        ValueChecker.is_string(include_type)
        if None is self.__include_type:
            self.__include_type = []

        self.__include_type.append(include_type)
        return self

    def get_include_type(self):
        return self.__include_type

    def set_exclude_type(self, exclude_type):
        ValueChecker.is_string(exclude_type)
        if None is self.__exclude_type:
            self.__exclude_type = []

        self.__exclude_type.append(exclude_type)
        return self

    def get_exclude_type(self):
        return self.__exclude_type

    def set_eregi_path(self, eregi_path):
        ValueChecker.is_string(eregi_path)
        if None is self.__eregi_path:
            self.__eregi_path = []
        self.__eregi_path.append(eregi_path)
        return self

    def get_eregi_path(self):
        return self.__eregi_path

    def set_eregi_partition(self, eregi_partition):
        ValueChecker.is_string(eregi_partition)
        self.__eregi_partition = eregi_partition
        return self

    def get_eregi_partition(self):
        return self.__eregi_partition

    def set_ereg_path(self, ereg_path):
        ValueChecker.is_string(ereg_path)
        if None is self.__ereg_path:
            self.__ereg_path = []

        self.__ereg_path.append(ereg_path)
        return self

    def get_ereg_path(self):
        return self.__ereg_path

    def set_ereg_partition(self, ereg_partition):
        ValueChecker.is_string(ereg_partition)
        self.__ereg_partition = ereg_partition
        return self

    def get_ereg_partition(self):
        return self.__ereg_partition

    def set_ignore_eregi_path(self, ignore_eregi_path):
        ValueChecker.is_string(ignore_eregi_path)
        if None is self.__ignore_ereg_path:
            self.__ignore_eregi_path = []
        self.__ignore_eregi_path.append(ignore_eregi_path)
        return self

    def get_ignore_eregi_path(self):
        return self.__ignore_eregi_path

    def set_ignore_eregi_partition(self, ignore_eregi_partition):
        ValueChecker.is_string(ignore_eregi_partition)
        self.__ignore_eregi_partition = ignore_eregi_partition
        return self

    def get_ignore_eregi_partition(self):
        return self.__ignore_eregi_partition

    def set_ignore_ereg_path(self, ignore_ereg_path):
        ValueChecker.is_string(ignore_ereg_path)
        if None is self.__ignore_ereg_path:
            self.__ignore_ereg_path = []

        self.__ignore_ereg_path.append(ignore_ereg_path)
        return self

    def get_ignore_ereg_path(self):
        return self.__ignore_ereg_path

    def set_ignore_ereg_partition(self, ignore_ereg_partition):
        ValueChecker.is_string(ignore_ereg_partition)
        self.__ignore_ereg_partition = ignore_ereg_partition
        return self

    def get_ignore_ereg_partition(self):
        return self.__ignore_ereg_partition

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckDisk(id) \
                .set_check_interval('15m') \
                .add_service_group(ServiceGroup.create('disk').set_display_name('Disk'))
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('disk'):
            DiskCommand.create('disk')

        return check

    def validate(self):
        pass
