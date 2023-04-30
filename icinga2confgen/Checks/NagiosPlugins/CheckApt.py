#!/usr/bin/python3
# -*- coding: utf-8
import typing

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.NagiosPlugins.AptCommand import AptCommand
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

T = typing.TypeVar('T', bound='CheckApt')


class CheckApt(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckApt', 'nagios_plugins_apt')
        self.__timeout = 10
        self.__upgrade = None
        self.__dist_upgrade = None
        self.__no_upgrade = None
        self.__include = None
        self.__exclude = None
        self.__critical = None
        self.__only_critical = False
        self.__packages_warning = None
        self.__update = None
        self.set_check_interval('15m')
        self.add_service_group(ServiceGroup.create('updates'))
        self.add_service_group(ServiceGroup.create('apt'))

    def set_timeout(self, seconds: int) -> T:
        self.__timeout = seconds
        return self

    def get_timeout(self) -> int:
        return self.__timeout

    def set_upgrade(self, opts: typing.Union[str, None]) -> T:
        self.__upgrade = opts
        return self

    def get_upgrade(self) -> typing.Union[str, None]:
        return self.__upgrade

    def set_dist_upgrade(self, opts: typing.Union[str, None]) -> T:
        self.__dist_upgrade = opts
        return self

    def get_dist_upgrade(self) -> typing.Union[str, None]:
        return self.__dist_upgrade

    def set_no_upgrade(self, opts: typing.Union[str, None]) -> T:
        self.__no_upgrade = opts
        return self

    def get_no_upgrade(self) -> typing.Union[str, None]:
        return self.__no_upgrade

    def set_include(self, expr: typing.Union[str, None]) -> T:
        self.__include = expr
        return self

    def get_include(self) -> typing.Union[str, None]:
        return self.__include

    def set_exclude(self, expr: typing.Union[str, None]) -> T:
        self.__exclude = expr
        return self

    def get_exclude(self) -> typing.Union[str, None]:
        return self.__exclude

    def set_critical(self, expr: typing.Union[str, None]) -> T:
        self.__critical = expr
        return self

    def get_critical(self) -> typing.Union[str, None]:
        return self.__critical

    def set_only_critical(self, enable: bool) -> T:
        self.__only_critical = enable
        return self

    def get_only_critical(self) -> bool:
        return self.__only_critical

    def set_packages_warning(self, count: typing.Union[int, None]) -> T:
        self.__packages_warning = count
        return self

    def get_packages_warning(self) -> typing.Union[int, None]:
        return self.__packages_warning

    def set_update(self, opts: typing.Union[str, None]) -> T:
        self.__update = opts
        return self

    def get_update(self) -> typing.Union[str, None]:
        return self.__update

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckApt(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckApt):
            raise Exception('Id must be for an instance of CheckApt but other instance is returned')

        if None is ConfigBuilder.get_command('nagios_plugins_apt'):
            AptCommand.create('nagios_plugins_apt')

        return check

    def validate(self):
        pass
