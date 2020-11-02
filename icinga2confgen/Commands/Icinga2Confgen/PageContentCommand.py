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


class PageContentCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = PageContentCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_page_content.py'

    def get_arguments(self):
        config = """{
    "--ok-content" = {
      value = "$command_page_content_ok$"
      set_if = {{ macro("$command_page_content_ok$") != false }}
      repeat_key = true
    }
    "--warning-content" = {
      value = "$command_page_content_warning$"
      set_if = {{ macro("$command_page_content_warning$") != false }}
      repeat_key = true
    }
    "--critical-content" = {
      value = "$command_page_content_critical$"
      set_if = {{ macro("$command_page_content_critical$") != false }}
      repeat_key = true
    }
    "--header" = {
      value = "$command_page_content_header$"
      set_if = {{ macro("$command_page_content_header$") != false }}
      repeat_key = true
    }
    "--uri" = {
      value = "$command_page_content_uri$"
      set_if = {{ macro("$command_page_content_uri$") != false }}
    }
    "--domain" = {
      value = "$command_page_content_domain$"
      required = true
    }
    "--port" = {
      value = "$command_page_content_port$"
      set_if = {{ macro("$command_page_content_port$") != false }}
    }
    "--ssl" = {
      set_if = "$command_page_content_ssl$"
    }
    "--client-cert" = {
      value = "$command_page_content_client_cert$"
      set_if = {{ macro("$command_page_content_client_cert$") != false }}
    }
    "--client-key" = {
      value = "$command_page_content_client_key$"
      set_if = {{ macro("$command_page_content_client_key$") != false }}
    }
  }
"""
        return config
