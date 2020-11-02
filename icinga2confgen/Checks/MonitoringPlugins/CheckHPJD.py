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
from icinga2confgen.Commands.MonitoringPlugins.HPJDCommand import HPJDCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckHPJD(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckHPJD', 'hpjd')
        self.__host = None
        self.__community = None
        self.__paper_check = False
        self.__port = None
        self.add_service_group(ServiceGroup.create('hpjd'))

    def set_host(self, host):
        ValueChecker.is_string(host)
        self.__host = host
        return self

    def get_host(self):
        return self.__host

    def set_community(self, community):
        ValueChecker.is_string(community)
        self.__community = community
        return self

    def get_community(self):
        return self.__community

    def set_paper_check(self, paper_check):
        ValueChecker.is_bool(paper_check)
        self.__paper_check = paper_check
        return self

    def get_paper_check(self):
        return self.__paper_check

    def set_port(self, port):
        ValueChecker.is_string(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckHPJD(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('hpjd'):
            HPJDCommand.create('hpjd')

        return check

    def validate(self):
        if None is self.__host:
            raise Exception('You have to specify a host for ' + self.get_id())
