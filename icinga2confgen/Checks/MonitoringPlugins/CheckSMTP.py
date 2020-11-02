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
from icinga2confgen.Commands.MonitoringPlugins.SMTPCommand import SMTPCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckSMTP(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckSMTP', 'smtp')
        self.__host = None
        self.__port = 25
        self.__use_ipv4 = False
        self.__use_ipv6 = False
        self.__expect = None
        self.__command = None
        self.__response = None
        self.__from = None
        self.__fqdn = None
        self.__cert_warning = 29
        self.__cert_critical = 15
        self.__cert = True
        self.__starttls = False
        self.__authtype = None
        self.__authuser = None
        self.__authpass = None
        self.__ignore_quit_failure = False
        self.__warning = 5
        self.__critical = 9
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

    def set_expect(self, expect):
        ValueChecker.is_string(expect)
        self.__expect = expect
        return self

    def get_expect(self):
        return self.__expect

    def set_command(self, command):
        ValueChecker.is_string(command)
        self.__command = command
        return self

    def get_command(self):
        return self.__command

    def set_response(self, response):
        ValueChecker.is_string(response)
        self.__response = response
        return self

    def get_response(self):
        return self.__response

    def set_fqdn(self, fqdn):
        ValueChecker.is_string(fqdn)
        self.__fqdn = fqdn
        return self

    def get_fqdn(self):
        return self.__fqdn

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

    def set_starttls(self, starttls):
        ValueChecker.is_bool(starttls)
        self.__starttls = starttls
        return self

    def get_starttls(self):
        return self.__starttls

    def set_authtype(self, authtype):
        ValueChecker.is_string(authtype)
        self.__authtype = authtype
        return self

    def get_authtype(self):
        return self.__authtype

    def set_authuser(self, authuser):
        ValueChecker.is_string(authuser)
        self.__authuser = authuser
        return self

    def get_authuser(self):
        return self.__authuser

    def set_authpass(self, authpass):
        ValueChecker.is_string(authpass)
        self.__authpass = authpass
        return self

    def get_authpass(self):
        return self.__authpass

    def set_ignore_quit_failure(self, ignore_quit_failure):
        ValueChecker.is_bool(ignore_quit_failure)
        self.__ignore_quit_failure = ignore_quit_failure
        return self

    def get_ignore_quit_failure(self):
        return self.__ignore_quit_failure

    def set_warning(self, warning):
        ValueChecker.is_number(warning)
        self.__warning = warning
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, critical):
        ValueChecker.is_number(critical)
        self.__critical = critical
        return self

    def get_critical(self):
        return self.__critical

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
            check = CheckSMTP(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('smtp'):
            SMTPCommand.create('smtp')

        return check

    def validate(self):
        if None is self.__host:
            raise Exception('You have to specify a host for ' + self.get_id())
