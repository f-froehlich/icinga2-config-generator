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
from __future__ import annotations

from typing import Union

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.ClaudioKuenzler.ESXIHardwareCommand import ESXIHardwareCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckESXIHardware(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckESXIHardware', 'claudio_kuenzler_esxi_hardware')
        self.__host: Union[str, None] = None
        self.__user: Union[str, None] = None
        self.__password: Union[str, None] = None

        self.__vendor: str = 'dell'
        self.__sslproto: Union[str, None] = None
        self.__ignore: Union[str, None] = None
        self.__port: int = 5989
        self.__html: Union[str, None] = None

        self.__regex: bool = False
        self.__perfdata: bool = True
        self.__nopower: bool = False
        self.__novolts: bool = False
        self.__nocurrent: bool = False
        self.__notemp: bool = False
        self.__nofan: bool = False
        self.__nolcd: bool = False
        self.__nointrusion: bool = False

        self.add_service_group(ServiceGroup.create('esxi_hardware'))

    def set_host(self, host: str) -> CheckESXIHardware:
        self.__host = host
        return self

    def get_host(self) -> Union[str, None]:
        return self.__host

    def set_user(self, user: str) -> CheckESXIHardware:
        self.__user = user
        return self

    def get_user(self) -> Union[str, None]:
        return self.__user

    def set_password(self, password: str) -> CheckESXIHardware:
        self.__password = password
        return self

    def get_password(self) -> Union[str, None]:
        return self.__password

    def set_vendor(self, vendor: str) -> CheckESXIHardware:
        self.__vendor = vendor
        return self

    def get_vendor(self) -> str:
        return self.__vendor

    def set_sslproto(self, sslproto: str) -> CheckESXIHardware:
        protos = ['SSLv2', 'SSLv3', 'TLSv1.0', 'TLSv1.1', 'TLSv1.2', 'TLSv1.3']
        if sslproto not in protos:
            raise Exception('Proto must be in ' + ', '.join(protos))

        self.__sslproto = sslproto
        return self

    def get_sslproto(self) -> Union[str, None]:
        return self.__sslproto

    def set_ignore(self, ignore: str) -> CheckESXIHardware:
        self.__ignore = ignore
        return self

    def get_ignore(self) -> Union[str, None]:
        return self.__ignore

    def set_port(self, port: int) -> CheckESXIHardware:
        self.__port = port
        return self

    def get_port(self) -> int:
        return self.__port

    def set_html(self, lang: Union[str, None]) -> CheckESXIHardware:
        self.__html = lang
        return self

    def get_html(self) -> Union[str, None]:
        return self.__html

    def set_regex(self, enabled: bool) -> CheckESXIHardware:
        self.__regex = enabled
        return self

    def get_regex(self) -> bool:
        return self.__regex

    def set_perfdata(self, enabled: bool) -> CheckESXIHardware:
        self.__perfdata = enabled
        return self

    def get_perfdata(self) -> bool:
        return self.__perfdata

    def set_nopower(self, enabled: bool) -> CheckESXIHardware:
        self.__nopower = enabled
        return self

    def get_nopower(self) -> bool:
        return self.__nopower

    def set_novolts(self, enabled: bool) -> CheckESXIHardware:
        self.__novolts = enabled
        return self

    def get_novolts(self) -> bool:
        return self.__novolts

    def set_nocurrent(self, enabled: bool) -> CheckESXIHardware:
        self.__nocurrent = enabled
        return self

    def get_nocurrent(self) -> bool:
        return self.__nocurrent

    def set_notemp(self, enabled: bool) -> CheckESXIHardware:
        self.__notemp = enabled
        return self

    def get_notemp(self) -> bool:
        return self.__notemp

    def set_nofan(self, enabled: bool) -> CheckESXIHardware:
        self.__nofan = enabled
        return self

    def get_nofan(self) -> bool:
        return self.__nofan

    def set_nolcd(self, enabled: bool) -> CheckESXIHardware:
        self.__nolcd = enabled
        return self

    def get_nolcd(self) -> bool:
        return self.__nolcd

    def set_nointrusion(self, enabled: bool) -> CheckESXIHardware:
        self.__nointrusion = enabled
        return self

    def get_nointrusion(self) -> bool:
        return self.__nointrusion

    def validate(self):

        if None is self.__host:
            raise Exception('Host must be set')

        if None is self.__user:
            raise Exception('User must be set')

        if None is self.__password:
            raise Exception('Password must be set')

    @staticmethod
    def create(id: str, force_create: bool = False) -> CheckESXIHardware:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckESXIHardware(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckESXIHardware):
            raise Exception('Id must be for an instance of CheckESXIHardware but other instance is returned')

        if None is ConfigBuilder.get_command('claudio_kuenzler_esxi_hardware'):
            ESXIHardwareCommand.create('claudio_kuenzler_esxi_hardware')

        return check
