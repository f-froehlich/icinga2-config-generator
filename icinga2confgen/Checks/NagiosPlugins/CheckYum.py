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
from icinga2confgen.Commands.NagiosPlugins.YumCommand import YumCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckYum(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckYum', 'yum')
        self.__timeout = 30
        self.__all_updates = False
        self.__warn_any_update = True
        self.__cache_only = False
        self.__no_warn_on_lock = False
        self.__config = None
        self.__repo_enabled = None
        self.__repo_disabled = None
        self.__plugin_disabled = None
        self.set_check_interval('1h')
        self.add_service_group(ServiceGroup.create('updates'))
        self.add_service_group(ServiceGroup.create('yum'))

    def set_timeout(self, seconds):
        ValueChecker.is_number(seconds)
        self.__timeout = seconds
        return self

    def get_timeout(self):
        return self.__timeout

    def set_all_updates(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__all_updates = enabled
        return self

    def get_all_updates(self):
        return self.__all_updates

    def set_cache_only(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__cache_only = enabled
        return self

    def get_cache_only(self):
        return self.__cache_only

    def set_no_warn_on_lock(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__no_warn_on_lock = enabled
        return self

    def get_no_warn_on_lock(self):
        return self.__no_warn_on_lock

    def set_warn_any_update(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__warn_any_update = enabled
        return self

    def get_warn_any_update(self):
        return self.__warn_any_update

    def set_yum_config(self, config):
        ValueChecker.is_string(config)
        self.__config = config
        return self

    def get_yum_config(self):
        return self.__config

    def set_repo_enabled(self, repo_enabled):
        ValueChecker.is_string(repo_enabled)
        self.__repo_enabled = repo_enabled
        return self

    def get_repo_enabled(self):
        return self.__repo_enabled

    def set_repo_disabled(self, repo_disabled):
        ValueChecker.is_string(repo_disabled)
        self.__repo_disabled = repo_disabled
        return self

    def get_repo_disabled(self):
        return self.__repo_disabled

    def set_plugin_disabled(self, plugin_disabled):
        ValueChecker.is_string(plugin_disabled)
        self.__plugin_disabled = plugin_disabled
        return self

    def get_plugin_disabled(self):
        return self.__plugin_disabled

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckYum(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('yum'):
            YumCommand.create('yum')

        return check

    def validate(self):
        pass
