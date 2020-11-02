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
from icinga2confgen.Commands.MonitoringPlugins.SSHCommand import SSHCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckSSH(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckSSH', 'ssh')
        self.__hostname = None
        self.__port = None
        self.__timeout = None
        self.__remote_version = None
        self.__remote_protocol = None
        self.__force_ipv4 = None
        self.__force_ipv6 = None
        self.add_service_group(ServiceGroup.create('sshd'))

    def set_hostname(self, hostname):
        ValueChecker.is_string(hostname)
        self.__hostname = hostname
        return self

    def get_hostname(self):
        return self.__hostname

    def set_port(self, port):
        ValueChecker.is_number(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    def set_timeout(self, timeout):
        ValueChecker.is_number(timeout)
        self.__timeout = timeout
        return self

    def get_timeout(self):
        return self.__timeout

    def set_remote_version(self, remote_version):
        ValueChecker.is_string(remote_version)
        self.__remote_version = remote_version
        return self

    def get_remote_version(self):
        return self.__remote_version

    def set_remote_protocol(self, remote_protocol):
        ValueChecker.is_string(remote_protocol)
        self.__remote_protocol = remote_protocol
        return self

    def get_remote_protocol(self):
        return self.__remote_protocol

    def set_force_ipv4(self, enabled):
        ValueChecker.is_number(enabled)
        self.__force_ipv4 = enabled
        return self

    def get_force_ipv4(self):
        return self.__force_ipv4

    def set_force_ipv6(self, enabled):
        ValueChecker.is_number(enabled)
        self.__force_ipv6 = enabled
        return self

    def get_force_ipv6(self):
        return self.__force_ipv6

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckSSH(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('ssh'):
            SSHCommand.create('ssh')

        return check

    def validate(self):
        if None is self.__hostname:
            raise Exception('You have to specify a hostname for ' + self.get_id())
