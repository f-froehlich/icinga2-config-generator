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

from icinga2confgen.Commands.MonitoringPlugins.CiphersCommand import CiphersCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.Helpers.Nmap import NmapBase, \
    NmapScanTCP, \
    NmapNotScanUDP, \
    NmapN, \
    Nmapr, \
    NmapSystemDns, \
    NmapTraceroute, \
    NmapF, \
    NmapR, \
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
    NmapUnprivileged, \
    NmapScriptExecutor
from icinga2confgen.ValueChecker import ValueChecker


class CheckCiphers(NmapBase, NmapScriptExecutor, NmapNotScanUDP, NmapScanTCP, NmapN, NmapR, Nmapr, NmapSystemDns,
                   NmapTraceroute, NmapF, NmapSV, NmapVersionLight, NmapVersionAll, NmapVersionTrace, NmapSC,
                   NmapScriptTrace, NmapO, NmapOsscanGuess, NmapBadsum, Nmap6, NmapA, NmapSendEth, NmapSendIp,
                   NmapPrivileged, NmapPn, NmapUnprivileged):

    def __init__(self, id):
        NmapBase.__init__(self, id, 'CheckCiphers', 'ciphers')
        NmapNotScanUDP.__init__(self, 'ciphers')
        NmapScanTCP.__init__(self, 'ciphers')
        NmapN.__init__(self, 'ciphers')
        NmapR.__init__(self, 'ciphers')
        NmapSystemDns.__init__(self, 'ciphers')
        NmapTraceroute.__init__(self, 'ciphers')
        NmapF.__init__(self, 'ciphers')
        Nmapr.__init__(self, 'ciphers')
        NmapSV.__init__(self, 'ciphers')
        NmapVersionLight.__init__(self, 'ciphers')
        NmapVersionAll.__init__(self, 'ciphers')
        NmapVersionTrace.__init__(self, 'ciphers')
        NmapSC.__init__(self, 'ciphers')
        NmapScriptTrace.__init__(self, 'ciphers')
        NmapO.__init__(self, 'ciphers')
        NmapOsscanGuess.__init__(self, 'ciphers')
        NmapBadsum.__init__(self, 'ciphers')
        Nmap6.__init__(self, 'ciphers')
        NmapA.__init__(self, 'ciphers')
        NmapSendEth.__init__(self, 'ciphers')
        NmapSendIp.__init__(self, 'ciphers')
        NmapPrivileged.__init__(self, 'ciphers')
        NmapPn.__init__(self, 'ciphers')
        NmapUnprivileged.__init__(self, 'ciphers')

        NmapScriptExecutor.__init__(self, 'ciphers')
        self.add_service_group(ServiceGroup.create('ciphers'))

        self.__allowed_ciphers = []
        self.__least_protocol_strength = []
        self.__least_port_strength = []
        self.__ignore_cipher_name = False
        self.__ignore_protocol_strength = False
        self.__ignore_strength = False

    def add_allowed_cipher(self, ip, port, protocol, cipher_names):
        ValueChecker.is_number(port)
        ValueChecker.is_string(ip)
        ValueChecker.is_string(protocol)
        ValueChecker.is_array(cipher_names)

        config = ip + '/' + str(port) + '/' + protocol + '/' + ','.join(cipher_names)
        if config not in self.__allowed_ciphers:
            self.__allowed_ciphers.append(config)

        return self

    def remove_allowed_cipher(self, ip, port, protocol, cipher_names):
        ValueChecker.is_number(port)
        ValueChecker.is_string(protocol)
        ValueChecker.is_string(ip)
        ValueChecker.is_array(cipher_names)

        config = ip + '/' + str(port) + '/' + protocol + '/' + ','.join(cipher_names)
        self.__allowed_ciphers.remove(config)

        return self

    def get_allowed_ciphers(self):
        return self.__allowed_ciphers

    def validate_strength(self, strength):
        ValueChecker.is_string(strength)
        strength = strength.upper()
        if strength not in ['A', 'B', 'C', 'D', 'E', 'F']:
            raise Exception('Invalid strength "' + strength + '" detected in ' + self.get_id())

    def add_least_protocol_strength(self, ip, port, protocol, strength):
        ValueChecker.is_number(port)
        ValueChecker.is_string(protocol)
        ValueChecker.is_string(ip)
        self.validate_strength(strength)

        config = ip + '/' + str(port) + '/' + protocol + '/' + strength
        if config not in self.__least_protocol_strength:
            self.__least_protocol_strength.append(config)

        return self

    def remove_least_protocol_strength(self, ip, port, protocol, strength):
        ValueChecker.is_number(port)
        ValueChecker.is_string(protocol)
        ValueChecker.is_string(ip)
        self.validate_strength(strength)

        config = ip + '/' + str(port) + '/' + protocol + '/' + strength
        self.__least_protocol_strength.remove(config)

        return self

    def get_least_protocol_strength(self):
        return self.__least_protocol_strength

    def add_least_port_strength(self, ip, port, strength):
        ValueChecker.is_number(port)
        ValueChecker.is_string(ip)
        self.validate_strength(strength)

        config = ip + '/' + str(port) + '/' + strength
        if config not in self.__least_port_strength:
            self.__least_port_strength.append(config)

        return self

    def remove_least_port_strength(self, ip, port, strength):
        ValueChecker.is_number(port)
        ValueChecker.is_string(ip)
        self.validate_strength(strength)

        config = ip + '/' + str(port) + '/' + '/' + strength
        self.__least_port_strength.remove(config)

        return self

    def get_least_port_strength(self):
        return self.__least_port_strength

    def set_ignore_cipher_name(self, ignore):
        ValueChecker.is_bool(ignore)
        self.__ignore_cipher_name = ignore

        return self

    def get_ignore_cipher_name(self):
        return self.__ignore_cipher_name

    def set_ignore_protocol_strength(self, ignore):
        ValueChecker.is_bool(ignore)
        self.__ignore_protocol_strength = ignore

        return self

    def get_ignore_protocol_strength(self):
        return self.__ignore_protocol_strength

    def set_ignore_strength(self, ignore):
        ValueChecker.is_bool(ignore)
        self.__ignore_strength = ignore

        return self

    def get_ignore_strength(self):
        return self.__ignore_strength

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckCiphers(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckCiphers):
            raise Exception('Id must be for an instance of CheckCiphers but other instance is returned')

        if None is ConfigBuilder.get_command('ciphers'):
            CiphersCommand.create('ciphers')

        return check

    def get_config(self):
        return NmapBase.get_config(self)

    def get_custom_config(self):
        config = NmapNotScanUDP.get_config(self)
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
        config += NmapBase.get_custom_config(self)
        config += NmapScriptExecutor.get_config(self)

        return config

    def validate(self):
        NmapNotScanUDP.validate(self)
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
        NmapScriptExecutor.validate(self)
