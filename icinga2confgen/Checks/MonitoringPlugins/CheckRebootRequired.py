#!/usr/bin/python3
# -*- coding: utf-8
import typing

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.MonitoringPlugins.RebootRequiredCommand import RebootRequiredCommand
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
T = typing.TypeVar('T', bound='CheckRebootRequired')


class CheckRebootRequired(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckRebootRequired', 'monitoring_plugins_reboot_required')
        self.__exit_critical = False
        self.__ignore_scheduled = True
        self.set_check_interval('15m')
        self.add_service_group(ServiceGroup.create('reboot'))
        self.add_service_group(ServiceGroup.create('system_health'))

    def set_exit_critical(self, exit_critical: bool) -> T:
        self.__exit_critical = exit_critical
        return self

    def get_exit_critical(self) -> bool:
        return self.__exit_critical

    def set_ignore_scheduled(self, ignore_scheduled: bool) -> T:
        self.__ignore_scheduled = ignore_scheduled
        return self

    def get_ignore_scheduled(self) -> bool:
        return self.__ignore_scheduled

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckRebootRequired(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckRebootRequired):
            raise Exception('Id must be for an instance of CheckRebootRequired but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_reboot_required'):
            RebootRequiredCommand.create('monitoring_plugins_reboot_required')

        return check

    def validate(self):
        pass
