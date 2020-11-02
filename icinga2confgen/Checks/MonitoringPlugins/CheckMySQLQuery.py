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
from icinga2confgen.Commands.MonitoringPlugins.MySQLQueryCommand import MySQLQueryCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckMysqlQuery(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckMysqlQuery', 'mysql_query')
        self.__query = None
        self.__warning = None
        self.__critical = None
        self.__host = '127.0.0.1'
        self.__port = 3306
        self.__socket = None
        self.__database = None
        self.__file = None
        self.__group = None
        self.__user = None
        self.__password = None
        self.add_service_group(ServiceGroup.create('mysql'))
        self.add_service_group(ServiceGroup.create('database'))

    def set_query(self, query):
        ValueChecker.is_string(query)
        self.__query = query
        return self

    def get_query(self):
        return self.__query

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

    def set_socket(self, socket):
        ValueChecker.is_string(socket)
        self.__socket = socket
        return self

    def get_socket(self):
        return self.__socket

    def set_database(self, database):
        ValueChecker.is_string(database)
        self.__database = database
        return self

    def get_database(self):
        return self.__database

    def set_file(self, file):
        ValueChecker.is_string(file)
        self.__file = file
        return self

    def get_file(self):
        return self.__file

    def set_group(self, group):
        ValueChecker.is_string(group)
        self.__group = group
        return self

    def get_group(self):
        return self.__group

    def set_user(self, user):
        ValueChecker.is_string(user)
        self.__user = user
        return self

    def get_user(self):
        return self.__user

    def set_password(self, password):
        ValueChecker.is_string(password)
        self.__password = password
        return self

    def get_password(self):
        return self.__password

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckMysqlQuery(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('mysql_query'):
            MySQLQueryCommand.create('mysql_query')

        return check

    def validate(self):
        if None is self.__query:
            raise Exception('You have to specify a query for ' + self.get_id())
