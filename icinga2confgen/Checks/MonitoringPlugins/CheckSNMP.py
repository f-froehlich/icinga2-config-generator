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
from icinga2confgen.Commands.MonitoringPlugins.SNMPCommand import SNMPCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckSNMP(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckSNMP', 'snmp')
        self.__over_ipv4 = False
        self.__over_ipv6 = False
        self.__host = None
        self.__port = 161
        self.__snmp_getnext = False
        self.__protocol = None
        self.__context = None
        self.__seclevel = None
        self.__authproto = None
        self.__privproto = None
        self.__community = None
        self.__username = None
        self.__authpassword = None
        self.__privpassword = None
        self.__oids = None
        self.__delimiter = None
        self.__warning = None
        self.__critical = None
        self.__rate = False
        self.__rate_multiplier = None
        self.__offset = None
        self.__string = None
        self.__ereg = None
        self.__invert = False
        self.__label = None
        self.__units = None
        self.__output_delimiter = None
        self.__timeout = 10
        self.__retries = 2
        self.__perf_oids = False
        self.add_service_group(ServiceGroup.create('snmp'))
        self.add_service_group(ServiceGroup.create('network'))

    def set_over_ipv4(self, over_ipv4):
        ValueChecker.is_bool(over_ipv4)
        self.__over_ipv4 = over_ipv4
        return self

    def get_over_ipv4(self):
        return self.__over_ipv4

    def set_over_ipv6(self, over_ipv6):
        ValueChecker.is_bool(over_ipv6)
        self.__over_ipv6 = over_ipv6
        return self

    def get_over_ipv6(self):
        return self.__over_ipv6

    def set_host(self, host):
        ValueChecker.is_string(host)
        self.__host = host
        return self

    def get_host(self):
        return self.__host

    def set_port(self, port):
        ValueChecker.is_string(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    def set_snmp_getnext(self, snmp_getnext):
        ValueChecker.is_bool(snmp_getnext)
        self.__snmp_getnext = snmp_getnext
        return self

    def get_snmp_getnext(self):
        return self.__snmp_getnext

    def set_protocol(self, protocol):
        ValueChecker.is_string(protocol)
        self.__protocol = protocol
        return self

    def get_protocol(self):
        return self.__protocol

    def set_context(self, context):
        ValueChecker.is_string(context)
        self.__context = context
        return self

    def get_context(self):
        return self.__context

    def set_seclevel(self, seclevel):
        ValueChecker.is_string(seclevel)
        self.__seclevel = seclevel
        return self

    def get_seclevel(self):
        return self.__seclevel

    def set_authproto(self, authproto):
        ValueChecker.is_string(authproto)
        self.__authproto = authproto
        return self

    def get_authproto(self):
        return self.__authproto

    def set_privproto(self, privproto):
        ValueChecker.is_string(privproto)
        self.__privproto = privproto
        return self

    def get_privproto(self):
        return self.__privproto

    def set_community(self, community):
        ValueChecker.is_string(community)
        self.__community = community
        return self

    def get_community(self):
        return self.__community

    def set_username(self, username):
        ValueChecker.is_string(username)
        self.__username = username
        return self

    def get_username(self):
        return self.__username

    def set_authpassword(self, authpassword):
        ValueChecker.is_string(authpassword)
        self.__authpassword = authpassword
        return self

    def get_authpassword(self):
        return self.__authpassword

    def set_privpassword(self, privpassword):
        ValueChecker.is_string(privpassword)
        self.__privpassword = privpassword
        return self

    def get_privpassword(self):
        return self.__privpassword

    def set_oids(self, oids):
        ValueChecker.is_string(oids)
        self.__oids = oids
        return self

    def get_oids(self):
        return self.__oids

    def set_delimiter(self, delimiter):
        ValueChecker.is_string(delimiter)
        self.__delimiter = delimiter
        return self

    def get_delimiter(self):
        return self.__delimiter

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

    def set_rate(self, rate):
        ValueChecker.is_bool(rate)
        self.__rate = rate
        return self

    def get_rate(self):
        return self.__rate

    def set_rate_multiplier(self, rate_multiplier):
        ValueChecker.is_number(rate_multiplier)
        self.__rate_multiplier = rate_multiplier
        return self

    def get_rate_multiplier(self):
        return self.__rate_multiplier

    def set_offset(self, offset):
        ValueChecker.is_bool(offset)
        self.__offset = offset
        return self

    def get_offset(self):
        return self.__offset

    def set_string(self, string):
        ValueChecker.is_string(string)
        self.__string = string
        return self

    def get_string(self):
        return self.__string

    def set_ereg(self, ereg):
        ValueChecker.is_string(ereg)
        self.__ereg = ereg
        return self

    def get_ereg(self):
        return self.__ereg

    def set_invert(self, invert):
        ValueChecker.is_bool(invert)
        self.__invert = invert
        return self

    def get_invert(self):
        return self.__invert

    def set_label(self, label):
        ValueChecker.is_string(label)
        self.__label = label
        return self

    def get_label(self):
        return self.__label

    def set_units(self, units):
        ValueChecker.is_string(units)
        self.__units = units
        return self

    def get_units(self):
        return self.__units

    def set_output_delimiter(self, output_delimiter):
        ValueChecker.is_string(output_delimiter)
        self.__output_delimiter = output_delimiter
        return self

    def get_output_delimiter(self):
        return self.__output_delimiter

    def set_timeout(self, timeout):
        ValueChecker.is_number(timeout)
        self.__timeout = timeout
        return self

    def get_timeout(self):
        return self.__timeout

    def set_retries(self, retries):
        ValueChecker.is_number(retries)
        self.__retries = retries
        return self

    def get_retries(self):
        return self.__retries

    def set_perf_oids(self, perf_oids):
        ValueChecker.is_bool(perf_oids)
        self.__perf_oids = perf_oids
        return self

    def get_perf_oids(self):
        return self.__perf_oids

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckSNMP(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('snmp'):
            SNMPCommand.create('snmp')

        return check

    def validate(self):
        if None is self.__host:
            raise Exception('You have to specify a host for ' + self.get_id())
        if None is self.__oids:
            raise Exception('You have to specify a oids for ' + self.get_id())
