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


class ScriptDirs:

    def __init__(self):
        self.__icinga_script_dir = '/etc/icinga2/scripts/'
        self.__monitoring_script_dir = '/usr/local/monitoring/monitoring_scripts/'

    def set_icinga_scriptdir(self, dir):
        ValueChecker.is_string(dir)
        self.__icinga_script_dir = dir
        return self

    def get_icinga_scriptdir(self):
        return self.__icinga_script_dir

    def set_monitoring_scriptdir(self, dir):
        ValueChecker.is_string(dir)
        self.__icinga_script_dir = dir
        return self

    def get_monitoring_scriptdir(self):
        return self.__monitoring_script_dir

    def get_config(self):
        config = ValueMapper.parse_var('vars.icinga_script_dir', self.__icinga_script_dir)
        config += ValueMapper.parse_var('vars.monitoring_script_dir', self.__monitoring_script_dir)
        return config
