#!/usr/bin/python3
# -*- coding: utf-8
import typing

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.MonitoringPlugins.PathExistsCommand import PathExistsCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

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

T = typing.TypeVar('T', bound='CheckPathExists')


class CheckPathExists(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckPathExists', 'monitoring_plugins_path_exists')
        self.__file = None
        self.__dir = None
        self.__invert = False
        self.add_service_group(ServiceGroup.create('path_exists'))

    def set_file(self, file: str) -> T:
        self.__file = file
        return self

    def get_file(self) -> typing.Union[str, None]:
        return self.__file

    def set_dir(self, dir: str) -> T:
        self.__dir = dir
        return self

    def get_dir(self) -> typing.Union[str, None]:
        return self.__dir

    def set_invert(self, invert: bool) -> T:
        self.__invert = invert
        return self

    def get_invert(self) -> bool:
        return self.__invert

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckPathExists(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckPathExists):
            raise Exception('Id must be for an instance of CheckPathExist but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_path_exists'):
            PathExistsCommand.create('monitoring_plugins_path_exists')

        return check

    def validate(self):
        if None is self.__file and None is self.__dir:
            raise Exception('You have to specify a file or dir for ' + self.get_id())
