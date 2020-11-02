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
from icinga2confgen.Commands.MonitoringPlugins.ProcsCommand import ProcsCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckProcs(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckProcs', 'procs')
        self.__warning_range = None
        self.__critical_range = None
        self.__metric = None
        self.__timeout = 10
        self.__traditional = False
        self.__state = None
        self.__pid = None
        self.__vsz = None
        self.__user = None
        self.__argument = None
        self.__argument_ereg = None
        self.__command = None
        self.__only_non_kernel = False
        self.add_service_group(ServiceGroup.create('procs'))
        self.add_service_group(ServiceGroup.create('system_health'))

    def set_warning_range(self, warning_range):
        ValueChecker.is_string(warning_range)
        self.__warning_range = warning_range
        return self

    def get_warning_range(self):
        return self.__warning_range

    def set_critical_range(self, critical_range):
        ValueChecker.is_string(critical_range)
        self.__critical_range = critical_range
        return self

    def get_critical_range(self):
        return self.__critical_range

    def set_metric(self, metric):
        ValueChecker.is_string(metric)
        self.__metric = metric
        return self

    def get_metric(self):
        return self.__metric

    def set_timeout(self, timeout):
        ValueChecker.is_number(timeout)
        self.__timeout = timeout
        return self

    def get_timeout(self):
        return self.__timeout

    def set_traditional(self, traditional):
        ValueChecker.is_bool(traditional)
        self.__traditional = traditional
        return self

    def get_traditional(self):
        return self.__traditional

    def set_state(self, state):
        ValueChecker.is_string(state)
        self.__state = state
        return self

    def get_state(self):
        return self.__state

    def set_pid(self, pid):
        ValueChecker.is_string(pid)
        self.__pid = pid
        return self

    def get_pid(self):
        return self.__pid

    def set_vsz(self, vsz):
        ValueChecker.is_string(vsz)
        self.__vsz = vsz
        return self

    def get_vsz(self):
        return self.__vsz

    def set_user_of_threads(self, user):
        ValueChecker.is_string(user)
        self.__user = user
        return self

    def get_user_of_threads(self):
        return self.__user

    def set_argument(self, argument):
        ValueChecker.is_string(argument)
        self.__argument = argument
        return self

    def get_argument(self):
        return self.__argument

    def set_argument_ereg(self, argument_ereg):
        ValueChecker.is_string(argument_ereg)
        self.__argument_ereg = argument_ereg
        return self

    def get_argument_ereg(self):
        return self.__argument_ereg

    def set_command(self, command):
        ValueChecker.is_string(command)
        self.__command = command
        return self

    def get_command(self):
        return self.__command

    def set_only_non_kernel(self, only_non_kernel):
        ValueChecker.is_bool(only_non_kernel)
        self.__only_non_kernel = only_non_kernel
        return self

    def get_only_non_kernel(self):
        return self.__only_non_kernel

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckProcs(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('procs'):
            ProcsCommand.create('procs')

        return check

    def validate(self):
        pass
