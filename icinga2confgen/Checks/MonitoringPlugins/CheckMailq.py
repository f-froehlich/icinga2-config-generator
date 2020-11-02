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
from icinga2confgen.Commands.MonitoringPlugins.MailqCommand import MailqCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckMailq(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckMailq', 'mailq')
        self.__warning = None
        self.__critical = None
        self.__warning_same_domain = None
        self.__critical_same_domain = None
        self.__sudo = False
        self.add_service_group(ServiceGroup.create('mailq'))
        self.add_service_group(ServiceGroup.create('mail'))

    def set_warning(self, warning):
        ValueChecker.is_number(warning)
        self.__warning = warning
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, critical):
        ValueChecker.is_number(critical)
        self.__critical = critical
        return self

    def get_critical(self):
        return self.__critical

    def set_warning_same_domain(self, warning_same_domain):
        ValueChecker.is_number(warning_same_domain)
        self.__warning_same_domain = warning_same_domain
        return self

    def get_warning_same_domain(self):
        return self.__warning_same_domain

    def set_critical_same_domain(self, critical_same_domain):
        ValueChecker.is_number(critical_same_domain)
        self.__critical_same_domain = critical_same_domain
        return self

    def get_critical_same_domain(self):
        return self.__critical_same_domain

    def set_sudo(self, sudo):
        ValueChecker.is_bool(sudo)
        self.__sudo = sudo
        return self

    def get_sudo(self):
        return self.__sudo

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckMailq(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('mailq'):
            MailqCommand.create('mailq')

        return check

    def validate(self):
        if None is self.__warning:
            raise Exception('You have to specify a warning for ' + self.get_id())
        if None is self.__critical:
            raise Exception('You have to specify a criitical for ' + self.get_id())
