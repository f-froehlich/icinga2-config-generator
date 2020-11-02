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


class Command:

    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def get_command(self):
        raise Exception("get_command must return command name")

    def get_arguments(self):
        raise Exception("get_arguments must return arguments")

    def get_config(self):
        config = self.get_config_local()
        config += self.get_config_ssh()

        return config

    def get_command_definition(self):
        return '[ "$plugin_dir$" + "/' + self.get_command() + '"]'

    def get_config_local(self):
        config = 'object CheckCommand "command_' + self.get_id() + '_local" {\n'
        config += '  command = ' + self.get_command_definition() + '\n'
        config += '  arguments = ' + self.get_arguments() + '\n'
        config += '}\n'

        return config

    def get_config_ssh(self):
        config = 'object CheckCommand "command_' + self.get_id() + '_ssh" {\n'
        config += '  vars.realcmd = ' + self.get_command_definition() + '\n'
        config += '  vars.realargs = ' + self.get_arguments() + '\n'
        config += """  command = [ "$command_overssh_plugin_dir$" + "/check_by_ssh"]
  arguments = {
    "-i" = "$command_overssh_identityfile$"
    "-l" = "$command_overssh_user$"
    "-p" = "$command_overssh_port$"
    "-H" = "$command_overssh_host$"
    "--timeout" = "$command_overssh_timeout$"
    "-C" = {{
      var command = macro("$realcmd$")
      var arguments = macro("$realargs$")
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
}
"""
        return config
