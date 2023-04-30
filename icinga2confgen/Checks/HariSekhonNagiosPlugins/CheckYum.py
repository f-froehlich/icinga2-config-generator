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

from __future__ import annotations

from ctypes import Union

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.HariSekhonNagiosPlugins.YumCommand import YumCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckYum(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckYum', 'hari_sekhon_nagios_plugins_yum')
        self.__timeout = 30
        self.__all_updates = False
        self.__warn_any_update = True
        self.__cache_only = False
        self.__no_warn_on_lock = False
        self.__config = None
        self.__repo_enabled = None
        self.__repo_disabled = None
        self.__plugin_disabled = None
        self.set_check_interval('15m')
        self.add_service_group(ServiceGroup.create('updates'))
        self.add_service_group(ServiceGroup.create('yum'))

    def set_timeout(self, seconds) -> CheckYum:
        ValueChecker.is_number(seconds)
        self.__timeout = seconds
        return self

    def get_timeout(self) -> int:
        return self.__timeout

    def set_all_updates(self, enabled: bool) -> CheckYum:
        self.__all_updates = enabled
        return self

    def get_all_updates(self) -> bool:
        return self.__all_updates

    def set_cache_only(self, enabled: bool) -> CheckYum:
        self.__cache_only = enabled
        return self

    def get_cache_only(self) -> bool:
        return self.__cache_only

    def set_no_warn_on_lock(self, enabled: bool) -> CheckYum:
        self.__no_warn_on_lock = enabled
        return self

    def get_no_warn_on_lock(self) -> bool:
        return self.__no_warn_on_lock

    def set_warn_any_update(self, enabled: bool) -> CheckYum:
        self.__warn_any_update = enabled
        return self

    def get_warn_any_update(self) -> bool:
        return self.__warn_any_update

    def set_yum_config(self, config: Union[str, None]) -> CheckYum:
        self.__config = config
        return self

    def get_yum_config(self) -> Union[str, None]:
        return self.__config

    def set_repo_enabled(self, repo_enabled: Union[str, None]) -> CheckYum:
        self.__repo_enabled = repo_enabled
        return self

    def get_repo_enabled(self) -> Union[str, None]:
        return self.__repo_enabled

    def set_repo_disabled(self, repo_disabled: Union[str, None]) -> CheckYum:
        self.__repo_disabled = repo_disabled
        return self

    def get_repo_disabled(self) -> Union[str, None]:
        return self.__repo_disabled

    def set_plugin_disabled(self, plugin_disabled: Union[str, None]) -> CheckYum:
        self.__plugin_disabled = plugin_disabled
        return self

    def get_plugin_disabled(self) -> Union[str, None]:
        return self.__plugin_disabled

    @staticmethod
    def create(id: str, force_create: bool = False) -> CheckYum:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckYum(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckYum):
            raise Exception('Id must be for an instance of CheckYum but other instance is returned')

        if None is ConfigBuilder.get_command('hari_sekhon_nagios_plugins_yum'):
            YumCommand.create('hari_sekhon_nagios_plugins_yum')

        return check

    def validate(self):
        pass
