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
from icinga2confgen.Checks.MonitoringPlugins.CheckOpenPorts import CheckOpenPorts
from icinga2confgen.Checks.NagiosPlugins.CheckPing4 import CheckPing4
from icinga2confgen.Checks.NagiosPlugins.CheckPing6 import CheckPing6
from icinga2confgen.Checks.NagiosPlugins.CheckSSH import CheckSSH
from icinga2confgen.Helpers.RemoteCheckManager import RemoteCheckManager
from icinga2confgen.ValueChecker import ValueChecker


class DefaultRemoteChecks(RemoteCheckManager):

    def __init__(self, servers=[], checkserver=[], notifications=[]):
        RemoteCheckManager.__init__(self, servers=servers, checkserver=checkserver, notifications=notifications)
        self.__check_ping = True
        self.__check_open_ports = False
        self.__open_ports = []
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

    def check_open_ports(self, port):
        ValueChecker.is_number(port)
        self.__check_open_ports = port

        return self

    def is_checking_open_ports(self):
        return self.__check_open_ports

    def add_allowed_port(self, port, protocol):
        ValueChecker.is_number(port)
        ValueChecker.is_string(protocol)
        protocol = protocol.lower()

        config = (port, protocol)
        if config not in self.__open_ports:
            self.__open_ports.append(config)

        return self

    def remove_allowed_port(self, port, protocol):
        ValueChecker.is_number(port)
        ValueChecker.is_string(protocol)
        protocol = protocol.lower()

        config = (port, protocol)
        self.__open_ports.remove(config)

        return self

    def get_allowed_ports(self):
        return self.__open_ports

    def apply(self):
        for server in self.get_servers():
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
                    check = CheckPing6.create('ping6_' + base_id)
                    check.set_address(ipv6) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check)

            if True is self.__check_open_ports:
                if None is not ipv4:
                    check = CheckOpenPorts.create('open_ports4_' + base_id)
                    check.add_host(ipv4) \
                        .set_top_ports(15000)
                    for config in self.__open_ports:
                        check.add_allowed_port(config[0], config[1])
                    check.set_display_name(check.get_display_name() + ' (ipv4) ' + server.get_display_name())
                    self.apply_check(check)

                if None is not ipv6:
                    check = CheckOpenPorts.create('open_ports6_' + base_id)
                    check.add_host(ipv6) \
                        .set_top_ports(15000) \
                        .set_6(True)

                    for config in self.__open_ports:
                        check.add_allowed_port(config[0], config[1])
                    check.set_display_name(check.get_display_name() + ' (ipv6) ' + server.get_display_name())
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
                        .set_force_ipv6(True) \
                        .set_port(self.__check_ssh_port) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check)
