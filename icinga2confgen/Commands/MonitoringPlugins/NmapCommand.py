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

    def __init__(self, id, command_name, only_udp=False, only_tcp=False, pn=False, fast=False):
        MonitoringPluginCommand.__init__(self, id)
        self.__command_name = command_name
        self.__only_udp = only_udp
        self.__only_tcp = only_tcp
        self.__pn = pn
        self.__fast = fast

    @staticmethod
    def create(id, force_create=False):
        raise Exception('Can\'t create NmapCommand, use child classes instead.')

    def get_arguments(self):
        config = """
    "--host" = {
      value = "$command_""" + self.__command_name + """_host$"
      required = true
    }
    "--ports" = {
      value = "$command_""" + self.__command_name + """_ports$"
      set_if = {{ macro("$command_""" + self.__command_name + """_ports$") != false }}
    }
    "--top-ports" = {
      value = "$command_""" + self.__command_name + """_top_ports$"
      set_if = {{ macro("$command_""" + self.__command_name + """_top_ports$") != false }}
    }
    "--min-rate" = {
      value = "$command_""" + self.__command_name + """_min_rate$"
      set_if = {{ macro("$command_""" + self.__command_name + """_min_rate$") != false }}
    }
    "--max-rate" = {
      value = "$command_""" + self.__command_name + """_max_rate$"
      set_if = {{ macro("$command_""" + self.__command_name + """_max_rate$") != false }}
    }
    "--host-timeout" = {
      value = "$command_""" + self.__command_name + """_host_timeout$"
      set_if = {{ macro("$command_""" + self.__command_name + """_host_timeout$") != false }}
    }
    "--max-retries" = {
      value = "$command_""" + self.__command_name + """_max_retries$"
      set_if = {{ macro("$command_""" + self.__command_name + """_max_retries$") != false }}
    }
    "--timeout" = {
      value = "$command_""" + self.__command_name + """_timeout$"
      set_if = {{ macro("$command_""" + self.__command_name + """_timeout$") != false }}
    }
"""
        if self.__only_udp:
            config += """
    "--not-only-udp" = {
      set_if = "$command_""" + self.__command_name + """_not_only_udp$"
    }
"""
        else:
            config += """
    "--only-udp" = {
      set_if = "$command_""" + self.__command_name + """_only_udp$"
    }
"""

        if self.__only_tcp:
            config += """
    "--not-only-tcp" = {
      set_if = "$command_""" + self.__command_name + """_not_only_tcp$"
    }
"""
        else:
            config += """
    "--only-tcp" = {
      set_if = "$command_""" + self.__command_name + """_only_tcp$"
    }
"""
        if self.__fast:
            config += """
    "--not-fasr" = {
      set_if = "$command_""" + self.__command_name + """_not_fast$"
    }
"""
        else:
            config += """
    "--fast" = {
      set_if = "$command_""" + self.__command_name + """_fast$"
    }
"""

        if self.__pn:
            config += """
    "--not-Pn" = {
      set_if = "$command_""" + self.__command_name + """_not_pn$"
    }
"""
        else:
            config += """
    "--Pn" = {
      set_if = "$command_""" + self.__command_name + """_pn$"
    }
"""

        return config
