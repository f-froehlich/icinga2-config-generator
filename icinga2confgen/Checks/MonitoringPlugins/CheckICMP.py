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
from icinga2confgen.Commands.MonitoringPlugins.ICMPCommand import ICMPCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckICMP(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckICMP', 'icmp')
        self.__host = None
        self.__use_ipv4 = False
        self.__use_ipv6 = False
        self.__source = None
        self.__packets = 2
        self.__packet_interval = None
        self.__minimum_hosts = None
        self.__ttl = 5
        self.__timeout = 10
        self.__bytes = 76
        self.__warning = None
        self.__critical = None
        self.add_service_group(ServiceGroup.create('icmp'))
        self.add_service_group(ServiceGroup.create('network'))

    def set_host(self, host):
        ValueChecker.is_string(host)
        self.__host = host
        return self

    def get_host(self):
        return self.__host

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

    def set_source(self, source):
        ValueChecker.is_string(source)
        self.__source = source
        return self

    def get_source(self):
        return self.__source

    def set_packets(self, packets):
        ValueChecker.is_number(packets)
        self.__packets = packets
        return self

    def get_packets(self):
        return self.__packets

    def set_packet_interval(self, packet_interval):
        ValueChecker.is_string(packet_interval)
        self.__packet_interval = packet_interval
        return self

    def get_packet_interval(self):
        return self.__packet_interval

    def set_minimum_hosts(self, minimum_hosts):
        ValueChecker.is_string(minimum_hosts)
        self.__minimum_hosts = minimum_hosts
        return self

    def get_minimum_hosts(self):
        return self.__minimum_hosts

    def set_ttl(self, ttl):
        ValueChecker.is_number(ttl)
        self.__ttl = ttl
        return self

    def get_ttl(self):
        return self.__ttl

    def set_bytes(self, bytes):
        ValueChecker.is_number(bytes)
        self.__bytes = bytes
        return self

    def get_bytes(self):
        return self.__bytes

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckICMP(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('icmp'):
            ICMPCommand.create('icmp')

        return check

    def validate(self):
        if None is self.__host:
            raise Exception('You have to specify a host for ' + self.get_id())
