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
from icinga2confgen.Commands.MonitoringPlugins.LDAPCommand import LDAPCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckLDAP(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckLDAP', 'ldap')
        self.__host = None
        self.__port = None
        self.__use_ipv4 = False
        self.__use_ipv6 = False
        self.__attr = None
        self.__base = None
        self.__dn = None
        self.__pass = None
        self.__starttls = False
        self.__ssl = True
        self.__protocol_v2 = False
        self.__protocol_v3 = False
        self.__warning = None
        self.__critical = None
        self.__warning_entries = None
        self.__critical_entries = None
        self.__timeout = 10
        self.add_service_group(ServiceGroup.create('ldap'))

    def set_host(self, host):
        ValueChecker.is_string(host)
        self.__host = host
        return self

    def get_host(self):
        return self.__host

    def set_port(self, port):
        ValueChecker.is_number(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    def set_use_ipv4(self, use_ipv4):
        ValueChecker.is_bool(use_ipv4)
        self.__use_ipv4 = use_ipv4
        return self

    def get_use_ipv4(self):
        return self.__use_ipv4

    def set_use_ipv6(self, use_ipv6):
        ValueChecker.is_bool(use_ipv6)
        self.__use_ipv6 = use_ipv6
        return self

    def get_use_ipv6(self):
        return self.__use_ipv6

    def set_attr(self, attr):
        ValueChecker.is_string(attr)
        self.__attr = attr
        return self

    def get_attr(self):
        return self.__attr

    def set_base(self, base):
        ValueChecker.is_string(base)
        self.__base = base
        return self

    def get_base(self):
        return self.__base

    def set_dn(self, dn):
        ValueChecker.is_string(dn)
        self.__dn = dn
        return self

    def get_dn(self):
        return self.__dn

    def set_pass(self, passwd):
        ValueChecker.is_string(passwd)
        self.__pass = passwd
        return self

    def get_pass(self):
        return self.__pass

    def set_starttls(self, starttls):
        ValueChecker.is_bool(starttls)
        self.__starttls = starttls
        return self

    def get_starttls(self):
        return self.__starttls

    def set_ssl(self, ssl):
        ValueChecker.is_bool(ssl)
        self.__ssl = ssl
        return self

    def get_ssl(self):
        return self.__ssl

    def set_protocol_v2(self, protocol_v2):
        ValueChecker.is_bool(protocol_v2)
        self.__protocol_v2 = protocol_v2
        return self

    def get_protocol_v2(self):
        return self.__protocol_v2

    def set_protocol_v3(self, protocol_v3):
        ValueChecker.is_bool(protocol_v3)
        self.__protocol_v3 = protocol_v3
        return self

    def get_protocol_v3(self):
        return self.__protocol_v3

    def set_warning(self, warning):
        ValueChecker.is_string(warning)
        self.__warning = warning
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, critical):
        ValueChecker.is_string(critical)
        self.__critical = critical
        return self

    def get_critical(self):
        return self.__critical

    def set_warning_entries(self, warning_entries):
        ValueChecker.is_number(warning_entries)
        self.__warning_entries = warning_entries
        return self

    def get_warning_entries(self):
        return self.__warning_entries

    def set_critical_entries(self, critical_entries):
        ValueChecker.is_number(critical_entries)
        self.__critical_entries = critical_entries
        return self

    def get_critical_entries(self):
        return self.__critical_entries

    def set_timeout(self, timeout):
        ValueChecker.is_number(timeout)
        self.__timeout = timeout
        return self

    def get_timeout(self):
        return self.__timeout

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckLDAP(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('ldap'):
            LDAPCommand.create('ldap')

        return check

    def validate(self):
        if None is self.__base:
            raise Exception('You have to specify a base dn for ' + self.get_id())
        if None is self.__host:
            raise Exception('You have to specify a host for ' + self.get_id())
