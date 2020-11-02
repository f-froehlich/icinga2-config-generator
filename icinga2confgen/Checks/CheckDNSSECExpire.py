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
from icinga2confgen.Commands.DNSSECExpireCommand import DNSSECExpireCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckDNSSECExpire(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckDNSSECExpire', 'dnssec_expiry')
        self.__warning = '10d'
        self.__critical = '5d'
        self.__zone = None
        self.__resolver = '1.1.1.1'
        self.__failing_domain = None
        self.__record_type = None
        self.set_check_interval('3h')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('dns'))
        self.add_service_group(ServiceGroup.create('dnssec'))

    def set_warning(self, warning):
        ValueChecker.is_string(warning)
        self.__warning = warning
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, critical):
        ValueChecker.is_string(critical)
        self.__critical = critical
        return self

    def get_critical(self):
        return self.__critical

    def set_zone(self, zone):
        ValueChecker.is_string(zone)
        self.__zone = zone
        return self

    def get_zone(self):
        return self.__zone

    def set_resolver(self, resolver):
        ValueChecker.is_string(resolver)
        self.__resolver = resolver
        return self

    def get_resolver(self):
        return self.__resolver

    def set_failing_domain(self, failing_domain):
        ValueChecker.is_string(failing_domain)
        self.__failing_domain = failing_domain
        return self

    def get_failing_domain(self):
        return self.__failing_domain

    def set_record_type(self, record_type):
        ValueChecker.is_string(record_type)
        self.__record_type = record_type
        return self

    def get_record_type(self):
        return self.__record_type

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckDNSSECExpire(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('dnssec_expiry'):
            DNSSECExpireCommand.create('dnssec_expiry')

        return check

    def validate(self):
        if None is self.__zone:
            raise Exception('You have to specify a zone for ' + self.get_id())
