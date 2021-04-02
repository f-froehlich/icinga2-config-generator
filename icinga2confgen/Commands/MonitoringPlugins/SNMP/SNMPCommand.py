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
from __future__ import annotations

import typing
from abc import abstractmethod

from icinga2confgen.Commands.MonitoringPlugins.MonitoringPluginCommand import MonitoringPluginCommand

T = typing.TypeVar('T', bound='SNMPCommand')


class SNMPCommand(MonitoringPluginCommand):

    def __init__(self: T, id: str):
        MonitoringPluginCommand.__init__(self, id)

    def get_arguments(self: T) -> str:
        config = """{
    "-u" = {
      value = "$command_snmp_username$"
      set_if = {{ macro("$command_snmp_username$") != false }}
    }
    "-p" = {
      value = "$command_snmp_password$"
      set_if = {{ macro("$command_snmp_password$") != false }}
    }
    "-H" = {
      value = "$command_snmp_host$"
      required = true
    }
    "--timeout" = {
      value = "$command_snmp_timeout$"
      set_if = {{ macro("$command_snmp_timeout$") != false }}
    }
    "--version" = {
      value = "$command_snmp_version$"
      set_if = {{ macro("$command_snmp_version$") != false }}
    }
    "--community" = {
      value = "$command_snmp_community$"
      set_if = {{ macro("$command_snmp_community$") != false }}
    }
"""
        config += self.get_specific_arguments()
        config += """
  }
"""
        return config

    @abstractmethod
    def get_specific_arguments(self: T) -> str:
        raise NotImplementedError()
