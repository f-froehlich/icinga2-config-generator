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

from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class PluginDirs:

    def __init__(self):
        self.__nagios_plugin_dir = '/usr/lib/nagios/plugins/'
        self.__monitoring_plugin_dir = '/usr/local/monitoring/monitoring_plugins/'
        self.__harik_sekhon_plugin_dir = '/usr/local/monitoring/harik_sekhon/'

    def set_nagios_plugindir(self, dir):
        ValueChecker.is_string(dir)
        self.__nagios_plugin_dir = dir
        return self

    def get_nagios_plugindir(self):
        return self.__nagios_plugin_dir

    def set_monitoring_plugindir(self, dir):
        ValueChecker.is_string(dir)
        self.__monitoring_plugin_dir = dir
        return self

    def get_monitoring_plugindir(self):
        return self.__monitoring_plugin_dir

    def set_harik_sekhon_plugindir(self, dir):
        ValueChecker.is_string(dir)
        self.__harik_sekhon_plugin_dir = dir
        return self

    def get_harik_sekhon_plugindir(self):
        return self.__harik_sekhon_plugin_dir

    def get_config(self):
        config = ValueMapper.parse_var('vars.nagios_plugin_dir', self.__nagios_plugin_dir)
        config += ValueMapper.parse_var('vars.monitoring_plugin_dir', self.__monitoring_plugin_dir)
        config += ValueMapper.parse_var('vars.harik_sekhon_plugin_dir', self.__harik_sekhon_plugin_dir)
        return config
