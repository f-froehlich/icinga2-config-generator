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

from icinga2confgen.Commands.Command import Command
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker


class UDPCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = UDPCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_udp'

    def get_arguments(self):
        config = """{
    "-H" = {
      value = "$command_udp_host$"
      required = true
    }
    "-p" = {
      value = "$command_udp_port$"
      required = true
    }
    "-4" = {
      set_if = "$command_udp_ipv4$"
    }
    "-6" = {
      set_if = "$command_udp_ipv6$"
    }
    "-E" = {
      set_if = "$command_udp_escape$"
    }
    "-s" = {
      value = "$command_udp_send$"
      set_if = {{ macro("$command_udp_send$") != false }}
    }
    "-e" = {
      value = "$command_udp_expect$"
      set_if = {{ macro("$command_udp_expect$") != false }}
    }
    "-A" = {
      set_if = "$command_udp_all$"
    }
    "-q" = {
      value = "$command_udp_quit$"
      set_if = {{ macro("$command_udp_quit$") != false }}
    }
    "-r" = {
      value = "$command_udp_refuse_state$"
      set_if = {{ macro("$command_udp_refuse_state$") != false }}
    }
    "-M" = {
      value = "$command_udp_mismatch_state$"
      set_if = {{ macro("$command_udp_mismatch_state$") != false }}
    }
    "-j" = {
      set_if = "$command_udp_jail$"
    }
    "-m" = {
      value = "$command_udp_maxbytes$"
      set_if = {{ macro("$command_udp_maxbytes$") != false }}
    }
    "-d" = {
      value = "$command_udp_delay$"
      set_if = {{ macro("$command_udp_delay$") != false }}
    }
    "-D" = {
      value = "$command_udp_cert_warning$,$command_udp_cert_critical$"
      set_if = {{ macro("$command_udp_cert$") != false }}
    }
    "-S" = {
      set_if = "$command_udp_use_ssl$"
    }
    "--sni" = {
      value = "$command_udp_sni$"
      set_if = {{ macro("$command_udp_sni$") != false }}
    }
    "-w" = {
      value = "$command_udp_warning_time$"
      set_if = {{ macro("$command_udp_warning_time$") != false }}
    }
    "-c" = {
      value = "$command_udp_critical_time$"
      set_if = {{ macro("$command_udp_critical_time$") != false }}
    }
    "-t" = {
      value = "$command_udp_timeout$"
      set_if = {{ macro("$command_udp_timeout$") != false }}
    }
  }
"""

        return config
