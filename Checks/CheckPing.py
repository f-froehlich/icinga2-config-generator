#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, commands, checks, ... in python
#
#  Copyright (c) 2020 Fabian Fröhlich <mail@f-froehlich.de> https://f-froehlich.de
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

from Checks.Check import Check
from Commands.PingCommand import PingCommand
from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker


class CheckPing(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckPing', 'ping')
        self.__warning_percent_lost = 5
        self.__warning_average_time = 100
        self.__critical_percent_lost = 10
        self.__critical_average_time = 250
        self.__timeout = 10
        self.__packets = 4

    @staticmethod
    def create(id):
        ConfigBuilder.validate_id(id)
        check = ConfigBuilder.get_check(id)
        if None is check:
            id = 'check_' + id
            check = CheckPing(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('ping'):
            PingCommand.create('ping')

        return check

    def set_warning_percent_lost(self, threshold):
        ValueChecker.is_number(threshold)
        self.__warning_percent_lost = threshold

    def get_warning_percent_lost(self):
        return self.__warning_percent_lost

    def set_warning_average_time(self, time):
        ValueChecker.is_number(time)
        self.__warning_average_time = time

    def get_warning_average_time(self):
        return self.__warning_average_time

    def set_critical_percent_lost(self, threshold):
        ValueChecker.is_number(threshold)
        self.__critical_percent_lost = threshold

    def get_critical_percent_lost(self):
        return self.__critical_percent_lost

    def set_critical_average_time(self, time):
        ValueChecker.is_number(time)
        self.__critical_average_time = time

    def get_critical_average_time(self):
        return self.__critical_average_time

    def set_timeout(self, timeout):
        ValueChecker.is_number(timeout)
        self.__timeout = timeout

    def get_timeout(self):
        return self.__timeout

    def set_packets(self, packets):
        ValueChecker.is_number(packets)
        self.__packets = packets

    def get_packets(self):
        return self.__packets

    def get_config(self):

        config = ''

        for i in ['4', '6']:
            config += 'apply Service "' + self.get_id() + '_' + i + '" {\n'
            config += '  check_command = "command_ping_' + self.get_check_type() + '"\n'
            config += self.get_property_default_config()
            config += self.get_notification_config()

            if '4' == i:
                config += '  vars.command_ping_v4 = true\n'
                config += '  vars.command_ping_address = host.address\n'
                config += '  assign where host.vars.' + self.get_id() + ' && host.address\n'
            else:
                config += '  vars.command_ping_v6 = true\n'
                config += '  vars.command_ping_address = host.address6\n'
                config += '  assign where host.vars.' + self.get_id() + ' && host.address6\n'

            config += self.get_group_config()
            config += '}\n'

        return config
