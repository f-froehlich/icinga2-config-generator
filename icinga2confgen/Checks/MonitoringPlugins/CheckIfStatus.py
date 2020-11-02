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
from icinga2confgen.Commands.MonitoringPlugins.IfStatusCommand import IfStatusCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckIfStatus(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckIfStatus', 'ifstatus')
        self.__host = None
        self.__port = 161
        self.__community = None
        self.__snmp_version = None
        self.__if_mib = False
        self.__snmp_exclude = None
        self.__unused_ports_by_name = None
        self.__unused_ports = None
        self.__seclevel = None
        self.__secname = None
        self.__context = None
        self.__authpass = None
        self.__authproto = None
        self.__privpass = None
        self.__privproto = None
        self.__max_msg_size = None
        self.__timeout = 10
        self.add_service_group(ServiceGroup.create('network'))
        self.add_service_group(ServiceGroup.create('ifstatus'))

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

    def set_community(self, community):
        ValueChecker.is_string(community)
        self.__community = community
        return self

    def get_community(self):
        return self.__community

    def set_snmp_version(self, snmp_version):
        ValueChecker.is_string(snmp_version)
        self.__snmp_version = snmp_version
        return self

    def get_snmp_version(self):
        return self.__snmp_version

    def set_if_mib(self, if_mib):
        ValueChecker.is_bool(if_mib)
        self.__if_mib = if_mib
        return self

    def get_if_mib(self):
        return self.__if_mib

    def set_snmp_exclude(self, snmp_exclude):
        ValueChecker.is_string(snmp_exclude)
        self.__snmp_exclude = snmp_exclude
        return self

    def get_snmp_exclude(self):
        return self.__snmp_exclude

    def set_unused_ports_by_name(self, unused_ports_by_name):
        ValueChecker.is_string(unused_ports_by_name)
        self.__unused_ports_by_name = unused_ports_by_name
        return self

    def get_unused_ports_by_name(self):
        return self.__unused_ports_by_name

    def set_unused_ports(self, unused_ports):
        ValueChecker.is_string(unused_ports)
        self.__unused_ports = unused_ports
        return self

    def get_unused_ports(self):
        return self.__unused_ports

    def set_seclevel(self, seclevel):
        ValueChecker.is_string(seclevel)
        self.__seclevel = seclevel
        return self

    def get_seclevel(self):
        return self.__seclevel

    def set_secname(self, secname):
        ValueChecker.is_string(secname)
        self.__secname = secname
        return self

    def get_secname(self):
        return self.__secname

    def set_context(self, context):
        ValueChecker.is_string(context)
        self.__context = context
        return self

    def get_context(self):
        return self.__context

    def set_authpass(self, authpass):
        ValueChecker.is_string(authpass)
        self.__authpass = authpass
        return self

    def get_authpass(self):
        return self.__authpass

    def set_authproto(self, authproto):
        ValueChecker.is_string(authproto)
        self.__authproto = authproto
        return self

    def get_authproto(self):
        return self.__authproto

    def set_privpass(self, privpass):
        ValueChecker.is_string(privpass)
        self.__privpass = privpass
        return self

    def get_privpass(self):
        return self.__privpass

    def set_privproto(self, privproto):
        ValueChecker.is_string(privproto)
        self.__privproto = privproto
        return self

    def get_privproto(self):
        return self.__privproto

    def set_max_msg_size(self, max_msg_size):
        ValueChecker.is_number(max_msg_size)
        self.__max_msg_size = max_msg_size
        return self

    def get_max_msg_size(self):
        return self.__max_msg_size

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
            check = CheckIfStatus(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('ifstatus'):
            IfStatusCommand.create('ifstatus')

        return check

    def validate(self):
        if None is self.__community:
            raise Exception('You have to specify a community for ' + self.get_id())
        if None is self.__host:
            raise Exception('You have to specify a host for ' + self.get_id())
