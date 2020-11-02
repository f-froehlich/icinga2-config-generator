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
from icinga2confgen.Checks.MonitoringPlugins.CheckPing4 import CheckPing4
from icinga2confgen.Checks.MonitoringPlugins.CheckSSH import CheckSSH
from icinga2confgen.ValueChecker import ValueChecker


class DefaultRemoteChecks:

    def __init__(self, servers=[], checkserver=[], notifications=[]):
        self.__checkserver = checkserver
        self.__notifications = notifications
        self.__servers = servers
        self.__check_ping = True
        self.__check_ssh = True
        self.__check_ssh_port = 22

    def check_ping(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__check_ping = enabled

        return self

    def is_checking_ping(self):
        return self.__check_ping

    def check_ssh(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__check_ssh = enabled

        return self

    def is_checking_ssh(self):
        return self.__check_ssh

    def check_ssh_port(self, port):
        ValueChecker.is_number(port)
        self.__check_ssh_port = port

        return self

    def is_checking_ssh_port(self):
        return self.__check_ssh_port

    def apply_check(self, check):
        for notification in self.__notifications:
            check.add_notification(notification)

        for checkserver in self.__checkserver:
            checkserver.add_check(check)

    def apply(self):
        for server in self.__servers:
            base_id = 'remote_checks_' + server.get_id()
            ipv4 = server.get_ipv4()
            ipv6 = server.get_ipv6()

            if True is self.__check_ping:
                if None is not ipv4:
                    check = CheckPing4.create('ping4_' + base_id)
                    check.set_address(ipv4) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check)
                if None is not ipv6:
                    check = CheckPing4.create('ping6_' + base_id)
                    check.set_address(ipv6) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check)

            if True is self.__check_ssh:
                if None is not ipv4:
                    check = CheckSSH.create('ssh_ipv4_' + base_id)
                    check.set_hostname(ipv4) \
                        .set_port(self.__check_ssh_port) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check)

                if None is not ipv6:
                    check = CheckSSH.create('ssh_ipv4_' + base_id)
                    check.set_hostname(ipv6) \
                        .set_port(self.__check_ssh_port) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check)
