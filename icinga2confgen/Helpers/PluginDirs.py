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

from typing import Union

from icinga2confgen.ValueMapper import ValueMapper


class PluginDirs:

    def __init__(self, is_check: bool = False):
        if not is_check:
            self.__nagios_plugin_dir = '/usr/lib/nagios/plugins/'
            self.__monitoring_plugin_dir = '/usr/local/monitoring/monitoring_plugins/'
            self.__harik_sekhon_plugin_dir = '/usr/local/monitoring/harik_sekhon/'
            self.__claudio_kuenzler_plugin_dir = '/usr/local/monitoring/claudiokuenzler/'
            self.__other_plugin_dir = '/opt/monitoring/'

        else:
            self.__nagios_plugin_dir = None
            self.__monitoring_plugin_dir = None
            self.__harik_sekhon_plugin_dir = None
            self.__claudio_kuenzler_plugin_dir = None
            self.__other_plugin_dir = None

    def set_nagios_plugindir(self, dir: str) -> PluginDirs:
        self.__nagios_plugin_dir = dir
        return self

    def get_nagios_plugindir(self) -> Union[str, None]:
        return self.__nagios_plugin_dir

    def set_other_plugindir(self, dir: str) -> PluginDirs:
        self.__other_plugin_dir = dir
        return self

    def get_other_plugindir(self) -> Union[str, None]:
        return self.__other_plugin_dir

    def set_claudio_kuenzler_plugindir(self, dir) -> PluginDirs:
        self.__claudio_kuenzler_plugin_dir = dir
        return self

    def get_claudio_kuenzler_plugindir(self) -> Union[str, None]:
        return self.__claudio_kuenzler_plugin_dir

    def set_monitoring_plugindir(self, dir: str) -> PluginDirs:
        self.__monitoring_plugin_dir = dir
        return self

    def get_monitoring_plugindir(self) -> Union[str, None]:
        return self.__monitoring_plugin_dir

    def set_harik_sekhon_plugindir(self, dir: str) -> PluginDirs:
        self.__harik_sekhon_plugin_dir = dir
        return self

    def get_harik_sekhon_plugindir(self) -> Union[str, None]:
        return self.__harik_sekhon_plugin_dir

    def get_config(self) -> str:
        config = ValueMapper.parse_var('vars.nagios_plugin_dir', self.__nagios_plugin_dir)
        config += ValueMapper.parse_var('vars.monitoring_plugin_dir', self.__monitoring_plugin_dir)
        config += ValueMapper.parse_var('vars.harik_sekhon_plugin_dir', self.__harik_sekhon_plugin_dir)
        config += ValueMapper.parse_var('vars.other_plugin_dir', self.__other_plugin_dir)
        config += ValueMapper.parse_var('vars.claudio_kuenzler_plugin_dir', self.__claudio_kuenzler_plugin_dir)
        return config
