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

from Checks.Check import Check
from Commands.MonitoringPlugins.LogCommand import LogCommand
from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker


class CheckLog(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckLog', 'log')
        self.__file = None
        self.__oldfile = None
        self.__query = None
        
    def set_file(self, file):
        ValueChecker.is_string(file)
        self.__file = file
        return self

    def get_file(self):
        return self.__file
        
    def set_oldfile(self, oldfile):
        ValueChecker.is_string(oldfile)
        self.__oldfile = oldfile
        return self

    def get_oldfile(self):
        return self.__oldfile

    def set_query(self, query):
        ValueChecker.is_string(query)
        self.__query = query
        return self

    def get_query(self):
        return self.__query


    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckLog(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('log'):
            LogCommand.create('log')

        return check
