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


class TCPCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = TCPCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_tcp'

    def get_arguments(self):
        config = """{
    "-H" = {
      value = "$command_tcp_host$"
      required = true
    }
    "-p" = {
      value = "$command_tcp_port$"
      required = true
    }
    "-4" = {
      set_if = "$command_tcp_ipv4$"
    }
    "-6" = {
      set_if = "$command_tcp_ipv6$"
    }
    "-E" = {
      set_if = "$command_tcp_escape$"
    }
    "-s" = {
      value = "$command_tcp_send$"
      set_if = {{ macro("$command_tcp_send$") != false }}
    }
    "-e" = {
      value = "$command_tcp_expect$"
      set_if = {{ macro("$command_tcp_expect$") != false }}
    }
    "-A" = {
      set_if = "$command_tcp_all$"
    }
    "-q" = {
      value = "$command_tcp_quit$"
      set_if = {{ macro("$command_tcp_quit$") != false }}
    }
    "-r" = {
      value = "$command_tcp_refuse_state$"
      set_if = {{ macro("$command_tcp_refuse_state$") != false }}
    }
    "-M" = {
      value = "$command_tcp_mismatch_state$"
      set_if = {{ macro("$command_tcp_mismatch_state$") != false }}
    }
    "-j" = {
      set_if = "$command_tcp_jail$"
    }
    "-m" = {
      value = "$command_tcp_maxbytes$"
      set_if = {{ macro("$command_tcp_maxbytes$") != false }}
    }
    "-d" = {
      value = "$command_tcp_delay$"
      set_if = {{ macro("$command_tcp_delay$") != false }}
    }
    "-D" = {
      value = "$command_tcp_cert_warning$,$command_tcp_cert_critical$"
      set_if = {{ macro("$command_tcp_cert$") != false }}
    }
    "-S" = {
      set_if = "$command_tcp_use_ssl$"
    }
    "--sni" = {
      value = "$command_tcp_sni$"
      set_if = {{ macro("$command_tcp_sni$") != false }}
    }
    "-w" = {
      value = "$command_tcp_warning_time$"
      set_if = {{ macro("$command_tcp_warning_time$") != false }}
    }
    "-c" = {
      value = "$command_tcp_critical_time$"
      set_if = {{ macro("$command_tcp_critical_time$") != false }}
    }
    "-t" = {
      value = "$command_tcp_timeout$"
      set_if = {{ macro("$command_tcp_timeout$") != false }}
    }
  }
"""

        return config
