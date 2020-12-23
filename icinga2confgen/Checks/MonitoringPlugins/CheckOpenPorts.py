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

from icinga2confgen.Commands.MonitoringPlugins.OpenPortsCommand import OpenPortsCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.Helpers.Nmap import NmapBase, NmapOnlyTCP, NmapOnlyUDP, NmapPN, NmapFast
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class CheckOpenPorts(NmapBase, NmapOnlyUDP, NmapOnlyTCP, NmapPN, NmapFast):

    def __init__(self, id):
        NmapBase.__init__(self, id, 'CheckOpenPorts', 'open_ports')
        NmapOnlyUDP.__init__(self, 'open_ports')
        NmapOnlyTCP.__init__(self, 'open_ports')
        NmapPN.__init__(self, 'open_ports')
        NmapFast.__init__(self, 'open_ports')
        self.add_service_group(ServiceGroup.create('open_ports'))
        self.__allowed_ports = []

    def add_allowed_port(self, port, protocol):
        ValueChecker.is_number(port)
        ValueChecker.is_string(protocol)
        protocol = protocol.lower()

        if protocol not in ['udp', 'tcp']:
            raise Exception('Protocol must be UDP or TCP in ' + self.get_id())

        config = str(port) + '/' + protocol
        if config not in self.__allowed_ports:
            self.__allowed_ports.append(config)

        return self

    def remove_allowed_port(self, port, protocol):
        ValueChecker.is_number(port)
        ValueChecker.is_string(protocol)
        protocol = protocol.lower()

        if protocol not in ['udp', 'tcp']:
            raise Exception('Protocol must be UDP or TCP in ' + self.get_id())

        config = str(port) + '/' + protocol
        self.__allowed_ports.remove(config)

        return self

    def get_allowed_ports(self):
        return self.__allowed_ports

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckOpenPorts(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckOpenPorts):
            raise Exception('Id must be for an instance of CheckOpenPorts but other instance is returned')

        if None is ConfigBuilder.get_command('open_ports'):
            OpenPortsCommand.create('open_ports')

        return check

    def get_config(self):
        return NmapBase.get_config(self)

    def get_custom_config(self):
        config = NmapOnlyUDP.get_config(self)
        config += NmapOnlyTCP.get_config(self)
        config += NmapPN.get_config(self)
        config += NmapFast.get_config(self)
        config += ValueMapper.parse_var('vars.allowed_ports', self.__allowed_ports)
        config += NmapBase.get_custom_config(self)

        return config

    def validate(self):
        NmapBase.validate(self)
        NmapOnlyUDP.validate(self)
        NmapOnlyTCP.validate(self)
        NmapPN.validate(self)
        NmapFast.validate(self)
