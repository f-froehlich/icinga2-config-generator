#!/usr/bin/python3
# -*- coding: utf-8
import typing

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.MonitoringPlugins.DNSSECExpireCommand import DNSSECExpireCommand
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

T = typing.TypeVar('T', bound='CheckDNSSECExpire')


class CheckDNSSECExpire(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckDNSSECExpire', 'monitoring_plugins_dnssec_expiry')
        self.__warning = 10
        self.__critical = 5
        self.__dns_domains = []
        self.__resolver = '1.1.1.1'
        self.__ignore_root = True
        self.__ignore_tld = True
        self.__timeout = 30
        self.set_check_interval('15m')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('dns'))
        self.add_service_group(ServiceGroup.create('dnssec'))

    def set_warning(self, warning:int) -> T:
        self.__warning = warning
        return self

    def get_warning(self) -> int:
        return self.__warning

    def set_critical(self, critical : int) -> T:
        self.__critical = critical
        return self

    def get_critical(self) -> int:
        return self.__critical

    def set_timeout(self, timeout: int) -> T:
        self.__timeout = timeout
        return self

    def get_timeout(self) -> int:
        return self.__timeout

    def add_dns_domain(self, domain: str) -> T:
        if domain not in self.__dns_domains:
            self.__dns_domains.append(domain)
        return self

    def remove_dns_domain(self, domain: str) -> T:
        if domain in self.__dns_domains:
            self.__dns_domains.remove(domain)
        return self

    def get_dns_domains(self) -> typing.List[str]:
        return self.__dns_domains

    def set_resolver(self, resolver: str) -> T:
        self.__resolver = resolver
        return self

    def get_resolver(self) -> str:
        return self.__resolver

    def set_ignore_root(self, ignore_root:bool) -> T:
        self.__ignore_root = ignore_root
        return self

    def get_ignore_root(self) -> bool:
        return self.__ignore_root

    def set_ignore_tld(self, ignore_tld:bool) -> T:
        self.__ignore_tld = ignore_tld
        return self

    def get_ignore_tld(self) -> bool:
        return self.__ignore_tld

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckDNSSECExpire(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckDNSSECExpire):
            raise Exception('Id must be for an instance of CheckDNSSECExpire but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_dnssec_expiry'):
            DNSSECExpireCommand.create('monitoring_plugins_dnssec_expiry')

        return check

    def validate(self):
        pass
