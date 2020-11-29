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
from icinga2confgen.Helpers.Nmap import NmapBase, NmapNotOnlyTCP, NmapOnlyUDP, NmapPN, NmapFast
from icinga2confgen.ValueChecker import ValueChecker


class CheckCiphers(NmapBase, NmapOnlyUDP, NmapNotOnlyTCP, NmapPN, NmapFast):

    def __init__(self, id):
        NmapBase.__init__(self, id, 'CheckCiphers', 'ciphers')
        NmapOnlyUDP.__init__(self, 'ciphers')
        NmapNotOnlyTCP.__init__(self, 'ciphers')
        NmapPN.__init__(self, 'ciphers')
        NmapFast.__init__(self, 'ciphers')
        self.add_service_group(ServiceGroup.create('ciphers'))

        self.__allowed_tlsv1_0_ciphers = []
        self.__allowed_tlsv1_1_ciphers = []
        self.__allowed_tlsv1_2_ciphers = []
        self.__allowed_tlsv1_3_ciphers = []

        self.__least_tlsv1_0_strength = []
        self.__least_tlsv1_1_strength = []
        self.__least_tlsv1_2_strength = []
        self.__least_tlsv1_3_strength = []

        self.__least_strength = []
        self.__least_strength_overall = None

        self.__ignore_cipher_name = False
        self.__ignore_cipher_strength = False
        self.__ignore_strength = False
        self.__ignore_port = []

    def add_allowed_tlsv1_0_cipher(self, port, cipher_names):
        ValueChecker.is_number(port)
        ValueChecker.is_array(cipher_names)

        config = str(port) + ':' + ','.join(cipher_names)
        if config not in self.__allowed_tlsv1_0_ciphers:
            self.__allowed_tlsv1_0_ciphers.append(config)

        return self

    def remove_allowed_tlsv1_0_cipher(self, port, cipher_names):
        ValueChecker.is_number(port)
        ValueChecker.is_array(cipher_names)

        config = str(port) + ':' + ','.join(cipher_names)
        self.__allowed_tlsv1_0_ciphers.remove(config)

        return self

    def get_allowed_tlsv1_0_ciphers(self):
        return self.__allowed_tlsv1_0_ciphers

    def add_allowed_tlsv1_1_cipher(self, port, cipher_names):
        ValueChecker.is_number(port)
        ValueChecker.is_array(cipher_names)

        config = str(port) + ':' + ','.join(cipher_names)
        if config not in self.__allowed_tlsv1_1_ciphers:
            self.__allowed_tlsv1_1_ciphers.append(config)

        return self

    def remove_allowed_tlsv1_1_cipher(self, port, cipher_names):
        ValueChecker.is_number(port)
        ValueChecker.is_array(cipher_names)

        config = str(port) + ':' + ','.join(cipher_names)
        self.__allowed_tlsv1_1_ciphers.remove(config)

        return self

    def get_allowed_tlsv1_1_ciphers(self):
        return self.__allowed_tlsv1_1_ciphers

    def add_allowed_tlsv1_2_cipher(self, port, cipher_names):
        ValueChecker.is_number(port)
        ValueChecker.is_array(cipher_names)

        config = str(port) + ':' + ','.join(cipher_names)
        if config not in self.__allowed_tlsv1_2_ciphers:
            self.__allowed_tlsv1_2_ciphers.append(config)

        return self

    def remove_allowed_tlsv1_2_cipher(self, port, cipher_names):
        ValueChecker.is_number(port)
        ValueChecker.is_array(cipher_names)

        config = str(port) + ':' + ','.join(cipher_names)
        self.__allowed_tlsv1_2_ciphers.remove(config)

        return self

    def get_allowed_tlsv1_2_ciphers(self):
        return self.__allowed_tlsv1_2_ciphers

    def add_allowed_tlsv1_3_cipher(self, port, cipher_names):
        ValueChecker.is_number(port)
        ValueChecker.is_array(cipher_names)

        config = str(port) + ':' + ','.join(cipher_names)
        if config not in self.__allowed_tlsv1_3_ciphers:
            self.__allowed_tlsv1_3_ciphers.append(config)

        return self

    def remove_allowed_tlsv1_3_cipher(self, port, cipher_names):
        ValueChecker.is_number(port)
        ValueChecker.is_array(cipher_names)

        config = str(port) + ':' + ','.join(cipher_names)
        self.__allowed_tlsv1_3_ciphers.remove(config)

        return self

    def get_allowed_tlsv1_3_ciphers(self):
        return self.__allowed_tlsv1_3_ciphers

    def validate_strength(self, strength):
        ValueChecker.is_string(strength)
        strength = strength.upper()
        if strength not in ['A', 'B', 'C', 'D', 'E', 'F']:
            raise Exception('Invalid strength "' + strength + '" detected in ' + self.get_id())

    def add_least_tlsv1_0_strength(self, port, strength):
        ValueChecker.is_number(port)
        self.validate_strength(strength)

        config = str(port) + ':' + strength
        if config not in self.__least_tlsv1_0_strength:
            self.__least_tlsv1_0_strength.append(config)

        return self

    def remove_least_tlsv1_0_strength(self, port, strength):
        ValueChecker.is_number(port)
        self.validate_strength(strength)

        config = str(port) + ':' + strength
        self.__least_tlsv1_0_strength.remove(config)

        return self

    def get_least_tlsv1_0_strength(self):
        return self.__least_tlsv1_0_strength

    def add_least_tlsv1_1_strength(self, port, strength):
        ValueChecker.is_number(port)
        self.validate_strength(strength)

        config = str(port) + ':' + strength
        if config not in self.__least_tlsv1_1_strength:
            self.__least_tlsv1_1_strength.append(config)

        return self

    def remove_least_tlsv1_1_strength(self, port, strength):
        ValueChecker.is_number(port)
        self.validate_strength(strength)

        config = str(port) + ':' + strength
        self.__least_tlsv1_1_strength.remove(config)

        return self

    def get_least_tlsv1_1_strength(self):
        return self.__least_tlsv1_1_strength

    def add_least_tlsv1_2_strength(self, port, strength):
        ValueChecker.is_number(port)
        self.validate_strength(strength)

        config = str(port) + ':' + strength
        if config not in self.__least_tlsv1_2_strength:
            self.__least_tlsv1_2_strength.append(config)

        return self

    def remove_least_tlsv1_2_strength(self, port, strength):
        ValueChecker.is_number(port)
        self.validate_strength(strength)

        config = str(port) + ':' + strength
        self.__least_tlsv1_2_strength.remove(config)

        return self

    def get_least_tlsv1_2_strength(self):
        return self.__least_tlsv1_2_strength

    def add_least_tlsv1_3_strength(self, port, strength):
        ValueChecker.is_number(port)
        self.validate_strength(strength)

        config = str(port) + ':' + strength
        if config not in self.__least_tlsv1_3_strength:
            self.__least_tlsv1_3_strength.append(config)

        return self

    def remove_least_tlsv1_3_strength(self, port, strength):
        ValueChecker.is_number(port)
        self.validate_strength(strength)

        config = str(port) + ':' + strength
        self.__least_tlsv1_3_strength.remove(config)

        return self

    def get_least_tlsv1_3_strength(self):
        return self.__least_tlsv1_3_strength

    def add_least_strength(self, port, strength):
        ValueChecker.is_number(port)
        self.validate_strength(strength)

        config = str(port) + ':' + strength
        if config not in self.__least_strength:
            self.__least_strength.append(config)

        return self

    def remove_least_strength(self, port, strength):
        ValueChecker.is_number(port)
        self.validate_strength(strength)

        config = str(port) + ':' + strength
        self.__least_strength.remove(config)

        return self

    def get_least_strength(self):
        return self.__least_strength

    def set_least_strength_overall(self, strength):
        self.validate_strength(strength)
        self.__least_strength_overall = strength

        return self

    def get_least_strength_overall(self):
        return self.__least_strength_overall

    def set_ignore_cipher_name(self, ignore):
        ValueChecker.is_bool(ignore)
        self.__ignore_cipher_name = ignore

        return self

    def get_ignore_cipher_name(self):
        return self.__ignore_cipher_name

    def set_ignore_cipher_strength(self, ignore):
        ValueChecker.is_bool(ignore)
        self.__ignore_cipher_strength = ignore

        return self

    def get_ignore_cipher_strength(self):
        return self.__ignore_cipher_strength

    def set_ignore_strength(self, ignore):
        ValueChecker.is_bool(ignore)
        self.__ignore_strength = ignore

        return self

    def get_ignore_strength(self):
        return self.__ignore_strength

    def add_ignore_port(self, port):
        ValueChecker.is_number(port)

        if port not in self.__ignore_port:
            self.__ignore_port.append(port)

        return self

    def remove_ignore_port(self, port):
        ValueChecker.is_number(port)
        self.__ignore_port.remove(port)

        return self

    def get_ignore_port(self):
        return self.__ignore_port

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            id = 'check_' + id
            check = CheckCiphers(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('ciphers'):
            CiphersCommand.create('ciphers')

        return check

    def get_config(self):
        return NmapBase.get_config(self)

    def get_custom_config(self):
        config = NmapOnlyUDP.get_config(self)
        config += NmapNotOnlyTCP.get_config(self)
        config += NmapPN.get_config(self)
        config += NmapFast.get_config(self)
        config += NmapBase.get_custom_config(self)

        return config

    def validate(self):
        NmapOnlyUDP.validate(self)
        NmapNotOnlyTCP.validate(self)
        NmapPN.validate(self)
        NmapFast.validate(self)
