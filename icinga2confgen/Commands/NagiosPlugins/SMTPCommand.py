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


class SMTPCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = SMTPCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_smtp'

    def get_arguments(self):
        config = """{
    "-H" = {
      value = "$command_smtp_host$"
      required = true
    }
    "-p" = {
      value = "$command_smtp_port$"
      set_if = {{ macro("$command_smtp_port$") != false }}
    }
    "-4" = {
      set_if = "$command_smtp_use_ipv4$"
    }
    "-6" = {
      set_if = "$command_smtp_use_ipv6$"
    }
    "-e" = {
      value = "$command_smtp_expect$"
      set_if = {{ macro("$command_smtp_expect$") != false }}
    }
    "-C" = {
      value = "$command_smtp_command$"
      set_if = {{ macro("$command_smtp_command$") != false }}
    }
    "-R" = {
      value = "$command_smtp_response$"
      set_if = {{ macro("$command_smtp_response$") != false }}
    }
    "-f" = {
      value = "$command_smtp_from$"
      set_if = {{ macro("$command_smtp_from$") != false }}
    }
    "-F" = {
      value = "$command_smtp_fqdn$"
      set_if = {{ macro("$command_smtp_fqdn$") != false }}
    }
    "-D" = {
      value = "$command_smtp_cert_warning$,$command_smtp_cert_critical$"
      set_if = {{ macro("$command_smtp_cert$") != false }}
    }
    "-S" = {
      set_if = "$command_smtp_starttls$"
    }
    "-A" = {
      value = "$command_smtp_authtype$"
      set_if = {{ macro("$command_smtp_authtype$") != false }}
    }
    "-U" = {
      value = "$command_smtp_authuser$"
      set_if = {{ macro("$command_smtp_authuser$") != false }}
    }
    "-P" = {
      value = "$command_smtp_authpass$"
      set_if = {{ macro("$command_smtp_authpass$") != false }}
    }
    "-q" = {
      set_if = "$command_smtp_ignore_quit_failure$"
    }
    "-w" = {
      value = "$command_smtp_warning$"
      set_if = {{ macro("$command_smtp_warning$") != false }}
    }
    "-c" = {
      value = "$command_smtp_critical$"
      set_if = {{ macro("$command_smtp_critical$") != false }}
    }
    "-t" = {
      value = "$command_smtp_timeout$"
      set_if = {{ macro("$command_smtp_timeout$") != false }}
    }
  }
"""

        return config
