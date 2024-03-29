#!/usr/bin/python3
# -*- coding: utf-8

from __future__ import annotations

from typing import List, Union

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

    def __init__(self, id: str, class_name: str, command_name: str):
        Check.__init__(self, id, class_name, command_name)
        self._command_name = command_name
        self.__host = []
        self.__exclude = []
        self.__dns_servers = []
        self.__p = []
        self.__exclude_ports = []
        self.__script = []
        self.__script_args = []
        self.__D = []
        self.__proxies = []
        self.__iR = None
        self.__top_ports = None
        self.__port_ratio = None
        self.__version_intensity = None
        self.__osscan_limit = None
        self.__T = None
        self.__min_hostgroup = None
        self.__max_hostgroup = None
        self.__min_rate = None
        self.__max_rate = None
        self.__min_parallelism = None
        self.__max_parallelism = None
        self.__g = None
        self.__data_length = None
        self.__ttl = None
        self.__min_rtt_timeout = None
        self.__max_rtt_timeout = None
        self.__initial_rtt_timeout = None
        self.__max_retries = None
        self.__host_timeout = None
        self.__scan_delay = None
        self.__max_scan_delay = None
        self.__mtu = None
        self.__S = None
        self.__e = None
        self.__data = None
        self.__data_string = None
        self.__ip_options = None
        self.__spoof_mac = None
        self.__datadir = None

        self.__timeout = 12000
        self.set_timeout(12000)
        self.set_check_interval('24h')
        self.add_service_group(ServiceGroup.create('nmap'))
        self.add_service_group(ServiceGroup.create('security'))

    def set_timeout(self, timeout: int) -> NmapBase:
        ValueChecker.is_number(timeout)
        self.__timeout = timeout
        self.set_check_timeout(timeout)
        return self

    def get_timeout(self) -> int:
        return self.__timeout

    def add_host(self, host: str) -> NmapBase:
        ValueChecker.is_string(host)

        if host not in self.__host:
            self.__host.append(host)

        return self

    def remove_host(self, host: str) -> NmapBase:

        if host not in self.__host:
            self.__host.remove(host)

        return self

    def get_host(self) -> List[str]:
        return self.__host

    def add_exclude(self, exclude: str) -> NmapBase:
        ValueChecker.is_string(exclude)

        if exclude not in self.__exclude:
            self.__exclude.append(exclude)

        return self

    def remove_exclude(self, exclude: str) -> NmapBase:
        ValueChecker.is_string(exclude)
        self.__exclude.remove(exclude)

        return self

    def get_exclude(self) -> List[str]:
        return self.__exclude

    def add_dns_servers(self, dns_servers: str) -> NmapBase:
        ValueChecker.is_string(dns_servers)

        if dns_servers not in self.__dns_servers:
            self.__dns_servers.append(dns_servers)

        return self

    def remove_dns_servers(self, dns_servers: str) -> NmapBase:
        if dns_servers in self.__dns_servers:
            self.__dns_servers.remove(dns_servers)

        return self

    def get_dns_servers(self):
        return self.__dns_servers

    def add_p(self, p: str) -> NmapBase:
        ValueChecker.is_string(p)

        if p not in self.__p:
            self.__p.append(p)

        return self

    def remove_p(self, p: str) -> NmapBase:
        ValueChecker.is_string(p)
        if p in self.__p:
            self.__p.remove(p)

        return self

    def get_p(self) -> List[str]:
        return self.__p

    def add_exclude_ports(self, exclude_ports: int) -> NmapBase:

        if exclude_ports not in self.__exclude_ports:
            self.__exclude_ports.append(exclude_ports)

        return self

    def remove_exclude_ports(self, exclude_ports: int) -> NmapBase:
        self.__exclude_ports.remove(exclude_ports)

        return self

    def get_exclude_ports(self) -> List[int]:
        return self.__exclude_ports

    def add_script(self, script: str) -> NmapBase:
        ValueChecker.is_string(script)

        if script not in self.__script:
            self.__script.append(script)

        return self

    def remove_script(self, script: str) -> NmapBase:
        ValueChecker.is_string(script)
        if script in self.__script:
            self.__script.append(script)

        return self

    def get_script(self):
        return self.__script

    def add_script_args(self, script_args: str) -> NmapBase:
        ValueChecker.is_string(script_args)

        if script_args not in self.__script_args:
            self.__script_args.append(script_args)

        return self

    def remove_script_args(self, script_args: str) -> NmapBase:
        ValueChecker.is_string(script_args)
        if script_args not in self.__script_args:
            self.__script_args.append(script_args)

        return self

    def get_script_args(self) -> List[str]:
        return self.__script_args

    def add_D(self, D: str) -> NmapBase:
        ValueChecker.is_string(D)

        if D not in self.__D:
            self.__D.append(D)

        return self

    def remove_D(self, D: str) -> NmapBase:
        ValueChecker.is_string(D)
        self.__D.remove(D)

        return self

    def get_D(self) -> List[str]:
        return self.__D

    def add_proxies(self, proxies: str) -> NmapBase:
        ValueChecker.is_string(proxies)

        if proxies not in self.__proxies:
            self.__proxies.append(proxies)

        return self

    def remove_proxies(self, proxies: str) -> NmapBase:
        ValueChecker.is_string(proxies)
        if proxies in self.__proxies:
            self.__proxies.append(proxies)

        return self

    def get_proxies(self) -> List[str]:
        return self.__proxies

    def set_iR(self, iR: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(iR)
        self.__iR = iR

        return self

    def get_iR(self) -> Union[str, None]:
        return self.__iR

    def set_top_ports(self, top_ports: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(top_ports)
        self.__top_ports = top_ports

        return self

    def get_top_ports(self) -> Union[int, None]:
        return self.__top_ports

    def set_port_ratio(self, port_ratio: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(port_ratio)
        self.__port_ratio = port_ratio

        return self

    def get_port_ratio(self) -> Union[int, None]:
        return self.__port_ratio

    def set_version_intensity(self, version_intensity: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(version_intensity)
        self.__version_intensity = version_intensity

        return self

    def get_version_intensity(self) -> Union[str, None]:
        return self.__version_intensity

    def set_osscan_limit(self, osscan_limit: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(osscan_limit)
        self.__osscan_limit = osscan_limit

        return self

    def get_osscan_limit(self) -> NmapBase:
        return self.__osscan_limit

    def set_T(self, T: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(T)
        self.__T = T

        return self

    def get_T(self) -> Union[str, None]:
        return self.__T

    def set_min_hostgroup(self, min_hostgroup: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(min_hostgroup)
        self.__min_hostgroup = min_hostgroup

        return self

    def get_min_hostgroup(self) -> Union[str, None]:
        return self.__min_hostgroup

    def set_max_hostgroup(self, max_hostgroup: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(max_hostgroup)
        self.__max_hostgroup = max_hostgroup

        return self

    def get_max_hostgroup(self) -> Union[str, None]:
        return self.__max_hostgroup

    def set_min_rate(self, min_rate: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(min_rate)
        self.__min_rate = min_rate

        return self

    def get_min_rate(self) -> Union[str, None]:
        return self.__min_rate

    def set_max_rate(self, max_rate: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(max_rate)
        self.__max_rate = max_rate

        return self

    def get_max_rate(self) -> Union[str, None]:
        return self.__max_rate

    def set_min_parallelism(self, min_parallelism: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(min_parallelism)
        self.__min_parallelism = min_parallelism

        return self

    def get_min_parallelism(self) -> Union[str, None]:
        return self.__min_parallelism

    def set_max_parallelism(self, max_parallelism: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(max_parallelism)
        self.__max_parallelism = max_parallelism

        return self

    def get_max_parallelism(self) -> Union[str, None]:
        return self.__max_parallelism

    def set_g(self, g: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(g)
        self.__g = g

        return self

    def get_g(self) -> Union[str, None]:
        return self.__g

    def set_data_length(self, data_length: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(data_length)
        self.__data_length = data_length

        return self

    def get_data_length(self) -> Union[str, None]:
        return self.__data_length

    def set_ttl(self, ttl: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(ttl)
        self.__ttl = ttl

        return self

    def get_ttl(self) -> Union[str, None]:
        return self.__ttl

    def set_min_rtt_timeout(self, min_rtt_timeout: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(min_rtt_timeout)
        self.__min_rtt_timeout = min_rtt_timeout

        return self

    def get_min_rtt_timeout(self) -> Union[int, None]:
        return self.__min_rtt_timeout

    def set_max_rtt_timeout(self, max_rtt_timeout: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(max_rtt_timeout)
        self.__max_rtt_timeout = max_rtt_timeout

        return self

    def get_max_rtt_timeout(self) -> Union[int, None]:
        return self.__max_rtt_timeout

    def set_initial_rtt_timeout(self, initial_rtt_timeout: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(initial_rtt_timeout)
        self.__initial_rtt_timeout = initial_rtt_timeout

        return self

    def get_initial_rtt_timeout(self) -> Union[int, None]:
        return self.__initial_rtt_timeout

    def set_max_retries(self, max_retries: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(max_retries)
        self.__max_retries = max_retries

        return self

    def get_max_retries(self) -> Union[int, None]:
        return self.__max_retries

    def set_host_timeout(self, host_timeout: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(host_timeout)
        self.__host_timeout = host_timeout

        return self

    def get_host_timeout(self) -> Union[int, None]:
        return self.__host_timeout

    def set_scan_delay(self, scan_delay: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(scan_delay)
        self.__scan_delay = scan_delay

        return self

    def get_scan_delay(self) -> Union[int, None]:
        return self.__scan_delay

    def set_max_scan_delay(self, max_scan_delay: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(max_scan_delay)
        self.__max_scan_delay = max_scan_delay

        return self

    def get_max_scan_delay(self) -> Union[int, None]:
        return self.__max_scan_delay

    def set_mtu(self, mtu: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(mtu)
        self.__mtu = mtu

        return self

    def get_mtu(self) -> Union[int, None]:
        return self.__mtu

    def set_S(self, S: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(S)
        self.__S = S

        return self

    def get_S(self) -> Union[int, None]:
        return self.__S

    def set_e(self, e: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(e)
        self.__e = e

        return self

    def get_e(self) -> Union[int, None]:
        return self.__e

    def set_data(self, data: Union[int, None]) -> NmapBase:
        ValueChecker.is_number(data)
        self.__data = data

        return self

    def get_data(self) -> Union[int, None]:
        return self.__data

    def set_data_string(self, data_string: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(data_string)
        self.__data_string = data_string

        return self

    def get_data_string(self) -> Union[str, None]:
        return self.__data_string

    def set_ip_options(self, ip_options: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(ip_options)
        self.__ip_options = ip_options

        return self

    def get_ip_options(self) -> Union[str, None]:
        return self.__ip_options

    def set_spoof_mac(self, spoof_mac: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(spoof_mac)
        self.__spoof_mac = spoof_mac

        return self

    def get_spoof_mac(self) -> Union[str, None]:
        return self.__spoof_mac

    def set_datadir(self, datadir: Union[str, None]) -> NmapBase:
        ValueChecker.is_string(datadir)
        self.__datadir = datadir

        return self

    def get_datadir(self) -> Union[str, None]:
        return self.__datadir

    def validate(self):
        if 0 == len(self.__host):
            raise Exception('You have to set a host.')

    def get_config(self) -> str:
        self.validate()
        NmapBase.validate(self)
        config = Check.get_config(self)
        return config

    def get_custom_config(self) -> str:
        return ValueMapper.get_property_default_config(self, 'NmapBase', self._command_name, 'command')


class NmapScriptExecutor:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapScriptExecutor'
        self.__ignored_ports = []

    def add_ignored_port(self, port: int) -> NmapScriptExecutor:
        ValueChecker.is_number(port)
        if port not in self.__ignored_ports:
            self.__ignored_ports.append(port)

        return self

    def remove_ignored_port(self, port: int) -> NmapScriptExecutor:
        ValueChecker.is_number(port)
        if port not in self.__ignored_ports:
            self.__ignored_ports.remove(port)

        return self

    def get_ignored_ports(self) -> List[int]:
        return self.__ignored_ports

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapScriptExecutor.validate(self)

        return ValueMapper.get_property_default_config(self, NmapScriptExecutor(self)._class_name, self._command_name,
                                                       'command')


class NmapScanUDP:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapScanUDP'
        self.__scan_udp = False

    def set_scan_udp(self, scan_udp: bool) -> NmapScanUDP:
        ValueChecker.is_bool(scan_udp)
        self.__scan_udp = scan_udp
        return self

    def get_scan_udp(self) -> bool:
        return self.__scan_udp

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapScanUDP.validate(self)

        return ValueMapper.get_property_default_config(self, NmapScanUDP(self)._class_name, self._command_name,
                                                       'command')


class NmapNotScanUDP:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotScanUDP'
        self.__not_scan_udp = False

    def set_not_scan_udp(self, not_scan_udp: bool) -> NmapNotScanUDP:
        ValueChecker.is_bool(not_scan_udp)
        self.__not_scan_udp = not_scan_udp
        return self

    def get_not_scan_udp(self) -> bool:
        return self.__not_scan_udp

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotScanUDP.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotScanUDP(self)._class_name, self._command_name,
                                                       'command')


class NmapScanTCP:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapScanTCP'
        self.__scan_tcp = False

    def set_scan_tcp(self, scan_tcp: bool) -> NmapScanTCP:
        ValueChecker.is_bool(scan_tcp)
        self.__scan_tcp = scan_tcp
        return self

    def get_scan_tcp(self) -> bool:
        return self.__scan_tcp

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapScanTCP.validate(self)

        return ValueMapper.get_property_default_config(self, NmapScanTCP(self)._class_name, self._command_name,
                                                       'command')


class NmapNotScanTCP:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotScanTCP'
        self.__not_scan_tcp = False

    def set_not_scan_tcp(self, not_scan_tcp: bool) -> NmapNotScanTCP:
        ValueChecker.is_bool(not_scan_tcp)
        self.__not_scan_tcp = not_scan_tcp
        return self

    def get_not_scan_tcp(self) -> bool:
        return self.__not_scan_tcp

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotScanTCP.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotScanTCP(self)._class_name, self._command_name,
                                                       'command')


class NmapN:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapN'
        self.__n = False

    def set_n(self, enabled: bool) -> NmapN:
        ValueChecker.is_bool(enabled)
        self.__n = enabled
        return self

    def get_n(self) -> bool:
        return self.__n

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapN.validate(self)

        return ValueMapper.get_property_default_config(self, NmapN(self)._class_name, self._command_name, 'command')


class NmapNotN:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotN'
        self.__not_n = False

    def set_not_n(self, not_enabled: bool) -> NmapNotN:
        ValueChecker.is_bool(not_enabled)
        self.__not_n = not_enabled
        return self

    def get_not_n(self) -> bool:
        return self.__not_n

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotN.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotN(self)._class_name, self._command_name, 'command')


class Nmapr:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'Nmapr'
        self.__r = False

    def set_r(self, enabled: bool) -> Nmapr:
        ValueChecker.is_bool(enabled)
        self.__r = enabled
        return self

    def get_r(self) -> bool:
        return self.__r

    def validate(self):
        pass

    def get_config(self) -> str:
        Nmapr.validate(self)

        return ValueMapper.get_property_default_config(self, Nmapr(self)._class_name, self._command_name, 'command')


class NmapNotr:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotr'
        self.__not_r = False

    def set_not_r(self, not_enabled: bool) -> NmapNotr:
        ValueChecker.is_bool(not_enabled)
        self.__not_r = not_enabled
        return self

    def get_not_r(self) -> bool:
        return self.__not_r

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotr.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotr(self)._class_name, self._command_name, 'command')


class NmapSystemDns:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapSystemDns'
        self.__system_dns = False

    def set_system_dns(self, enabled: bool) -> NmapSystemDns:
        ValueChecker.is_bool(enabled)
        self.__system_dns = enabled
        return self

    def get_system_dns(self) -> bool:
        return self.__system_dns

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapSystemDns.validate(self)

        return ValueMapper.get_property_default_config(self, NmapSystemDns(self)._class_name, self._command_name,
                                                       'command')


class NmapNotSystemDns:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotSystemDns'
        self.__not_system_dns = False

    def set_not_system_dns(self, not_enabled: bool) -> NmapNotSystemDns:
        ValueChecker.is_bool(not_enabled)
        self.__not_system_dns = not_enabled
        return self

    def get_not_system_dns(self) -> bool:
        return self.__not_system_dns

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotSystemDns.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotSystemDns(self)._class_name, self._command_name,
                                                       'command')


class NmapTraceroute:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapTraceroute'
        self.__traceroute = False

    def set_traceroute(self, enabled: bool) -> NmapTraceroute:
        ValueChecker.is_bool(enabled)
        self.__traceroute = enabled
        return self

    def get_traceroute(self) -> bool:
        return self.__traceroute

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapTraceroute.validate(self)

        return ValueMapper.get_property_default_config(self, NmapTraceroute(self)._class_name, self._command_name,
                                                       'command')


class NmapNotTraceroute:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotTraceroute'
        self.__not_traceroute = False

    def set_not_traceroute(self, not_enabled: bool) -> NmapNotTraceroute:
        ValueChecker.is_bool(not_enabled)
        self.__not_traceroute = not_enabled
        return self

    def get_not_traceroute(self) -> bool:
        return self.__not_traceroute

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotTraceroute.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotTraceroute(self)._class_name, self._command_name,
                                                       'command')


class NmapF:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapF'
        self.__F = False

    def set_F(self, enabled: bool) -> NmapF:
        ValueChecker.is_bool(enabled)
        self.__F = enabled
        return self

    def get_F(self) -> bool:
        return self.__F

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapF.validate(self)

        return ValueMapper.get_property_default_config(self, NmapF(self)._class_name, self._command_name, 'command')


class NmapNotF:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotF'
        self.__not_F = False

    def set_not_F(self, not_enabled: bool) -> NmapNotF:
        ValueChecker.is_bool(not_enabled)
        self.__not_F = not_enabled
        return self

    def get_not_F(self) -> bool:
        return self.__not_F

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotF.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotF(self)._class_name, self._command_name, 'command')


class NmapR:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapR'
        self.__r = False

    def set_r(self, enabled: bool) -> NmapR:
        ValueChecker.is_bool(enabled)
        self.__r = enabled
        return self

    def get_r(self) -> bool:
        return self.__r

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapR.validate(self)

        return ValueMapper.get_property_default_config(self, NmapR(self)._class_name, self._command_name, 'command')


class NmapNotR:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotR'
        self.__not_r = False

    def set_not_r(self, not_enabled: bool) -> NmapNotR:
        ValueChecker.is_bool(not_enabled)
        self.__not_r = not_enabled
        return self

    def get_not_r(self) -> bool:
        return self.__not_r

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotR.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotR(self)._class_name, self._command_name, 'command')


class NmapSV:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapSV'
        self.__sV = False

    def set_sV(self, enabled: bool) -> NmapSV:
        ValueChecker.is_bool(enabled)
        self.__sV = enabled
        return self

    def get_sV(self) -> bool:
        return self.__sV

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapSV.validate(self)

        return ValueMapper.get_property_default_config(self, NmapSV(self)._class_name, self._command_name, 'command')


class NmapNotSV:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotSV'
        self.__not_sV = False

    def set_not_sV(self, not_enabled: bool) -> NmapNotSV:
        ValueChecker.is_bool(not_enabled)
        self.__not_sV = not_enabled
        return self

    def get_not_sV(self) -> bool:
        return self.__not_sV

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotSV.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotSV(self)._class_name, self._command_name, 'command')


class NmapVersionLight:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapVersionLight'
        self.__version_light = False

    def set_version_light(self, enabled: bool) -> NmapVersionLight:
        ValueChecker.is_bool(enabled)
        self.__version_light = enabled
        return self

    def get_version_light(self) -> bool:
        return self.__version_light

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapVersionLight.validate(self)

        return ValueMapper.get_property_default_config(self, NmapVersionLight(self)._class_name, self._command_name,
                                                       'command')


class NmapNotVersionLight:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotVersionLight'
        self.__not_version_light = False

    def set_not_version_light(self, not_enabled: bool) -> NmapNotVersionLight:
        ValueChecker.is_bool(not_enabled)
        self.__not_version_light = not_enabled
        return self

    def get_not_version_light(self) -> bool:
        return self.__not_version_light

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotVersionLight.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotVersionLight(self)._class_name, self._command_name,
                                                       'command')


class NmapVersionAll:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapVersionAll'
        self.__version_all = False

    def set_version_all(self, enabled: bool) -> NmapVersionAll:
        ValueChecker.is_bool(enabled)
        self.__version_all = enabled
        return self

    def get_version_all(self) -> bool:
        return self.__version_all

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapVersionAll.validate(self)

        return ValueMapper.get_property_default_config(self, NmapVersionAll(self)._class_name, self._command_name,
                                                       'command')


class NmapNotVersionAll:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotVersionAll'
        self.__not_version_all = False

    def set_not_version_all(self, not_enabled: bool) -> NmapNotVersionAll:
        ValueChecker.is_bool(not_enabled)
        self.__not_version_all = not_enabled
        return self

    def get_not_version_all(self) -> bool:
        return self.__not_version_all

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotVersionAll.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotVersionAll(self)._class_name, self._command_name,
                                                       'command')


class NmapVersionTrace:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapVersionTrace'
        self.__version_trace = False

    def set_version_trace(self, enabled: bool) -> NmapVersionTrace:
        ValueChecker.is_bool(enabled)
        self.__version_trace = enabled
        return self

    def get_version_trace(self) -> bool:
        return self.__version_trace

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapVersionTrace.validate(self)

        return ValueMapper.get_property_default_config(self, NmapVersionTrace(self)._class_name, self._command_name,
                                                       'command')


class NmapNotVersionTrace:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotVersionTrace'
        self.__not_version_trace = False

    def set_not_version_trace(self, not_enabled: bool) -> NmapNotVersionTrace:
        ValueChecker.is_bool(not_enabled)
        self.__not_version_trace = not_enabled
        return self

    def get_not_version_trace(self) -> bool:
        return self.__not_version_trace

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotVersionTrace.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotVersionTrace(self)._class_name, self._command_name,
                                                       'command')


class NmapSC:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapSC'
        self.__sC = False

    def set_sC(self, enabled: bool) -> NmapSC:
        ValueChecker.is_bool(enabled)
        self.__sC = enabled
        return self

    def get_sC(self) -> bool:
        return self.__sC

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapSC.validate(self)

        return ValueMapper.get_property_default_config(self, NmapSC(self)._class_name, self._command_name, 'command')


class NmapNotSC:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotSC'
        self.__not_sC = False

    def set_not_sC(self, not_enabled: bool) -> NmapNotSC:
        ValueChecker.is_bool(not_enabled)
        self.__not_sC = not_enabled
        return self

    def get_not_sC(self) -> bool:
        return self.__not_sC

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotSC.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotSC(self)._class_name, self._command_name, 'command')


class NmapScriptTrace:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapScriptTrace'
        self.__script_trace = False

    def set_script_trace(self, enabled: bool) -> NmapScriptTrace:
        ValueChecker.is_bool(enabled)
        self.__script_trace = enabled
        return self

    def get_script_trace(self) -> bool:
        return self.__script_trace

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapScriptTrace.validate(self)

        return ValueMapper.get_property_default_config(self, NmapScriptTrace(self)._class_name, self._command_name,
                                                       'command')


class NmapNotScriptTrace:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotScriptTrace'
        self.__not_script_trace = False

    def set_not_script_trace(self, not_enabled: bool) -> NmapNotScriptTrace:
        ValueChecker.is_bool(not_enabled)
        self.__not_script_trace = not_enabled
        return self

    def get_not_script_trace(self) -> bool:
        return self.__not_script_trace

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotScriptTrace.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotScriptTrace(self)._class_name, self._command_name,
                                                       'command')


class NmapO:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapO'
        self.__O = False

    def set_O(self, enabled: bool) -> NmapO:
        ValueChecker.is_bool(enabled)
        self.__O = enabled
        return self

    def get_O(self) -> bool:
        return self.__O

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapO.validate(self)

        return ValueMapper.get_property_default_config(self, NmapO(self)._class_name, self._command_name, 'command')


class NmapNotO:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotO'
        self.__not_O = False

    def set_not_O(self, not_enabled: bool) -> NmapNotO:
        ValueChecker.is_bool(not_enabled)
        self.__not_O = not_enabled
        return self

    def get_not_O(self) -> bool:
        return self.__not_O

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotO.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotO(self)._class_name, self._command_name, 'command')


class NmapOsscanGuess:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapOsscanGuess'
        self.__osscan_guess = False

    def set_osscan_guess(self, enabled: bool) -> NmapOsscanGuess:
        ValueChecker.is_bool(enabled)
        self.__osscan_guess = enabled
        return self

    def get_osscan_guess(self) -> bool:
        return self.__osscan_guess

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapOsscanGuess.validate(self)

        return ValueMapper.get_property_default_config(self, NmapOsscanGuess(self)._class_name, self._command_name,
                                                       'command')


class NmapNotOsscanGuess:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotOsscanGuess'
        self.__not_osscan_guess = False

    def set_not_osscan_guess(self, not_enabled: bool) -> NmapNotOsscanGuess:
        ValueChecker.is_bool(not_enabled)
        self.__not_osscan_guess = not_enabled
        return self

    def get_not_osscan_guess(self) -> bool:
        return self.__not_osscan_guess

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotOsscanGuess.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotOsscanGuess(self)._class_name, self._command_name,
                                                       'command')


class NmapBadsum:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapBadsum'
        self.__badsum = False

    def set_badsum(self, enabled: bool) -> NmapBadsum:
        ValueChecker.is_bool(enabled)
        self.__badsum = enabled
        return self

    def get_badsum(self) -> bool:
        return self.__badsum

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapBadsum.validate(self)

        return ValueMapper.get_property_default_config(self, NmapBadsum(self)._class_name, self._command_name,
                                                       'command')


class NmapNotBadsum:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotBadsum'
        self.__not_badsum = False

    def set_not_badsum(self, not_enabled: bool) -> NmapNotBadsum:
        ValueChecker.is_bool(not_enabled)
        self.__not_badsum = not_enabled
        return self

    def get_not_badsum(self) -> bool:
        return self.__not_badsum

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotBadsum.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotBadsum(self)._class_name, self._command_name,
                                                       'command')


class Nmap6:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'Nmap6'
        self.__6 = False

    def set_6(self, enabled: bool) -> Nmap6:
        ValueChecker.is_bool(enabled)
        self.__6 = enabled
        return self

    def get_6(self) -> bool:
        return self.__6

    def validate(self):
        pass

    def get_config(self) -> str:
        Nmap6.validate(self)

        return ValueMapper.get_property_default_config(self, Nmap6(self)._class_name, self._command_name, 'command')


class NmapNot6:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNot6'
        self.__not_6 = False

    def set_not_6(self, not_enabled: bool) -> NmapNot6:
        ValueChecker.is_bool(not_enabled)
        self.__not_6 = not_enabled
        return self

    def get_not_6(self) -> bool:
        return self.__not_6

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNot6.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNot6(self)._class_name, self._command_name, 'command')


class NmapA:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapA'
        self.__A = False

    def set_A(self, enabled: bool) -> NmapA:
        ValueChecker.is_bool(enabled)
        self.__A = enabled
        return self

    def get_A(self) -> bool:
        return self.__A

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapA.validate(self)

        return ValueMapper.get_property_default_config(self, NmapA(self)._class_name, self._command_name, 'command')


class NmapNotA:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotA'
        self.__not_A = False

    def set_not_A(self, not_enabled: bool) -> NmapNotA:
        ValueChecker.is_bool(not_enabled)
        self.__not_A = not_enabled
        return self

    def get_not_A(self) -> bool:
        return self.__not_A

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotA.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotA(self)._class_name, self._command_name, 'command')


class NmapSendEth:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapSendEth'
        self.__send_eth = False

    def set_send_eth(self, enabled: bool) -> NmapSendEth:
        ValueChecker.is_bool(enabled)
        self.__send_eth = enabled
        return self

    def get_send_eth(self) -> bool:
        return self.__send_eth

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapSendEth.validate(self)

        return ValueMapper.get_property_default_config(self, NmapSendEth(self)._class_name, self._command_name,
                                                       'command')


class NmapNotSendEth:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotSendEth'
        self.__not_send_eth = False

    def set_not_send_eth(self, not_enabled: bool) -> NmapNotSendEth:
        ValueChecker.is_bool(not_enabled)
        self.__not_send_eth = not_enabled
        return self

    def get_not_send_eth(self) -> bool:
        return self.__not_send_eth

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotSendEth.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotSendEth(self)._class_name, self._command_name,
                                                       'command')


class NmapSendIp:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapSendIp'
        self.__send_ip = False

    def set_send_ip(self, enabled: bool) -> NmapSendIp:
        ValueChecker.is_bool(enabled)
        self.__send_ip = enabled
        return self

    def get_send_ip(self) -> bool:
        return self.__send_ip

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapSendIp.validate(self)

        return ValueMapper.get_property_default_config(self, NmapSendIp(self)._class_name, self._command_name,
                                                       'command')


class NmapNotSendIp:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotSendIp'
        self.__not_send_ip = False

    def set_not_send_ip(self, not_enabled: bool) -> NmapNotSendIp:
        ValueChecker.is_bool(not_enabled)
        self.__not_send_ip = not_enabled
        return self

    def get_not_send_ip(self) -> bool:
        return self.__not_send_ip

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotSendIp.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotSendIp(self)._class_name, self._command_name,
                                                       'command')


class NmapPrivileged:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapPrivileged'
        self.__privileged = False

    def set_privileged(self, enabled: bool) -> NmapPrivileged:
        ValueChecker.is_bool(enabled)
        self.__privileged = enabled
        return self

    def get_privileged(self) -> bool:
        return self.__privileged

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapPrivileged.validate(self)

        return ValueMapper.get_property_default_config(self, NmapPrivileged(self)._class_name, self._command_name,
                                                       'command')


class NmapNotPrivileged:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotPrivileged'
        self.__not_privileged = False

    def set_not_privileged(self, not_enabled: bool) -> NmapNotPrivileged:
        ValueChecker.is_bool(not_enabled)
        self.__not_privileged = not_enabled
        return self

    def get_not_privileged(self) -> bool:
        return self.__not_privileged

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotPrivileged.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotPrivileged(self)._class_name, self._command_name,
                                                       'command')


class NmapPn:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapPn'
        self.__Pn = False

    def set_Pn(self, enabled: bool) -> NmapPn:
        ValueChecker.is_bool(enabled)
        self.__Pn = enabled
        return self

    def get_Pn(self) -> bool:
        return self.__Pn

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapPn.validate(self)

        return ValueMapper.get_property_default_config(self, NmapPn(self)._class_name, self._command_name, 'command')


class NmapNotPn:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotPn'
        self.__not_Pn = False

    def set_not_Pn(self, not_enabled: bool) -> NmapNotPn:
        ValueChecker.is_bool(not_enabled)
        self.__not_Pn = not_enabled
        return self

    def get_not_Pn(self) -> bool:
        return self.__not_Pn

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotPn.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotPn(self)._class_name, self._command_name, 'command')


class NmapUnprivileged:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapUnprivileged'
        self.__unprivileged = False

    def set_unprivileged(self, enabled: bool) -> NmapUnprivileged:
        ValueChecker.is_bool(enabled)
        self.__unprivileged = enabled
        return self

    def get_unprivileged(self) -> bool:
        return self.__unprivileged

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapUnprivileged.validate(self)

        return ValueMapper.get_property_default_config(self, NmapUnprivileged(self)._class_name, self._command_name,
                                                       'command')


class NmapNotUnprivileged:

    def __init__(self, command_name):
        self._command_name = command_name
        self._class_name = 'NmapNotUnprivileged'
        self.__not_unprivileged = False

    def set_not_unprivileged(self, not_enabled: bool) -> NmapNotUnprivileged:
        ValueChecker.is_bool(not_enabled)
        self.__not_unprivileged = not_enabled
        return self

    def get_not_unprivileged(self) -> bool:
        return self.__not_unprivileged

    def validate(self):
        pass

    def get_config(self) -> str:
        NmapNotUnprivileged.validate(self)

        return ValueMapper.get_property_default_config(self, NmapNotUnprivileged(self)._class_name, self._command_name,
                                                       'command')
