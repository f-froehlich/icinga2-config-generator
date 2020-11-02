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
from icinga2confgen.Commands.MonitoringPlugins.PgSQLCommand import PgSQLCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckPgSQL(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckPgSQL', 'pgsql')
        self.__host = None
        self.__port = 5432
        self.__database = None
        self.__logname = None
        self.__password = None
        self.__option = None
        self.__warning = None
        self.__critical = None
        self.__timeout = 10
        self.__query = None
        self.__warning_range = None
        self.__critical_range = None
        self.add_service_group(ServiceGroup.create('postgres'))
        self.add_service_group(ServiceGroup.create('database'))

    def set_host(self, host):
        ValueChecker.is_string(host)
        self.__host = host
        return self

    def get_host(self):
        return self.__host

    def set_port(self, port):
        ValueChecker.is_number(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    def set_database(self, database):
        ValueChecker.is_string(database)
        self.__database = database
        return self

    def get_database(self):
        return self.__database

    def set_logname(self, logname):
        ValueChecker.is_string(logname)
        self.__logname = logname
        return self

    def get_logname(self):
        return self.__logname

    def set_password(self, password):
        ValueChecker.is_string(password)
        self.__password = password
        return self

    def get_password(self):
        return self.__password

    def set_option(self, option):
        ValueChecker.is_string(option)
        self.__option = option
        return self

    def get_option(self):
        return self.__option

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

    def set_timeout(self, timeout):
        ValueChecker.is_number(timeout)
        self.__timeout = timeout
        return self

    def get_timeout(self):
        return self.__timeout

    def set_query(self, query):
        ValueChecker.is_string(query)
        self.__query = query
        return self

    def get_query(self):
        return self.__query

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

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckPgSQL(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('pgsql'):
            PgSQLCommand.create('pgsql')

        return check

    def validate(self):
        pass
