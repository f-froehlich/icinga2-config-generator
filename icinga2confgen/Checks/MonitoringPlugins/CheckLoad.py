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
from icinga2confgen.Commands.MonitoringPlugins.LoadCommand import LoadCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckLoad(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckLoad', 'load')
        self.__warning = '10,8,6'
        self.__critical = '15,12,9'
        self.__percpu = True
        self.__procs_to_show = None
        self.add_service_group(ServiceGroup.create('load'))
        self.add_service_group(ServiceGroup.create('system_health'))

    def set_warning(self, load1, load5, load15):
        ValueChecker.is_number(load1)
        ValueChecker.is_number(load5)
        ValueChecker.is_number(load15)
        self.__warning = str(load1) + ',' + str(load5) + ',' + str(load15)
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, load1, load5, load15):
        ValueChecker.is_number(load1)
        ValueChecker.is_number(load5)
        ValueChecker.is_number(load15)
        self.__critical = str(load1) + ',' + str(load5) + ',' + str(load15)
        return self

    def get_critical(self):
        return self.__critical

    def set_per_cpu(self, percpu):
        ValueChecker.is_bool(percpu)
        self.__percpu = percpu
        return self

    def get_per_cpu(self):
        return self.__percpu

    def set_procs_to_show(self, procs_to_show):
        ValueChecker.is_bool(procs_to_show)
        self.__procs_to_show = procs_to_show
        return self

    def get_procs_to_show(self):
        return self.__procs_to_show

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckLoad(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('load'):
            LoadCommand.create('load')

        return check

    def validate(self):
        pass
