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
from icinga2confgen.Commands.MonitoringPlugins.SensorsCommand import SensorsCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckSensors(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckSensors', 'sensors')
        self.add_service_group(ServiceGroup.create('sensors'))
        self.add_service_group(ServiceGroup.create('system_health'))

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckSensors(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('sensors'):
            SensorsCommand.create('sensors')

        return check

    def validate(self):
        pass
