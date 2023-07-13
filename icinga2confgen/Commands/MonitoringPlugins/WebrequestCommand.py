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
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker


class WebrequestCommand(MonitoringPluginCommand):

    def __init__(self, id: str, command_name: str):
        MonitoringPluginCommand.__init__(self, id)
        self.__command_name = command_name

    @staticmethod
    def create(id: str, force_create: bool = False):
        raise Exception('Can\'t create WebrequestCommand, use child classes instead.')


    def get_command(self) -> str:
        return 'check_' + self.__command_name + '.py'

    def get_arguments(self) -> str:
        config = """
    "--header" = {
      value = "$command_""" + self.__command_name + """_header$"
      set_if = {{ macro("$command_""" + self.__command_name + """_header$") != false }}
      repeat_key = true
    }
    "--uri" = {
      value = "$command_""" + self.__command_name + """_uri$"
      set_if = {{ macro("$command_""" + self.__command_name + """_uri$") != false }}
    }
    "--domain" = {
      value = "$command_""" + self.__command_name + """_domain$"
      set_if = {{ macro("$command_""" + self.__command_name + """_domain$") != false }}
    }
    "--port" = {
      value = "$command_""" + self.__command_name + """_port$"
      set_if = {{ macro("$command_""" + self.__command_name + """_port$") != false }}
    }
    "--ssl" = {
      set_if = "$command_""" + self.__command_name + """_ssl$"
    }
    "--client-cert" = {
      value = "$command_""" + self.__command_name + """_client_cert$"
      set_if = {{ macro("$command_""" + self.__command_name + """_client_cert$") != false }}
    }
    "--client-key" = {
      value = "$command_""" + self.__command_name + """_client_key$"
      set_if = {{ macro("$command_""" + self.__command_name + """_client_key$") != false }}
    }
    "--timeout" = {
      value = "$command_""" + self.__command_name + """_timeout$"
      set_if = {{ macro("$command_""" + self.__command_name + """_timeout$") != false }}
    }
"""
        return config
