#!/usr/bin/python3
# -*- coding: utf-8
import typing

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.NagiosPlugins.DiskCommand import DiskCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

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

T = typing.TypeVar('T', bound='CheckDisk')


class CheckDisk(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckDisk', 'nagios_plugins_disk')
        self.__warning = '20%'
        self.__critical = '10%'
        self.__inode_warning = 20
        self.__inode_critical = 10
        self.__path = []
        self.__partition = None
        self.__exclude_device = None
        self.__clear_thresholds = False
        self.__exact_match = False
        self.__errors_only = False
        self.__freespace_ignore_reserved = False
        self.__group = None
        self.__local = False
        self.__skip_fake_fs = False
        self.__inode_perfdata = False
        self.__stat_remote_fs = False
        self.__display_mountpoint = False
        self.__all = False
        self.__eregi_path = []
        self.__eregi_partition = None
        self.__ignore_eregi_path = []
        self.__ignore_eregi_partition = None
        self.__ereg_path = []
        self.__ereg_partition = None
        self.__ignore_ereg_path = []
        self.__ignore_ereg_partition = None
        self.__timeout = None
        self.__units = None
        self.__exclude_type = []
        self.__include_type = []
        self.set_check_interval('30m')
        self.add_service_group(ServiceGroup.create('disk'))

    def set_warning_units(self, number: int) -> T:
        self.__warning = str(number)
        return self

    def get_warning_units(self):
        if "%" in self.__warning:
            raise Exception("Try to get warning units but percentage is set in " + self.get_id())
        return int(self.__warning)

    def set_warning_percent(self, number: int) -> T:
        self.__warning = str(number) + '%'
        return self

    def get_warning_percent(self) -> int:

        if "%" not in self.__warning:
            raise Exception("Try to get warning percent but unit is set in " + self.get_id())

        return int(self.__warning.replace("%", ""))

    def get_critical_units(self):
        if "%" in self.__critical:
            raise Exception("Try to get critical units but percentage is set in " + self.get_id())
        return int(self.__critical)

    def set_critical_percent(self, number: int) -> T:
        self.__critical = str(number) + '%'
        return self

    def get_critical_percent(self) -> int:

        if "%" not in self.__critical:
            raise Exception("Try to get critical percent but unit is set in " + self.get_id())

        return int(self.__critical.replace("%", ""))

    def set_warning_inode_percent(self, number: int) -> T:
        self.__inode_warning = number
        return self

    def get_warning_inode_percent(self) -> int:
        return self.__inode_warning

    def set_critical_inode_percent(self, number: int) -> T:
        self.__inode_critical = number
        return self

    def get_critical_inode_percent(self) -> int:
        return self.__inode_critical

    def set_timeout(self, number: int) -> T:
        self.__timeout = number
        return self

    def get_timeout(self) -> int:
        return self.__timeout

    def set_clear_thresholds(self, enabled: bool) -> T:
        self.__clear_thresholds = enabled
        return self

    def get_clear_thresholds(self) -> bool:
        return self.__clear_thresholds

    def set_freespace_ignore_reserved(self, enabled: bool) -> T:
        self.__freespace_ignore_reserved = enabled
        return self

    def get_freespace_ignore_reserved(self) -> bool:
        return self.__freespace_ignore_reserved

    def set_errors_only(self, enabled: bool) -> T:
        self.__errors_only = enabled
        return self

    def get_errors_only(self) -> bool:
        return self.__errors_only

    def set_local(self, enabled: bool) -> T:
        self.__local = enabled
        return self

    def get_local(self) -> bool:
        return self.__local

    def set_all(self, enabled: bool) -> T:
        self.__all = enabled
        return self

    def get_all(self) -> bool:
        return self.__all

    def set_display_mountpoint(self, enabled: bool) -> T:
        self.__display_mountpoint = enabled
        return self

    def get_display_mountpoint(self) -> bool:
        return self.__display_mountpoint

    def set_stat_remote_fs(self, enabled: bool) -> T:
        self.__stat_remote_fs = enabled
        return self

    def get_stat_remote_fs(self) -> bool:
        return self.__stat_remote_fs

    def set_inode_perfdata(self, enabled: bool) -> T:
        self.__inode_perfdata = enabled
        return self

    def get_inode_perfdata(self) -> bool:
        return self.__inode_perfdata

    def set_skip_fake_fs(self, enabled: bool) -> T:
        self.__skip_fake_fs = enabled
        return self

    def get_skip_fake_fs(self) -> bool:
        return self.__skip_fake_fs

    def set_path(self, path: str) -> T:
        if path not in self.__path:
            self.__path.append(path)
        return self

    def remove_path(self, path: str) -> T:
        if path in self.__path:
            self.__path.remove(path)
        return self

    def get_path(self) -> typing.List[str]:
        return self.__path

    def set_exclude_device(self, exclude_device: typing.Union[str, None]) -> T:
        self.__exclude_device = exclude_device
        return self

    def get_exclude_device(self) -> typing.Union[str, None]:
        return self.__exclude_device

    def set_partition(self, partition: typing.Union[str, None]) -> T:
        self.__partition = partition
        return self

    def get_partition(self) -> typing.Union[str, None]:
        return self.__partition

    def set_group(self, group: typing.Union[str, None]) -> T:
        self.__group = group
        return self

    def get_group(self) -> typing.Union[str, None]:
        return self.__group

    def set_units(self, units: typing.Union[str, None]) -> T:
        self.__units = units
        return self

    def get_units(self) -> typing.Union[str, None]:
        return self.__units

    def set_include_type(self, include_type: str) -> T:
        if include_type not in self.__include_type:
            self.__include_type.append(include_type)
        return self

    def remove_include_type(self, include_type: str) -> T:
        if include_type in self.__include_type:
            self.__include_type.remove(include_type)
        return self

    def get_include_type(self) -> typing.List[str]:
        return self.__include_type

    def set_exclude_type(self, exclude_type: str) -> T:

        if exclude_type not in self.__exclude_type:
            self.__exclude_type.append(exclude_type)

        return self

    def remove_exclude_type(self, exclude_type: str) -> T:

        if exclude_type in self.__exclude_type:
            self.__exclude_type.remove(exclude_type)

        return self

    def get_exclude_type(self) -> typing.List[str]:
        return self.__exclude_type

    def set_eregi_path(self, eregi_path: str) -> T:
        if eregi_path not in self.__eregi_path:
            self.__eregi_path.append(eregi_path)
        return self

    def remove_eregi_path(self, eregi_path: str) -> T:
        if eregi_path in self.__eregi_path:
            self.__eregi_path.remove(eregi_path)
        return self

    def get_eregi_path(self) -> typing.List[str]:
        return self.__eregi_path

    def set_eregi_partition(self, eregi_partition: typing.Union[str, None]) -> T:
        self.__eregi_partition = eregi_partition
        return self

    def get_eregi_partition(self) -> typing.Union[str, None]:
        return self.__eregi_partition

    def set_ereg_path(self, ereg_path: str) -> T:
        if ereg_path not in self.__ereg_path:
            self.__ereg_path.append(ereg_path)

        return self

    def remove_ereg_path(self, ereg_path: str) -> T:
        if ereg_path in self.__ereg_path:
            self.__ereg_path.remove(ereg_path)

        return self

    def get_ereg_path(self) -> typing.List[str]:
        return self.__ereg_path

    def set_ereg_partition(self, ereg_partition: typing.Union[str, None]) -> T:
        self.__ereg_partition = ereg_partition
        return self

    def get_ereg_partition(self) -> typing.Union[str, None]:
        return self.__ereg_partition

    def set_ignore_eregi_path(self, ignore_eregi_path: str) -> T:
        if ignore_eregi_path not in self.__ignore_eregi_path:
            self.__ignore_eregi_path.append(ignore_eregi_path)
        return self

    def remove_ignore_eregi_path(self, ignore_eregi_path: str) -> T:
        if ignore_eregi_path in self.__ignore_eregi_path:
            self.__ignore_eregi_path.remove(ignore_eregi_path)
        return self

    def get_ignore_eregi_path(self) -> typing.List[str]:
        return self.__ignore_eregi_path

    def set_ignore_eregi_partition(self, ignore_eregi_partition: typing.Union[str, None]) -> T:
        self.__ignore_eregi_partition = ignore_eregi_partition
        return self

    def get_ignore_eregi_partition(self) -> typing.Union[str, None]:
        return self.__ignore_eregi_partition

    def set_ignore_ereg_path(self, ignore_ereg_path: str) -> T:

        if ignore_ereg_path not in self.__ignore_ereg_path:
            self.__ignore_ereg_path.append(ignore_ereg_path)
        return self

    def remove_ignore_ereg_path(self, ignore_ereg_path: str) -> T:

        if ignore_ereg_path in self.__ignore_ereg_path:
            self.__ignore_ereg_path.remove(ignore_ereg_path)
        return self

    def get_ignore_ereg_path(self) -> typing.List[str]:
        return self.__ignore_ereg_path

    def set_ignore_ereg_partition(self, ignore_ereg_partition: typing.Union[str, None]) -> T:
        self.__ignore_ereg_partition = ignore_ereg_partition
        return self

    def get_ignore_ereg_partition(self) -> typing.Union[str, None]:
        return self.__ignore_ereg_partition

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckDisk(id) \
                .add_service_group(ServiceGroup.create('disk').set_display_name('Disk'))
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckDisk):
            raise Exception('Id must be for an instance of CheckDisk but other instance is returned')

        if None is ConfigBuilder.get_command('nagios_plugins_disk'):
            DiskCommand.create('nagios_plugins_disk')

        return check

    def validate(self):
        pass
