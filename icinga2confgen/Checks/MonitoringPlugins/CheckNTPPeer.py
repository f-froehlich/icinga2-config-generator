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
from icinga2confgen.Commands.MonitoringPlugins.NTPPeerCommand import NTPPeerCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckNTPPeer(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckNTPPeer', 'ntp_peer')
        self.__force_ipv4 = False
        self.__force_ipv6 = False
        self.__ntp_server = None
        self.__ntp_server_port = 123
        self.__quiet = None
        self.__warning = None
        self.__critical = None
        self.__swarn = None
        self.__scrit = None
        self.__jwarn = None
        self.__jcrit = None
        self.__twarn = None
        self.__tcrit = None
        self.__timeout = 10
        self.set_check_interval('5m')
        self.add_service_group(ServiceGroup.create('ntp'))
        self.add_service_group(ServiceGroup.create('network'))

    def set_warning(self, seconds):
        ValueChecker.is_number(seconds)
        self.__warning = seconds
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, seconds):
        ValueChecker.is_number(seconds)
        self.__critical = seconds
        return self

    def get_critical(self):
        return self.__critical

    def set_swarn(self, seconds):
        ValueChecker.is_number(seconds)
        self.__swarn = seconds
        return self

    def get_swarn(self):
        return self.__swarn

    def set_scrit(self, seconds):
        ValueChecker.is_number(seconds)
        self.__scrit = seconds
        return self

    def get_scrit(self):
        return self.__scrit

    def set_jwarn(self, seconds):
        ValueChecker.is_number(seconds)
        self.__jwarn = seconds
        return self

    def get_jwarn(self):
        return self.__jwarn

    def set_jcrit(self, seconds):
        ValueChecker.is_number(seconds)
        self.__jcrit = seconds
        return self

    def get_jcrit(self):
        return self.__jcrit

    def set_twarn(self, seconds):
        ValueChecker.is_number(seconds)
        self.__twarn = seconds
        return self

    def get_twarn(self):
        return self.__twarn

    def set_tcrit(self, seconds):
        ValueChecker.is_number(seconds)
        self.__tcrit = seconds
        return self

    def get_tcrit(self):
        return self.__tcrit

    def set_timeout(self, seconds):
        ValueChecker.is_number(seconds)
        self.__timeout = seconds
        return self

    def get_timeout(self):
        return self.__timeout

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
            check = CheckNTPPeer(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('ntp_peer'):
            NTPPeerCommand.create('ntp_peer')

        return check

    def validate(self):
        if None is self.__ntp_server:
            raise Exception('You have to specify a ntp server for ' + self.get_id())
