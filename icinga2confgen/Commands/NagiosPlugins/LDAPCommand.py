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


class LDAPCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = LDAPCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_ldap'

    def get_arguments(self):
        config = """{
    "-H" = {
      value = "$command_ldap_host$"
      required = true
    }
    "-p" = {
      value = "$command_ldap_port$"
      set_if = {{ macro("$command_ldap_port$") != false }}
    }
    "-4" = {
      set_if = "$command_ldap_use_ipv4$"
    }
    "-6" = {
      set_if = "$command_ldap_use_ipv6$"
    }
    "-a" = {
      value = "$command_ldap_attr$"
      set_if = {{ macro("$command_ldap_attr$") != false }}
    }
    "-b" = {
      value = "$command_ldap_base$"
      required = true
    }
    "-D" = {
      value = "$command_ldap_dn$"
      set_if = {{ macro("$command_ldap_dn$") != false }}
    }
    "-P" = {
      value = "$command_ldap_pass$"
      set_if = {{ macro("$command_ldap_pass$") != false }}
    }
    "-T" = {
      set_if = "$command_ldap_starttls$"
    }
    "-S" = {
      set_if = "$command_ldap_ssl$"
    }
    "-2" = {
      set_if = "$command_ldap_protocol_v2$"
    }
    "-3" = {
      set_if = "$command_ldap_protocol_v3$"
    }
    "-w" = {
      value = "$command_ldap_warning$"
      set_if = {{ macro("$command_ldap_warning$") != false }}
    }
    "-c" = {
      value = "$command_ldap_critical$"
      set_if = {{ macro("$command_ldap_critical$") != false }}
    }
    "-W" = {
      value = "$command_ldap_warning_entries$"
      set_if = {{ macro("$command_ldap_warning$") != false }}
    }
    "-C" = {
      value = "$command_ldap_critical_entries$"
      set_if = {{ macro("$command_ldap_critical$") != false }}
    }
    "-t" = {
      value = "$command_ldap_timeout$"
      set_if = {{ macro("$command_ldap_timeout$") != false }}
    }
  }
"""

        return config
