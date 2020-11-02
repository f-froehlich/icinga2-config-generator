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
from icinga2confgen.Checks.MonitoringPlugins.CheckPing import CheckPing
from icinga2confgen.Commands.MonitoringPlugins.PingCommand import PingCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckPing4(CheckPing):

    def __init__(self, id):
        CheckPing.__init__(self, id)
        self.add_service_group(ServiceGroup.create('ping'))
        self.add_service_group(ServiceGroup.create('network'))

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckPing4(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('ping'):
            PingCommand.create('ping')

        return check

    def get_custom_definitions(self):
        return [
            'vars.command_ping_v4 = true',
        ]

    def get_config(self):

        return Check.get_config(self)
