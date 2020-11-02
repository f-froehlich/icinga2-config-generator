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

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckPing(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckPing', 'ping')
        self.__warning_percent_lost = 5
        self.__warning_average_time = 100
        self.__critical_percent_lost = 10
        self.__critical_average_time = 250
        self.__timeout = 10
        self.__packets = 4
        self.__address = None
        self.add_service_group(ServiceGroup.create('ping'))
        self.add_service_group(ServiceGroup.create('network'))

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

    def set_address(self, address):
        ValueChecker.is_string(address)
        self.__address = address
        return self

    def get_address(self):
        return self.__address

    def get_config(self):
        raise Exception(
            'You can\'t use CheckPing for your configuration directly. Please use CheckPing4 or CheckPing6 instead')

    def validate(self):
        if None is self.__address:
            raise Exception('You have to specify an address for ' + self.get_id())
