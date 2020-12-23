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

from icinga2confgen.Commands.MonitoringPlugins.MonitoringPluginCommand import MonitoringPluginCommand


class NmapCommand(MonitoringPluginCommand):

    def __init__(self, id, command_name, single_host=True, scan_udp=True, scan_tcp=True, n=True, R=True,
                 system_dns=True, traceroute=True, F=True, r=True, sV=True, version_light=True, version_all=True,
                 version_trace=True, sC=True, script_trace=True, O=True, osscan_guess=True, badsum=True, ipv6=True,
                 A=True,
                 send_eth=True, send_ip=True, privileged=True, Pn=True, unprivileged=True):
        MonitoringPluginCommand.__init__(self, id)
        self.__command_name = command_name
        self.__single_host = single_host
        self.__scan_udp = scan_udp
        self.__scan_tcp = scan_tcp
        self.__n = n
        self.__R = R
        self.__system_dns = system_dns
        self.__traceroute = traceroute
        self.__F = F
        self.__r = r
        self.__sV = sV
        self.__version_light = version_light
        self.__version_all = version_all
        self.__version_trace = version_trace
        self.__sC = sC
        self.__script_trace = script_trace
        self.__O = O
        self.__osscan_guess = osscan_guess
        self.__badsum = badsum
        self.__6 = ipv6
        self.__A = A
        self.__send_eth = send_eth
        self.__send_ip = send_ip
        self.__privileged = privileged
        self.__Pn = Pn
        self.__unprivileged = unprivileged

    @staticmethod
    def create(id, force_create=False):
        raise Exception('Can\'t create NmapCommand, use child classes instead.')

    def get_arguments(self):
        config = """
    "--ignore-port" = {
      value = "$command_""" + self.__command_name + """_ignored_ports$"
      set_if = {{ macro("$command_""" + self.__command_name + """_ignored_ports$") != false }}
      repeat_key = true
    }
    "--timeout" = {
      value = "$command_""" + self.__command_name + """_timeout$"
      set_if = {{ macro("$command_""" + self.__command_name + """_timeout$") != false }}
    }
     "--host" = {
      value = "$command_""" + self.__command_name + """_host$"
      set_if = {{ macro("$command_""" + self.__command_name + """_host$") != false }}
      repeat_key = true
    }
    "--exclude" = {
      value = "$command_""" + self.__command_name + """_exclude$"
      set_if = {{ macro("$command_""" + self.__command_name + """_exclude$") != false }}
      repeat_key = true
    }
    "--dns-servers" = {
      value = "$command_""" + self.__command_name + """_dns_servers$"
      set_if = {{ macro("$command_""" + self.__command_name + """_dns_servers$") != false }}
      repeat_key = true
    }
    "-p" = {
      value = "$command_""" + self.__command_name + """_p$"
      set_if = {{ macro("$command_""" + self.__command_name + """_p$") != false }}
      repeat_key = true
    }
    "--exclude-ports" = {
      value = "$command_""" + self.__command_name + """_exclude_ports$"
      set_if = {{ macro("$command_""" + self.__command_name + """_exclude_ports$") != false }}
      repeat_key = true
    }
    "--script" = {
      value = "$command_""" + self.__command_name + """_script$"
      set_if = {{ macro("$command_""" + self.__command_name + """_script$") != false }}
      repeat_key = true
    }
    "--script-args" = {
      value = "$command_""" + self.__command_name + """_script_args$"
      set_if = {{ macro("$command_""" + self.__command_name + """_script_args$") != false }}
      repeat_key = true
    }
    "-D" = {
      value = "$command_""" + self.__command_name + """_D$"
      set_if = {{ macro("$command_""" + self.__command_name + """_D$") != false }}
      repeat_key = true
    }
    "--proxies" = {
      value = "$command_""" + self.__command_name + """_proxies$"
      set_if = {{ macro("$command_""" + self.__command_name + """_proxies$") != false }}
      repeat_key = true
    }
    "-iR" = {
      value = "$command_""" + self.__command_name + """_iR$"
      set_if = {{ macro("$command_""" + self.__command_name + """_iR$") != false }}
    }
    "--top-ports" = {
      value = "$command_""" + self.__command_name + """_top_ports$"
      set_if = {{ macro("$command_""" + self.__command_name + """_top_ports$") != false }}
    }
    "--port-ratio" = {
      value = "$command_""" + self.__command_name + """_port_ratio$"
      set_if = {{ macro("$command_""" + self.__command_name + """_port_ratio$") != false }}
    }
    "--version-intensity" = {
      value = "$command_""" + self.__command_name + """_version_intensity$"
      set_if = {{ macro("$command_""" + self.__command_name + """_version_intensity$") != false }}
    }
    "--osscan-limit" = {
      value = "$command_""" + self.__command_name + """_osscan_limit$"
      set_if = {{ macro("$command_""" + self.__command_name + """_osscan_limit$") != false }}
    }
    "-T" = {
      value = "$command_""" + self.__command_name + """_T$"
      set_if = {{ macro("$command_""" + self.__command_name + """_T$") != false }}
    }
    "--min-hostgroup" = {
      value = "$command_""" + self.__command_name + """_min_hostgroup$"
      set_if = {{ macro("$command_""" + self.__command_name + """_min_hostgroup$") != false }}
    }
    "--max-hostgroup" = {
      value = "$command_""" + self.__command_name + """_max_hostgroup$"
      set_if = {{ macro("$command_""" + self.__command_name + """_max_hostgroup$") != false }}
    }
    "--min-rate" = {
      value = "$command_""" + self.__command_name + """_min_rate$"
      set_if = {{ macro("$command_""" + self.__command_name + """_min_rate$") != false }}
    }
    "--max-rate" = {
      value = "$command_""" + self.__command_name + """_max_rate$"
      set_if = {{ macro("$command_""" + self.__command_name + """_max_rate$") != false }}
    }
    "--min-parallelism" = {
      value = "$command_""" + self.__command_name + """_min_parallelism$"
      set_if = {{ macro("$command_""" + self.__command_name + """_min_parallelism$") != false }}
    }
    "--max-parallelism" = {
      value = "$command_""" + self.__command_name + """_max_parallelism$"
      set_if = {{ macro("$command_""" + self.__command_name + """_max_parallelism$") != false }}
    }
    "-g" = {
      value = "$command_""" + self.__command_name + """_g$"
      set_if = {{ macro("$command_""" + self.__command_name + """_g$") != false }}
    }
    "--data-length" = {
      value = "$command_""" + self.__command_name + """_data_length$"
      set_if = {{ macro("$command_""" + self.__command_name + """_data_length$") != false }}
    }
    "--ttl" = {
      value = "$command_""" + self.__command_name + """_ttl$"
      set_if = {{ macro("$command_""" + self.__command_name + """_ttl$") != false }}
    }
    "--min-rtt-timeout" = {
      value = "$command_""" + self.__command_name + """_min_rtt_timeout$"
      set_if = {{ macro("$command_""" + self.__command_name + """_min_rtt_timeout$") != false }}
    }
    "--max-rtt-timeout" = {
      value = "$command_""" + self.__command_name + """_max_rtt_timeout$"
      set_if = {{ macro("$command_""" + self.__command_name + """_max_rtt_timeout$") != false }}
    }
    "--initial-rtt-timeout" = {
      value = "$command_""" + self.__command_name + """_initial_rtt_timeout$"
      set_if = {{ macro("$command_""" + self.__command_name + """_initial_rtt_timeout$") != false }}
    }
    "--max-retries" = {
      value = "$command_""" + self.__command_name + """_max_retries$"
      set_if = {{ macro("$command_""" + self.__command_name + """_max_retries$") != false }}
    }
    "--host-timeout" = {
      value = "$command_""" + self.__command_name + """_host_timeout$"
      set_if = {{ macro("$command_""" + self.__command_name + """_host_timeout$") != false }}
    }
    "--scan-delay" = {
      value = "$command_""" + self.__command_name + """_scan_delay$"
      set_if = {{ macro("$command_""" + self.__command_name + """_scan_delay$") != false }}
    }
    "--max-scan-delay" = {
      value = "$command_""" + self.__command_name + """_max_scan_delay$"
      set_if = {{ macro("$command_""" + self.__command_name + """_max_scan_delay$") != false }}
    }
    "--mtu" = {
      value = "$command_""" + self.__command_name + """_mtu$"
      set_if = {{ macro("$command_""" + self.__command_name + """_mtu$") != false }}
    }
    "-S" = {
      value = "$command_""" + self.__command_name + """_S$"
      set_if = {{ macro("$command_""" + self.__command_name + """_S$") != false }}
    }
    "-e" = {
      value = "$command_""" + self.__command_name + """_e$"
      set_if = {{ macro("$command_""" + self.__command_name + """_e$") != false }}
    }
    "--data" = {
      value = "$command_""" + self.__command_name + """_data$"
      set_if = {{ macro("$command_""" + self.__command_name + """_data$") != false }}
    }
    "--data-string" = {
      value = "$command_""" + self.__command_name + """_data_string$"
      set_if = {{ macro("$command_""" + self.__command_name + """_data_string$") != false }}
    }
    "--ip-options" = {
      value = "$command_""" + self.__command_name + """_ip_options$"
      set_if = {{ macro("$command_""" + self.__command_name + """_ip_options$") != false }}
    }
    "--spoof-mac" = {
      value = "$command_""" + self.__command_name + """_spoof_mac$"
      set_if = {{ macro("$command_""" + self.__command_name + """_spoof_mac$") != false }}
    }
    "--datadir" = {
      value = "$command_""" + self.__command_name + """_datadir$"
      set_if = {{ macro("$command_""" + self.__command_name + """_datadir$") != false }}
    }

"""
        if self.__single_host:
            config += """
    "--single-host" = {}
"""
        if self.__scan_udp:
            config += """
    "--scan-udp" = {
      set_if = "$command_""" + self.__command_name + """_scan_udp$"
    }
"""
        else:
            config += """
    "--not-scan-udp" = {
      set_if = "$command_""" + self.__command_name + """_not_scan_udp$"
    }
"""

        if self.__scan_tcp:
            config += """
    "--scan-tcp" = {
      set_if = "$command_""" + self.__command_name + """_scan_tcp$"
    }
"""
        else:
            config += """
    "--not-scan-tcp" = {
      set_if = "$command_""" + self.__command_name + """_not_scan_tcp$"
    }
"""

        if self.__n:
            config += """
    "-n" = {
      set_if = "$command_""" + self.__command_name + """_n$"
    }
"""
        else:
            config += """
    "-not-n" = {
      set_if = "$command_""" + self.__command_name + """_not_n$"
    }
"""
        if self.__R:
            config += """
    "-R" = {
      set_if = "$command_""" + self.__command_name + """_R$"
    }
"""
        else:
            config += """
    "-not-R" = {
      set_if = "$command_""" + self.__command_name + """_not_R$"
    }
"""
        if self.__system_dns:
            config += """
    "--system-dns" = {
      set_if = "$command_""" + self.__command_name + """_system_dns$"
    }
"""

        else:
            config += """
    "--not-system-dns" = {
      set_if = "$command_""" + self.__command_name + """_not_system_dns$"
    }
"""
        if self.__traceroute:
            config += """
    "--traceroute" = {
      set_if = "$command_""" + self.__command_name + """_traceroute$"
    }
"""

        else:
            config += """
    "--not-traceroute" = {
      set_if = "$command_""" + self.__command_name + """_not_traceroute$"
    }
"""
        if self.__F:
            config += """
    "-F" = {
      set_if = "$command_""" + self.__command_name + """_F$"
    }
"""
        else:
            config += """
    "-not-F" = {
      set_if = "$command_""" + self.__command_name + """_not_F$"
    }
"""
        if self.__r:
            config += """
    "-r" = {
      set_if = "$command_""" + self.__command_name + """_r$"
    }
"""
        else:
            config += """
    "-not-r" = {
      set_if = "$command_""" + self.__command_name + """_not_r$"
    }
"""
        if self.__sV:
            config += """
    "-sV" = {
      set_if = "$command_""" + self.__command_name + """_sV$"
    }
"""
        else:
            config += """
    "-not-sV" = {
      set_if = "$command_""" + self.__command_name + """_not_sV$"
    }
"""
        if self.__version_light:
            config += """
    "--version-light" = {
      set_if = "$command_""" + self.__command_name + """_version_light$"
    }
"""
        else:
            config += """
    "--not-version-light" = {
      set_if = "$command_""" + self.__command_name + """_not_version_light$"
    }
"""
        if self.__version_all:
            config += """
    "--version-all" = {
      set_if = "$command_""" + self.__command_name + """_version_all$"
    }
"""
        else:
            config += """
    "--not-version-all" = {
      set_if = "$command_""" + self.__command_name + """_not_version_all$"
    }
"""
        if self.__version_trace:
            config += """
    "--version-trace" = {
      set_if = "$command_""" + self.__command_name + """_version_trace$"
    }
"""
        else:
            config += """
    "--not-version-trace" = {
      set_if = "$command_""" + self.__command_name + """_not_version_trace$"
    }
"""
        if self.__sC:
            config += """
    "-sC" = {
      set_if = "$command_""" + self.__command_name + """_sC$"
    }
"""
        else:
            config += """
    "-not-sC" = {
      set_if = "$command_""" + self.__command_name + """_not_sC$"
    }
"""
        if self.__script_trace:
            config += """
    "--script-trace" = {
      set_if = "$command_""" + self.__command_name + """_script_trace$"
    }
"""
        else:
            config += """
    "--not-script-trace" = {
      set_if = "$command_""" + self.__command_name + """_not_script_trace$"
    }
"""
        if self.__O:
            config += """
    "-O" = {
      set_if = "$command_""" + self.__command_name + """_O$"
    }
"""
        else:
            config += """
    "-not-O" = {
      set_if = "$command_""" + self.__command_name + """_not_O$"
    }
"""
        if self.__osscan_guess:
            config += """
    "--osscan-guess" = {
      set_if = "$command_""" + self.__command_name + """_osscan_guess$"
    }
"""
        else:
            config += """
    "--not-osscan-guess" = {
      set_if = "$command_""" + self.__command_name + """_not_osscan_guess$"
    }
"""
        if self.__badsum:
            config += """
    "--badsum" = {
      set_if = "$command_""" + self.__command_name + """_badsum$"
    }
"""
        else:
            config += """
    "--not-badsum" = {
      set_if = "$command_""" + self.__command_name + """_not_badsum$"
    }
"""
        if self.__6:
            config += """
    "-6" = {
      set_if = "$command_""" + self.__command_name + """_6$"
    }
"""
        else:
            config += """
    "-not-6" = {
      set_if = "$command_""" + self.__command_name + """_not_6$"
    }
"""
        if self.__A:
            config += """
    "-A" = {
      set_if = "$command_""" + self.__command_name + """_A$"
    }
"""
        else:
            config += """
    "-not-A" = {
      set_if = "$command_""" + self.__command_name + """_not_A$"
    }
"""
        if self.__send_eth:
            config += """
    "--send-eth" = {
      set_if = "$command_""" + self.__command_name + """_send_eth$"
    }
"""
        else:
            config += """
    "--not-send-eth" = {
      set_if = "$command_""" + self.__command_name + """_not_send_eth$"
    }
"""
        if self.__send_ip:
            config += """
    "--send-ip" = {
      set_if = "$command_""" + self.__command_name + """_send_ip$"
    }
"""
        else:
            config += """
    "--not-send-ip" = {
      set_if = "$command_""" + self.__command_name + """_not_send_ip$"
    }
"""
        if self.__privileged:
            config += """
    "--privileged" = {
      set_if = "$command_""" + self.__command_name + """_privileged$"
    }
"""
        else:
            config += """
    "--not-privileged" = {
      set_if = "$command_""" + self.__command_name + """_not_privileged$"
    }
"""
        if self.__Pn:
            config += """
    "-Pn" = {
      set_if = "$command_""" + self.__command_name + """_Pn$"
    }
"""
        else:
            config += """
    "-not-Pn" = {
      set_if = "$command_""" + self.__command_name + """_not_Pn$"
    }
"""
        if self.__unprivileged:
            config += """
    "--unprivileged" = {
      set_if = "$command_""" + self.__command_name + """_unprivileged$"
    }
"""
        else:
            config += """
    "--not-unprivileged" = {
      set_if = "$command_""" + self.__command_name + """_not_unprivileged$"
    }
"""

        return config
