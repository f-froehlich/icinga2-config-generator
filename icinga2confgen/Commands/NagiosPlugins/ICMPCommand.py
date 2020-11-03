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


class ICMPCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = ICMPCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_icmp'

    def get_arguments(self):
        config = """{
    "-H" = {
      value = "$command_icmp_host$"
      required = true
    }
    "-4" = {
      set_if = "$command_icmp_use_ipv4$"
    }
    "-6" = {
      set_if = "$command_icmp_use_ipv6$"
    }
    "-w" = {
      value = "$command_icmp_warning$"
      set_if = {{ macro("$command_icmp_warning$") != false }}
    }
    "-c" = {
      value = "$command_icmp_critical$"
      set_if = {{ macro("$command_icmp_critical$") != false }}
    }
    "-s" = {
      value = "$command_icmp_source$"
      set_if = {{ macro("$command_icmp_source$") != false }}
    }
    "-n" = {
      value = "$command_icmp_packets$"
      set_if = {{ macro("$command_icmp_packets$") != false }}
    }
    "-i" = {
      value = "$command_icmp_packet_interval$"
      set_if = {{ macro("$command_icmp_packet_interval$") != false }}
    }
    "-m" = {
      value = "$command_icmp_minimum_hosts$"
      set_if = {{ macro("$command_icmp_minimum_hosts$") != false }}
    }
    "-l" = {
      value = "$command_icmp_ttl$"
      set_if = {{ macro("$command_icmp_ttl$") != false }}
    }
    "-t" = {
      value = "$command_icmp_timeout$"
      set_if = {{ macro("$command_icmp_timeout$") != false }}
    }
    "-b" = {
      value = "$command_icmp_bytes$"
      set_if = {{ macro("$command_icmp_bytes$") != false }}
    }
  }
"""

        return config
