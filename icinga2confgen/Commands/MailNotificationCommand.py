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

from icinga2confgen.Commands.MonitoringPlugins.NotificationCommand import NotificationCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker


class MailNotificationCommand(NotificationCommand):

    def __init__(self, id):
        NotificationCommand.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = MailNotificationCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command_definition(self):
        return '[ "/etc/icinga2/scripts/mail-service-notification.sh" ]'

    def get_arguments(self):
        config = """{
    "-4" = {
      required = true
      value = "$notification_address$"
    }
    "-6" = "$notification_address6$"
    "-b" = "$notification_author$"
    "-c" = "$notification_comment$"
    "-d" = {
      required = true
      value = "$notification_date$"
    }
    "-e" = {
      required = true
      value = "$notification_servicename$"
    }
    "-f" = {
      value = "$notification_from$"
      description = "Set from icinga2confgen.address. Requires GNU mailutils (Debian/Ubuntu) or mailx (RHEL/SUSE)"
    }
    "-i" = "$notification_icingaweb2url$"
    "-l" = {
      required = true
      value = "$notification_hostname$"
    }
    "-n" = {
      required = true
      value = "$notification_hostdisplayname$"
    }
    "-o" = {
      required = true
      value = "$notification_serviceoutput$"
    }
    "-r" = {
      required = true
      value = "$notification_useremail$"
    }
    "-s" = {
      required = true
      value = "$notification_servicestate$"
    }
    "-t" = {
      required = true
      value = "$notification_type$"
    }
    "-u" = {
      required = true
      value = "$notification_servicedisplayname$"
    }
    "-v" = "$notification_logtosyslog$"
  }

  vars += {
    notification_address = "$address$"
    notification_address6 = "$address6$"
    notification_author = "$notification.author$"
    notification_comment = "$notification.comment$"
    notification_type = "$notification.type$"
    notification_date = "$icinga.long_date_time$"
    notification_hostname = "$host.name$"
    notification_hostdisplayname = "$host.display_name$"
    notification_servicename = "$service.name$"
    notification_serviceoutput = "$service.output$"
    notification_servicestate = "$service.state$"
    notification_useremail = "$user.email$"
    notification_servicedisplayname = "$service.display_name$"
  }
"""

        return config
