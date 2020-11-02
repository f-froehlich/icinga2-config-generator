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
from icinga2confgen.Commands.MonitoringPlugins.MySQLCommand import MySQLCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckMySQL(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckMySQL', 'mysql')
        self.__host = '127.0.0.1'
        self.__port = 3306
        self.__ignore_auth = False
        self.__socket = None
        self.__database = None
        self.__file = None
        self.__group = None
        self.__user = None
        self.__password = None
        self.__check_slave = False
        self.__slave_warning = None
        self.__slave_critical = None
        self.__use_ssl = False
        self.__ssl_ciphers = None
        self.__ca_cert = None
        self.__ca_dir = None
        self.__cert = None
        self.__key = None
        self.add_service_group(ServiceGroup.create('mysql'))
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

    def set_ignore_auth(self, ignore_auth):
        ValueChecker.is_bool(ignore_auth)
        self.__ignore_auth = ignore_auth
        return self

    def get_ignore_auth(self):
        return self.__ignore_auth

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

    def set_check_slave(self, check_slave):
        ValueChecker.is_bool(check_slave)
        self.__check_slave = check_slave
        return self

    def get_check_slave(self):
        return self.__check_slave

    def set_slave_warning(self, slave_warning):
        ValueChecker.is_string(slave_warning)
        self.__slave_warning = slave_warning
        return self

    def get_slave_warning(self):
        return self.__slave_warning

    def set_slave_critical(self, slave_critical):
        ValueChecker.is_string(slave_critical)
        self.__slave_critical = slave_critical
        return self

    def get_slave_critical(self):
        return self.__slave_critical

    def set_use_ssl(self, use_ssl):
        ValueChecker.is_bool(use_ssl)
        self.__use_ssl = use_ssl
        return self

    def get_use_ssl(self):
        return self.__use_ssl

    def set_ssl_ciphers(self, ssl_ciphers):
        ValueChecker.is_string(ssl_ciphers)
        self.__ssl_ciphers = ssl_ciphers
        return self

    def get_ssl_ciphers(self):
        return self.__ssl_ciphers

    def set_ca_cert(self, ca_cert):
        ValueChecker.is_string(ca_cert)
        self.__ca_cert = ca_cert
        return self

    def get_ca_cert(self):
        return self.__ca_cert

    def set_ca_dir(self, ca_dir):
        ValueChecker.is_string(ca_dir)
        self.__ca_dir = ca_dir
        return self

    def get_ca_dir(self):
        return self.__ca_dir

    def set_cert(self, cert):
        ValueChecker.is_string(cert)
        self.__cert = cert
        return self

    def get_cert(self):
        return self.__cert

    def set_key(self, key):
        ValueChecker.is_string(key)
        self.__key = key
        return self

    def get_key(self):
        return self.__key

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckMySQL(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('mysql'):
            MySQLCommand.create('mysql')

        return check

    def validate(self):
        pass
