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
from icinga2confgen.Helpers.Nmap import NmapBase, \
    NmapScanTCP, \
    NmapScanUDP, \
    NmapN, \
    NmapR, \
    Nmapr, \
    NmapSystemDns, \
    NmapTraceroute, \
    NmapF, \
    NmapSV, \
    NmapVersionLight, \
    NmapVersionAll, \
    NmapVersionTrace, \
    NmapSC, \
    NmapScriptTrace, \
    NmapO, \
    NmapOsscanGuess, \
    NmapBadsum, \
    Nmap6, \
    NmapA, \
    NmapSendEth, \
    NmapSendIp, \
    NmapPrivileged, \
    NmapPn, \
    NmapUnprivileged
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class CheckOpenPorts(NmapBase, NmapScanUDP, NmapScanTCP, NmapN, NmapSystemDns, NmapTraceroute, NmapF, Nmapr, NmapR,
                     NmapSV, NmapVersionLight, NmapVersionAll, NmapVersionTrace, NmapSC, NmapScriptTrace, NmapO,
                     NmapOsscanGuess, NmapBadsum, Nmap6, NmapA, NmapSendEth, NmapSendIp, NmapPrivileged, NmapPn,
                     NmapUnprivileged):

    def __init__(self, id):
        NmapBase.__init__(self, id, 'CheckOpenPorts', 'open_ports')
        NmapScanUDP.__init__(self, 'open_ports')
        NmapScanTCP.__init__(self, 'open_ports')
        NmapN.__init__(self, 'open_ports')
        Nmapr.__init__(self, 'open_ports')
        NmapSystemDns.__init__(self, 'open_ports')
        NmapTraceroute.__init__(self, 'open_ports')
        NmapF.__init__(self, 'open_ports')
        NmapR.__init__(self, 'open_ports')
        NmapSV.__init__(self, 'open_ports')
        NmapVersionLight.__init__(self, 'open_ports')
        NmapVersionAll.__init__(self, 'open_ports')
        NmapVersionTrace.__init__(self, 'open_ports')
        NmapSC.__init__(self, 'open_ports')
        NmapScriptTrace.__init__(self, 'open_ports')
        NmapO.__init__(self, 'open_ports')
        NmapOsscanGuess.__init__(self, 'open_ports')
        NmapBadsum.__init__(self, 'open_ports')
        Nmap6.__init__(self, 'open_ports')
        NmapA.__init__(self, 'open_ports')
        NmapSendEth.__init__(self, 'open_ports')
        NmapSendIp.__init__(self, 'open_ports')
        NmapPrivileged.__init__(self, 'open_ports')
        NmapPn.__init__(self, 'open_ports')
        NmapUnprivileged.__init__(self, 'open_ports')
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
        config = NmapScanUDP.get_config(self)
        config += NmapScanTCP.get_config(self)
        config += NmapN.get_config(self)
        config += Nmapr.get_config(self)
        config += NmapSystemDns.get_config(self)
        config += NmapTraceroute.get_config(self)
        config += NmapF.get_config(self)
        config += NmapR.get_config(self)
        config += NmapSV.get_config(self)
        config += NmapVersionLight.get_config(self)
        config += NmapVersionAll.get_config(self)
        config += NmapVersionTrace.get_config(self)
        config += NmapSC.get_config(self)
        config += NmapScriptTrace.get_config(self)
        config += NmapO.get_config(self)
        config += NmapOsscanGuess.get_config(self)
        config += NmapBadsum.get_config(self)
        config += Nmap6.get_config(self)
        config += NmapA.get_config(self)
        config += NmapSendEth.get_config(self)
        config += NmapSendIp.get_config(self)
        config += NmapPrivileged.get_config(self)
        config += NmapPn.get_config(self)
        config += NmapUnprivileged.get_config(self)
        config += ValueMapper.parse_var('vars.allowed_ports', self.__allowed_ports)
        config += NmapBase.get_custom_config(self)

        return config

    def validate(self):
        NmapBase.validate(self)
        NmapScanUDP.validate(self)
        NmapScanTCP.validate(self)
        NmapN.validate(self)
        Nmapr.validate(self)
        NmapSystemDns.validate(self)
        NmapTraceroute.validate(self)
        NmapF.validate(self)
        NmapR.validate(self)
        NmapSV.validate(self)
        NmapVersionLight.validate(self)
        NmapVersionAll.validate(self)
        NmapVersionTrace.validate(self)
        NmapSC.validate(self)
        NmapScriptTrace.validate(self)
        NmapO.validate(self)
        NmapOsscanGuess.validate(self)
        NmapBadsum.validate(self)
        Nmap6.validate(self)
        NmapA.validate(self)
        NmapSendEth.validate(self)
        NmapSendIp.validate(self)
        NmapPrivileged.validate(self)
        NmapPn.validate(self)
        NmapUnprivileged.validate(self)
