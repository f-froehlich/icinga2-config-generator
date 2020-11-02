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
from icinga2confgen.Commands.MonitoringPlugins.DHCPCommand import DHCPCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckDHCP(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckDHCP', 'dhcp')
        self.__server = None
        self.__requested_ip = None
        self.__timeout = 10
        self.__interface = None
        self.__mac = None
        self.__unicast = False
        self.add_service_group(ServiceGroup.create('dhcp'))
        self.add_service_group(ServiceGroup.create('network'))

    def set_server(self, server):
        ValueChecker.is_string(server)
        self.__server = server
        return self

    def get_server(self):
        return self.__server

    def set_requested_ip(self, requested_ip):
        ValueChecker.is_string(requested_ip)
        self.__requested_ip = requested_ip
        return self

    def get_requested_ip(self):
        return self.__requested_ip

    def set_timeout(self, timeout):
        ValueChecker.is_number(timeout)
        self.__timeout = timeout
        return self

    def get_timeout(self):
        return self.__timeout

    def set_interface(self, interface):
        ValueChecker.is_string(interface)
        self.__interface = interface
        return self

    def get_interface(self):
        return self.__interface

    def set_mac(self, mac):
        ValueChecker.is_string(mac)
        self.__mac = mac
        return self

    def get_mac(self):
        return self.__mac

    def set_unicast(self, unicast):
        ValueChecker.is_bool(unicast)
        self.__unicast = unicast
        return self

    def get_unicast(self):
        return self.__unicast

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckDHCP(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('dhcp'):
            DHCPCommand.create('dhcp')

        return check

    def validate(self):
        pass
