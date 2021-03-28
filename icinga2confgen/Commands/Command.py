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
import typing

T = typing.TypeVar('T', bound='Command')

class Command:

    def __init__(self: T, id: str):
        self.__id: str = id

    def get_id(self: T) -> str:
        return self.__id

    def get_command(self: T) -> str:
        raise Exception("get_command must return command name")

    def get_arguments(self: T) -> str:
        raise Exception("get_arguments must return arguments")

    def get_config(self: T) -> str:
        config = self.get_config_local()
        config += self.get_config_local_negate()
        config += self.get_config_ssh()
        config += self.get_config_ssh_negate()

        return config

    def get_command_definition(self: T) -> str:
        return '[ "$nagios_plugin_dir$" + "/' + self.get_command() + '"]'

    def get_config_local(self: T) -> str:
        config = 'object CheckCommand "command_' + self.get_id() + '_local" {\n'
        config += '  command = ' + self.get_command_definition() + '\n'
        config += '  arguments = ' + self.get_arguments() + '\n'
        config += '}\n'

        return config

    def get_config_local_negate(self: T) -> str:
        config = 'object CheckCommand "command_' + self.get_id() + '_local_negate" {\n'
        config += '  vars.realcmd = ' + self.get_command_definition() + '\n'
        config += '  vars.realargs = ' + self.get_arguments() + '\n'
        config += '  arguments = ' + self.__get_negate_args() + '\n'
        config += '  command = ["$nagios_plugin_dir$" + "/negate"]\n'
        config += '}\n'

        return config

    def get_config_ssh(self: T) -> str:
        config = 'object CheckCommand "command_' + self.get_id() + '_ssh" {\n'
        config += '  vars.sshcmd = ' + self.get_command_definition() + '\n'
        config += '  vars.sshargs = ' + self.get_arguments() + '\n'
        config += '  command = [ "$command_overssh_nagios_plugin_dir$" + "/check_by_ssh"]\n'
        config += '  arguments = ' + self.__get_ssh_args() + '\n'
        config += '}\n'

        return config

    def get_config_ssh_negate(self: T) -> str:
        config = 'object CheckCommand "command_' + self.get_id() + '_ssh_negate" {\n'
        config += '  vars.realcmd = ' + self.get_command_definition() + '\n'
        config += '  vars.realargs = ' + self.get_arguments() + '\n'
        config += '  vars.sshargs = ' + self.__get_negate_args() + '\n'
        config += '  vars.sshcmd = ["$nagios_plugin_dir$" + "/negate"]\n'
        config += '  command = [ "$command_overssh_nagios_plugin_dir$" + "/check_by_ssh"]\n'
        config += '  arguments = ' + self.__get_ssh_args() + '\n'
        config += '}\n'

        return config

    def __get_negate_args(self: T) -> str:
        return """{
  "-t" = {
    value = "$negation_timeout$"
    set_if = {{ macro("$negation_timeout$") != false }}
  }
  "-o" = {
    value = "$negation_ok_status$"
    set_if = {{ macro("$negation_ok_status$") != false }}
  }
  "-w" = {
    value = "$negation_warning_status$"
    set_if = {{ macro("$negation_warning_status$") != false }}
  }
  "-c" = {
    value = "$negation_critical_status$"
    set_if = {{ macro("$negation_critical_status$") != false }}
  }
  "-u" = {
    value = "$negation_unknown_status$"
    set_if = {{ macro("$negation_unknown_status$") != false }}
  }
  "-s" = {
    set_if = {{ macro("$negation_substitute$") != false && "$negation_substitute$" }}
  }
  "--command" = {
    value = {{
      var command = macro("$realcmd$")
      var arguments = macro("$realargs$")
      if (typeof(command) == String && !arguments) {
        return command
      }
      var escaped_args = []
      for (arg in resolve_arguments(command, arguments)) {
          escaped_args.add(arg.replace(" ", "\\\\"))
      }
      return escaped_args.join(" ")
    }}
    skip_key = true
    required = true
    order = 99
  }
}
"""

    def __get_ssh_args(self: T) -> str:
        return """{
  "-i" = "$command_overssh_identityfile$"
  "-l" = "$command_overssh_user$"
  "-p" = "$command_overssh_port$"
  "-H" = "$command_overssh_host$"
  "--timeout" = "$command_overssh_timeout$"
  "-C" = {{
    var command = macro("$sshcmd$")
    var arguments = macro("$sshargs$")
    if (typeof(command) == String && !arguments) {
      return command
    }
    var escaped_args = []
    for (arg in resolve_arguments(command, arguments)) {
      escaped_args.add(escape_shell_arg(arg))
    }
    return escaped_args.join(" ")
  }}
}
"""
