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


class NotificationCommand:

    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def validate(self):
        raise Exception("validate must be overridden in " + self.__id)

    def get_command_executable_host(self):
        raise Exception("get_command_executable_path_host must return command executable for host in " + self.__id)

    def get_command_executable_service(self):
        raise Exception("get_command_executable_service must return command executable for service in " + self.__id)

    def get_arguments_host(self):
        config = '{\n' + self.get_default_arguments_host() + '}\n'
        config += self.get_default_vars_host()

        return config

    def get_arguments_service(self):
        config = '{\n' + self.get_default_arguments_service() + '}\n'
        config += self.get_default_vars_service()

        return config

    def get_command_definition_host(self):
        return '[ "/etc/icinga2/scripts/' + self.get_command_executable_host() + '"]'

    def get_command_definition_service(self):
        return '[ "/etc/icinga2/scripts/' + self.get_command_executable_service() + '"]'

    def get_config(self):
        self.validate()
        config = 'object NotificationCommand "command_host_' + self.get_id() + '" {\n'
        config += '  command = ' + self.get_command_definition_host() + '\n'
        config += '  arguments = ' + self.get_arguments_host() + '\n'
        config += '}\n'
        config += 'object NotificationCommand "command_service_' + self.get_id() + '" {\n'
        config += '  command = ' + self.get_command_definition_service() + '\n'
        config += '  arguments = ' + self.get_arguments_service() + '\n'
        config += '}\n'

        return config

    def get_default_arguments_host(self):
        return """
    "-d" = {
      value = "$notification_date$"
      required = true
    }
    "-l" = {
      value = "$notification_hostname$"
      required = true
    }
    "-n" = {
      value = "$notification_hostdisplayname$"
      required = true
    }
    "-o" = {
      value = "$notification_serviceoutput$"
      required = true
    }
    "-s" = {
      value = "$notification_servicestate$"
      required = true
    }
    "-4" = {
      value = "$notification_address$"
      set_if = {{ macro("$notification_address$") != false }}
    }
    "-6" = {
      value = "$notification_address6$"
      set_if = {{ macro("$notification_address6$") != false }}
    }
    "-b" = {
      value = "$notification_author$"
      set_if = {{ macro("$notification_author$") != false }}
    }
    "-c" = {
      value = "$notification_comment$"
      set_if = {{ macro("$notification_comment$") != false }}
    }
    "-i" = {
      value = "$notification_icingaweb2url$"
      set_if = {{ macro("$notification_icingaweb2url$") != false }}
    }
    "-f" = {
      value = "$notification_from$"
      set_if = {{ macro("$notification_from$") != false }}
      description = "Set from icinga2confgen.address. Requires GNU mailutils (Debian/Ubuntu) or mailx (RHEL/SUSE)"
    }
    "-v" = {
      set_if = "$notification_logtosyslog$"
    }
"""

    def get_default_vars_host(self):
        return """
  vars += {
    notification_address = "$address$"
    notification_address6 = "$address6$"
    notification_author = "$notification.author$"
    notification_comment = "$notification.comment$"
    notification_date = "$icinga.long_date_time$"
    notification_hostname = "$host.name$"
    notification_hostdisplayname = "$host.display_name$"
    notification_serviceoutput = "$service.output$"
    notification_servicestate = "$service.state$"
  }
"""

    def get_default_arguments_service(self):
        config = self.get_default_arguments_host()
        config += """
    "-e" = {
      value = "$notification_servicename$"
      required = true
    }
    "-t" = {
      value = "$notification_type$"
      required = true
    }
    "-u" = {
      value = "$notification_servicedisplayname$"
      required = true
    }
"""
        return config

    def get_default_vars_service(self):
        config = self.get_default_vars_host()
        config += """
  vars += {
    notification_servicename = "$service.name$"
    notification_type = "$notification.type$"
    notification_servicedisplayname = "$service.display_name$"
  }
"""
        return config
