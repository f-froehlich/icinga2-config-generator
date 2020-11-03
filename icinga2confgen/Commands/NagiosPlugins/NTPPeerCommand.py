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


class NTPPeerCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = NTPPeerCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_ntp_peer'

    def get_arguments(self):
        config = """{
    "--use-ipv4" = {
      value = "$command_ntp_peer_force_ipv4$"
      set_if = {{ macro("$command_ntp_peer_force_ipv4$") != false }}
    }
    "--use-ipv6" = {
      value = "$command_ntp_peer_force_ipv6$"
      set_if = {{ macro("$command_ntp_peer_force_ipv6$") != false }}
    }
    "--hostname" = {
      value = "$command_ntp_peer_ntp_server$"
      required = true
    }
    "--port" = {
      value = "$command_ntp_peer_ntp_server_port$"
      set_if = {{ macro("$command_ntp_peer_ntp_server_port$") != false }}
    }
    "--quiet" = {
      set_if = "$command_ntp_peer_quiet$"
    }
    "--warning" = {
      value = "$command_ntp_peer_warning$"
      set_if = {{ macro("$command_ntp_peer_warning$") != false }}
    }
    "--critical" = {
      value = "$command_ntp_peer_critical$"
      set_if = {{ macro("$command_ntp_peer_critical$") != false }}
    }
    "--swarn" = {
      value = "$command_ntp_peer_swarn$"
      set_if = {{ macro("$command_ntp_peer_swarn$") != false }}
    }
    "--scrit" = {
      value = "$command_ntp_peer_scrit$"
      set_if = {{ macro("$command_ntp_peer_scrit$") != false }}
    }
    "--jwarn" = {
      value = "$command_ntp_peer_jwarn$"
      set_if = {{ macro("$command_ntp_peer_jwarn$") != false }}
    }
    "--jcrit" = {
      value = "$command_ntp_peer_jcrit$"
      set_if = {{ macro("$command_ntp_peer_jcrit$") != false }}
    }
    "--twarn" = {
      value = "$command_ntp_peer_twarn$"
      set_if = {{ macro("$command_ntp_peer_twarn$") != false }}
    }
    "--tcrit" = {
      value = "$command_ntp_peer_tcrit$"
      set_if = {{ macro("$command_ntp_peer_tcrit$") != false }}
    }
    "--timeout" = {
      value = "$command_ntp_peer_timeout$"
      set_if = {{ macro("$command_ntp_peer_timeout$") != false }}
    }
  }
"""

        return config
