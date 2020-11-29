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
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class NmapBase(Check):

    def __init__(self, id, class_name, command_name):
        Check.__init__(self, id, class_name, command_name)
        self._command_name = command_name
        self.__host = None
        self.__ports = None
        self.__top_ports = None
        self.__min_rate = None
        self.__max_rate = None
        self.__host_timeout = None
        self.__max_retries = None
        self.__scripts = []
        self.__timeout = None
        self.set_timeout(300)
        self.set_check_interval('1h')
        self.add_service_group(ServiceGroup.create('nmap'))
        self.add_service_group(ServiceGroup.create('security'))

    def set_host(self, host):
        ValueChecker.is_string(host)
        self.__host = host
        return self

    def get_host(self):
        return self.__host

    def set_timeout(self, timeout):
        ValueChecker.is_number(timeout)
        self.__timeout = timeout
        self.set_check_timeout(timeout)
        return self

    def get_timeout(self):
        return self.__timeout

    def set_ports(self, ports):
        ValueChecker.is_string(ports)
        self.__ports = ports
        return self

    def get_ports(self):
        return self.__ports

    def set_host_timeout(self, host_timeout):
        ValueChecker.is_number(host_timeout)
        self.__host_timeout = host_timeout
        return self

    def get_host_timeout(self):
        return self.__host_timeout

    def set_min_rate(self, min_rate):
        ValueChecker.is_number(min_rate)
        self.__min_rate = min_rate
        return self

    def get_min_rate(self):
        return self.__min_rate

    def set_max_rate(self, max_rate):
        ValueChecker.is_number(max_rate)
        self.__max_rate = max_rate
        return self

    def get_max_rate(self):
        return self.__max_rate

    def set_max_retries(self, max_retries):
        ValueChecker.is_number(max_retries)
        self.__max_retries = max_retries
        return self

    def get_max_retries(self):
        return self.__max_retries

    def validate(self):
        if None == self.__host:
            raise Exception('You have to set a host.')

    def get_config(self):
        self.validate()
        NmapBase.validate(self)
        config = Check.get_config(self)
        return config

    def get_custom_config(self):
        return ValueMapper.get_property_default_config(self, 'NmapBase', self._command_name, 'command')


class NmapOnlyUDP:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapOnlyUDP'
        self.__only_udp = False

    def set_only_udp(self, only_udp):
        ValueChecker.is_bool(only_udp)
        self.__only_udp = only_udp
        return self

    def get_only_udp(self):
        return self.__only_udp

    def validate(self):
        pass

    def get_config(self):
        NmapOnlyUDP.validate(self)

        return ValueMapper.get_property_default_config(self, NmapOnlyUDP(self)._class_name, self._command_name,
                                                       'command')


class NmapNotOnlyUDP:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotOnlyUDP'
        self.__not_only_udp = False

    def set_not_only_udp(self, not_only_udp):
        ValueChecker.is_bool(not_only_udp)
        self.__not_only_udp = not_only_udp
        return self

    def get_not_only_udp(self):
        return self.__not_only_udp

    def validate(self):
        pass

    def get_config(self):
        NmapNotOnlyUDP.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotOnlyUDP(self)._class_name, self._command_name,
                                                       'command')


class NmapOnlyTCP:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapOnlyTCP'
        self.__only_tcp = False

    def set_only_tcp(self, only_tcp):
        ValueChecker.is_bool(only_tcp)
        self.__only_tcp = only_tcp
        return self

    def get_only_tcp(self):
        return self.__only_tcp

    def validate(self):
        pass

    def get_config(self):
        NmapOnlyTCP.validate(self)

        return ValueMapper.get_property_default_config(self, NmapOnlyTCP(self)._class_name, self._command_name,
                                                       'command')


class NmapNotOnlyTCP:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotOnlyTCP'
        self.__not_only_tcp = False

    def set_not_only_tcp(self, not_only_tcp):
        ValueChecker.is_bool(not_only_tcp)
        self.__not_only_tcp = not_only_tcp
        return self

    def get_not_only_tcp(self):
        return self.__not_only_tcp

    def validate(self):
        pass

    def get_config(self):
        NmapNotOnlyTCP.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotOnlyTCP(self)._class_name, self._command_name,
                                                       'command')


class NmapPN:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapPN'
        self.__pn = False

    def set_pn(self, pn):
        ValueChecker.is_bool(pn)
        self.__pn = pn
        return self

    def get_pn(self):
        return self.__pn

    def validate(self):
        pass

    def get_config(self):
        NmapPN.validate(self)

        return ValueMapper.get_property_default_config(self, NmapPN(self)._class_name, self._command_name, 'command')


class NmapNotPN:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotPN'
        self.__not_pn = False

    def set_not_pn(self, not_pn):
        ValueChecker.is_bool(not_pn)
        self.__not_pn = not_pn
        return self

    def get_not_pn(self):
        return self.__not_pn

    def validate(self):
        pass

    def get_config(self):
        NmapNotPN.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotPN(self)._class_name, self._command_name, 'command')


class NmapFast:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapFast'
        self.__fast = False

    def set_fast(self, fast):
        ValueChecker.is_bool(fast)
        self.__fast = fast
        return self

    def get_fast(self):
        return self.__fast

    def validate(self):
        pass

    def get_config(self):
        NmapFast.validate(self)

        return ValueMapper.get_property_default_config(self, NmapFast(self)._class_name, self._command_name, 'command')


class NmapNotFast:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotFast'
        self.__not_fast = False

    def set_not_fast(self, not_fast):
        ValueChecker.is_bool(not_fast)
        self.__not_fast = not_fast
        return self

    def get_not_fast(self):
        return self.__not_fast

    def validate(self):
        pass

    def get_config(self):
        NmapNotFast.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotFast(self)._class_name, self._command_name,
                                                       'command')
