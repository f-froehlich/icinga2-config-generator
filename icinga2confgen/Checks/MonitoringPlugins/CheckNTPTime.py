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
from icinga2confgen.Commands.MonitoringPlugins.NTPTimeCommand import NTPTimeCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckNTPTime(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckNTPTime', 'ntp_time')
        self.__force_ipv4 = False
        self.__force_ipv6 = False
        self.__ntp_server = '0.pool.ntp.org'
        self.__ntp_server_port = None
        self.__quiet = None
        self.__warning = '0.5'
        self.__critical = '1'
        self.__time_offset = None
        self.__delay = None
        self.__stratum_warn = None
        self.__stratum_crit = None
        self.__timeout = None
        self.set_check_interval('5m')
        self.add_service_group(ServiceGroup.create('ntp'))
        self.add_service_group(ServiceGroup.create('network'))

    def set_warning(self, seconds):
        ValueChecker.is_string(seconds)
        self.__warning = seconds
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, seconds):
        ValueChecker.is_string(seconds)
        self.__critical = seconds
        return self

    def get_critical(self):
        return self.__critical

    def set_stratum_critical(self, seconds):
        ValueChecker.is_string(seconds)
        self.__stratum_crit = seconds
        return self

    def get_stratum_critical(self):
        return self.__stratum_crit

    def set_stratum_warning(self, seconds):
        ValueChecker.is_string(seconds)
        self.__stratum_warn = seconds
        return self

    def get_stratum_warning(self):
        return self.__stratum_warn

    def set_timeout(self, seconds):
        ValueChecker.is_number(seconds)
        self.__timeout = seconds
        return self

    def get_timeout(self):
        return self.__timeout

    def set_delay(self, seconds):
        ValueChecker.is_number(seconds)
        self.__delay = seconds
        return self

    def get_delay(self):
        return self.__delay

    def set_time_offset(self, seconds):
        ValueChecker.is_number(seconds)
        self.__time_offset = seconds
        return self

    def get_time_offset(self):
        return self.__time_offset

    def set_quiet(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__quiet = enabled
        return self

    def get_quiet(self):
        return self.__quiet

    def set_ntp_server_port(self, port):
        ValueChecker.is_number(port)
        self.__ntp_server_port = port
        return self

    def get_ntp_server_port(self):
        return self.__ntp_server_port

    def set_ntp_server(self, hostname):
        ValueChecker.is_string(hostname)
        self.__ntp_server = hostname
        return self

    def get_ntp_server(self):
        return self.__ntp_server

    def set_force_ipv4(self, seconds):
        ValueChecker.is_number(seconds)
        self.__force_ipv4 = seconds
        return self

    def get_force_ipv4(self):
        return self.__force_ipv4

    def set_force_ipv6(self, seconds):
        ValueChecker.is_number(seconds)
        self.__force_ipv6 = seconds
        return self

    def get_force_ipv6(self):
        return self.__force_ipv6

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckNTPTime(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('ntp_time'):
            NTPTimeCommand.create('ntp_time')

        return check

    def validate(self):
        if None is self.__ntp_server:
            raise Exception('You have to specify a ntp server for ' + self.get_id())
