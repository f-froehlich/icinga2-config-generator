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
from icinga2confgen.Commands.MonitoringPlugins.DigCommand import DigCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckDig(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckDig', 'dig')
        self.__warning_time = 5
        self.__critical_time = 10
        self.__dnsserver_hostname = '1.1.1.1'
        self.__dnsserver_port = None
        self.__only_ipv4 = False
        self.__only_ipv6 = False
        self.__question = None
        self.__timeout = 10
        self.__record_type = 'A'
        self.__expected_address = 'set expected address!'
        self.__question_arguments = None
        self.set_check_interval('15m')
        self.add_service_group(ServiceGroup.create('dns'))
        self.add_service_group(ServiceGroup.create('dig'))
        self.add_service_group(ServiceGroup.create('network'))

    def set_warning_time(self, seconds):
        ValueChecker.is_number(seconds)
        self.__warning_time = seconds
        return self

    def get_warning_time(self):
        return self.__warning_time

    def set_critical_time(self, seconds):
        ValueChecker.is_number(seconds)
        self.__critical_time = seconds
        return self

    def get_critical_time(self):
        return self.__critical_time

    def set_timeout(self, seconds):
        ValueChecker.is_number(seconds)
        self.__timeout = seconds
        return self

    def get_timeout(self):
        return self.__timeout

    def set_question_arguments(self, arguments):
        ValueChecker.is_string(arguments)
        self.__question_arguments = arguments
        return self

    def get_question_arguments(self):
        return self.__question_arguments

    def set_expected_address(self, address):
        ValueChecker.is_string(address)
        self.__expected_address = address
        return self

    def get_expected_address(self):
        return self.__expected_address

    def set_record_type(self, type):
        ValueChecker.is_string(type)
        self.__record_type = type
        return self

    def get_record_type(self):
        return self.__record_type

    def set_question(self, address):
        ValueChecker.is_string(address)
        self.__question = address
        return self

    def get_question(self):
        return self.__question

    def set_dnsserver_hostname(self, hostname):
        ValueChecker.is_string(hostname)
        self.__dnsserver_hostname = hostname
        return self

    def get_dnsserver_hostname(self):
        return self.__dnsserver_hostname

    def set_dnsserver_port(self, port):
        ValueChecker.is_number(port)
        self.__dnsserver_port = port
        return self

    def get_dnsserver_port(self):
        return self.__dnsserver_port

    def set_only_ipv4(self, enabled):
        ValueChecker.is_number(enabled)
        self.__only_ipv4 = enabled
        return self

    def get_only_ipv4(self):
        return self.__only_ipv4

    def set_only_ipv6(self, enabled):
        ValueChecker.is_number(enabled)
        self.__only_ipv6 = enabled
        return self

    def get_only_ipv6(self):
        return self.__only_ipv6

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckDig(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('dig'):
            DigCommand.create('dig')

        return check

    def validate(self):
        if None is self.__question:
            raise Exception('You have to specify a question for ' + self.get_id())
        if None is self.__record_type:
            raise Exception('You have to specify a record type for ' + self.get_id())
        if None is self.__expected_address:
            raise Exception('You have to specify an expected address for ' + self.get_id())
        if None is self.__warning_time:
            raise Exception('You have to specify a warning time for ' + self.get_id())
        if None is self.__critical_time:
            raise Exception('You have to specify a critical time for ' + self.get_id())
