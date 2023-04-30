#!/usr/bin/python3
# -*- coding: utf-8
import typing

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.NagiosPlugins.ClamdCommand import ClamdCommand
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

T = typing.TypeVar('T', bound='CheckClamd')


class CheckClamd(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckClamd', 'nagios_plugins_clamd')
        self.__host = None
        self.__port = None
        self.__ipv4 = False
        self.__ipv6 = False
        self.__escape = False
        self.__send = None
        self.__expect = None
        self.__all = False
        self.__quit = None
        self.__refuse_state = None
        self.__mismatch_state = None
        self.__jail = False
        self.__maxbytes = None
        self.__delay = None
        self.__cert_warning = 29
        self.__cert_critical = 15
        self.__cert = True
        self.__use_ssl = False
        self.__sni = None
        self.__warning_time = None
        self.__critical_time = None
        self.__timeout = 10
        self.add_service_group(ServiceGroup.create('clamd'))

    def set_host(self, host: str) -> T:
        self.__host = host
        return self

    def get_host(self) -> typing.Union[str, None]:
        return self.__host

    def set_port(self, port: int) -> T:
        self.__port = port
        return self

    def get_port(self) -> typing.Union[int, None]:
        return self.__port

    def set_ipv4(self, ipv4: bool) -> T:
        self.__ipv4 = ipv4
        return self

    def get_ipv4(self) -> bool:
        return self.__ipv4

    def set_ipv6(self, ipv6: bool) -> T:
        self.__ipv6 = ipv6
        return self

    def get_ipv6(self) -> bool:
        return self.__ipv6

    def set_escape(self, escape: bool) -> T:
        self.__escape = escape
        return self

    def get_escape(self) -> bool:
        return self.__escape

    def set_send(self, send: typing.Union[str, None]) -> T:
        self.__send = send
        return self

    def get_send(self) -> typing.Union[str, None]:
        return self.__send

    def set_expect(self, expect: typing.Union[str, None]) -> T:
        self.__expect = expect
        return self

    def get_expect(self) -> typing.Union[str, None]:
        return self.__expect

    def set_all(self, all: bool) -> T:
        self.__all = all
        return self

    def get_all(self) -> bool:
        return self.__all

    def set_quit(self, quit: typing.Union[str, None]) -> T:
        self.__quit = quit
        return self

    def get_quit(self) -> typing.Union[str, None]:
        return self.__quit

    def set_refuse_state(self, refuse_state: typing.Union[str, None]) -> T:
        self.__refuse_state = refuse_state
        return self

    def get_refuse_state(self) -> typing.Union[str, None]:
        return self.__refuse_state

    def set_mismatch_state(self, mismatch_state: typing.Union[str, None]) -> T:
        self.__mismatch_state = mismatch_state
        return self

    def get_mismatch_state(self) -> typing.Union[str, None]:
        return self.__mismatch_state

    def set_jail(self, jail: bool) -> T:
        self.__jail = jail
        return self

    def get_jail(self) -> bool:
        return self.__jail

    def set_maxbytes(self, maxbytes: typing.Union[int, None]) -> T:
        self.__maxbytes = maxbytes
        return self

    def get_maxbytes(self) -> typing.Union[int, None]:
        return self.__maxbytes

    def set_delay(self, delay: typing.Union[int, None]) -> T:
        self.__delay = delay
        return self

    def get_delay(self) -> typing.Union[int, None]:
        return self.__delay

    def set_cert_warning(self, cert_warning: int) -> T:
        self.__cert_warning = cert_warning
        return self

    def get_cert_warning(self) -> int:
        return self.__cert_warning

    def set_cert_critical(self, cert_critical: int) -> T:
        self.__cert_critical = cert_critical
        return self

    def get_cert_critical(self) -> int:
        return self.__cert_critical

    def set_cert(self, cert: bool) -> T:
        self.__cert = cert
        return self

    def get_cert(self) -> bool:
        return self.__cert

    def set_use_ssl(self, use_ssl: bool) -> T:
        self.__use_ssl = use_ssl
        return self

    def get_use_ssl(self) -> bool:
        return self.__use_ssl

    def set_sni(self, sni: typing.Union[str, None]) -> T:
        self.__sni = sni
        return self

    def get_sni(self) -> T:
        return self.__sni

    def set_warning_time(self, warning_time: typing.Union[int, None]) -> T:
        self.__warning_time = warning_time
        return self

    def get_warning_time(self) -> typing.Union[int, None]:
        return self.__warning_time

    def set_critical_time(self, critical_time: typing.Union[int, None]) -> T:
        self.__critical_time = critical_time
        return self

    def get_critical_time(self) -> typing.Union[int, None]:
        return self.__critical_time

    def set_timeout(self, timeout: int) -> T:
        self.__timeout = timeout
        return self

    def get_timeout(self) -> int:
        return self.__timeout

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckClamd(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckClamd):
            raise Exception('Id must be for an instance of CheckClamd but other instance is returned')

        if None is ConfigBuilder.get_command('nagios_plugins_clamd'):
            ClamdCommand.create('nagios_plugins_clamd')

        return check

    def validate(self):
        if None is self.__host:
            raise Exception('You have to specify a host for ' + self.get_id())
        if None is self.__port:
            raise Exception('You have to specify a port for ' + self.get_id())
