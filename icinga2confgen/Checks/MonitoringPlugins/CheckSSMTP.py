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
from icinga2confgen.Commands.MonitoringPlugins.SSMTPCommand import SSMTPCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckSSMTP(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckSSMTP', 'ssmtp')
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
        self.add_service_group(ServiceGroup.create('smtp'))
        self.add_service_group(ServiceGroup.create('mail'))

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

    def set_ipv4(self, ipv4):
        ValueChecker.is_bool(ipv4)
        self.__ipv4 = ipv4
        return self

    def get_ipv4(self):
        return self.__ipv4

    def set_ipv6(self, ipv6):
        ValueChecker.is_bool(ipv6)
        self.__ipv6 = ipv6
        return self

    def get_ipv6(self):
        return self.__ipv6

    def set_escape(self, escape):
        ValueChecker.is_bool(escape)
        self.__escape = escape
        return self

    def get_escape(self):
        return self.__escape

    def set_send(self, send):
        ValueChecker.is_string(send)
        self.__send = send
        return self

    def get_send(self):
        return self.__send

    def set_expect(self, expect):
        ValueChecker.is_string(expect)
        self.__expect = expect
        return self

    def get_expect(self):
        return self.__expect

    def set_all(self, all):
        ValueChecker.is_bool(all)
        self.__all = all
        return self

    def get_all(self):
        return self.__all

    def set_quit(self, quit):
        ValueChecker.is_string(quit)
        self.__quit = quit
        return self

    def get_quit(self):
        return self.__quit

    def set_refuse_state(self, refuse_state):
        ValueChecker.is_string(refuse_state)
        self.__refuse_state = refuse_state
        return self

    def get_refuse_state(self):
        return self.__refuse_state

    def set_mismatch_state(self, mismatch_state):
        ValueChecker.is_string(mismatch_state)
        self.__mismatch_state = mismatch_state
        return self

    def get_mismatch_state(self):
        return self.__mismatch_state

    def set_jail(self, jail):
        ValueChecker.is_bool(jail)
        self.__jail = jail
        return self

    def get_jail(self):
        return self.__jail

    def set_maxbytes(self, maxbytes):
        ValueChecker.is_number(maxbytes)
        self.__maxbytes = maxbytes
        return self

    def get_maxbytes(self):
        return self.__maxbytes

    def set_delay(self, delay):
        ValueChecker.is_number(delay)
        self.__delay = delay
        return self

    def get_delay(self):
        return self.__delay

    def set_cert_warning(self, cert_warning):
        ValueChecker.is_number(cert_warning)
        self.__cert_warning = cert_warning
        return self

    def get_cert_warning(self):
        return self.__cert_warning

    def set_cert_critical(self, cert_critical):
        ValueChecker.is_number(cert_critical)
        self.__cert_critical = cert_critical
        return self

    def get_cert_critical(self):
        return self.__cert_critical

    def set_cert(self, cert):
        ValueChecker.is_bool(cert)
        self.__cert = cert
        return self

    def get_cert(self):
        return self.__cert

    def set_use_ssl(self, use_ssl):
        ValueChecker.is_bool(use_ssl)
        self.__use_ssl = use_ssl
        return self

    def get_use_ssl(self):
        return self.__use_ssl

    def set_sni(self, sni):
        ValueChecker.is_string(sni)
        self.__sni = sni
        return self

    def get_sni(self):
        return self.__sni

    def set_warning_time(self, warning_time):
        ValueChecker.is_number(warning_time)
        self.__warning_time = warning_time
        return self

    def get_warning_time(self):
        return self.__warning_time

    def set_critical_time(self, critical_time):
        ValueChecker.is_number(critical_time)
        self.__critical_time = critical_time
        return self

    def get_critical_time(self):
        return self.__critical_time

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
            check = CheckSSMTP(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('ssmtp'):
            SSMTPCommand.create('ssmtp')

        return check

    def validate(self):
        if None is self.__host:
            raise Exception('You have to specify a host for ' + self.get_id())
        if None is self.__port:
            raise Exception('You have to specify a port for ' + self.get_id())
