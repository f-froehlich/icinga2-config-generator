#!/usr/bin/python3
# -*- coding: utf-8
import typing

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
from icinga2confgen.Commands.NagiosPlugins.DHCPCommand import DHCPCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='CheckDHCP')


class CheckDHCP(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckDHCP', 'nagios_plugins_dhcp')
        self.__server = None
        self.__requested_ip = None
        self.__timeout = 10
        self.__interface = None
        self.__mac = None
        self.__unicast = False
        self.add_service_group(ServiceGroup.create('dhcp'))
        self.add_service_group(ServiceGroup.create('network'))

    def set_server(self, server: typing.Union[str, None]) -> T:
        self.__server = server
        return self

    def get_server(self) -> typing.Union[str, None]:
        return self.__server

    def set_requested_ip(self, requested_ip: typing.Union[str, None]) -> T:
        self.__requested_ip = requested_ip
        return self

    def get_requested_ip(self) -> typing.Union[str, None]:
        return self.__requested_ip

    def set_timeout(self, timeout: typing.Union[int, None]) -> T:
        self.__timeout = timeout
        return self

    def get_timeout(self) -> typing.Union[int, None]:
        return self.__timeout

    def set_interface(self, interface: typing.Union[str, None]) -> T:
        self.__interface = interface
        return self

    def get_interface(self) -> typing.Union[str, None]:
        return self.__interface

    def set_mac(self, mac: typing.Union[str, None]) -> T:
        self.__mac = mac
        return self

    def get_mac(self) -> typing.Union[str, None]:
        return self.__mac

    def set_unicast(self, unicast: bool) -> T:
        self.__unicast = unicast
        return self

    def get_unicast(self) -> bool:
        return self.__unicast

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckDHCP(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckDHCP):
            raise Exception('Id must be for an instance of CheckDHCP but other instance is returned')

        if None is ConfigBuilder.get_command('nagios_plugins_dhcp'):
            DHCPCommand.create('nagios_plugins_dhcp')

        return check

    def validate(self):
        pass
