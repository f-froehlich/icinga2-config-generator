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

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Dependency.Dependency import Dependency
from icinga2confgen.ValueChecker import ValueChecker


class ServerDependency(Dependency):

    def __init__(self, id):
        Dependency.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)

        dependency = None if force_create else ConfigBuilder.get_dependency(id)
        if None is dependency:
            dependency = ServerDependency(id)
            ConfigBuilder.add_dependency(id, dependency)

        return dependency

    def get_allowed_states(self):
        return ['Up', 'Down']

    def get_default_states(self):
        return ['Up']

    def get_config(self):
        self.validate()

        config = Dependency.get_config(self)
        config += 'apply Dependency "hostdependency_' + self.__id + '" to Host {\n'
        config += '  import "dependency_' + self.get_id() + '"\n'
        config += '  assign where "dependency_' + self.__id + '" in host.vars.dependencies\n'
        config += '}\n'

        return config
