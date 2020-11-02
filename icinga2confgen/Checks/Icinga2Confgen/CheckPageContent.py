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
from icinga2confgen.Commands.Icinga2Confgen.PageContentCommand import PageContentCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckPageContent(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckPageContent', 'page_content')
        self.__ok = None
        self.__warning = None
        self.__critical = None
        self.__header = None
        self.__uri = None
        self.__domain = None
        self.__port = None
        self.__ssl = False
        self.__client_cert = None
        self.__client_key = None
        self.add_service_group(ServiceGroup.create('webserver'))

    def set_ok(self, ok):
        ValueChecker.is_string(ok)
        if None is self.__ok:
            self.__ok = []
        self.__ok.append(ok)
        return self

    def get_ok(self):
        return self.__ok

    def set_warning(self, warning):
        ValueChecker.is_string(warning)
        if None is self.__warning:
            self.__warning = []
        self.__warning.append(warning)
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, critical):
        ValueChecker.is_string(critical)
        if None is self.__critical:
            self.__critical = []
        self.__critical.append(critical)
        return self

    def get_critical(self):
        return self.__critical

    def set_header(self, header):
        ValueChecker.is_string(header)
        if None is self.__header:
            self.__header = []
        self.__header.append(header)
        return self

    def get_header(self):
        return self.__header

    def set_uri(self, uri):
        ValueChecker.is_string(uri)
        self.__uri = uri
        return self

    def get_uri(self):
        return self.__uri

    def set_domain(self, domain):
        ValueChecker.is_string(domain)
        self.__domain = domain
        return self

    def get_domain(self):
        return self.__domain

    def set_port(self, port):
        ValueChecker.is_number(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    def set_ssl(self, ssl):
        ValueChecker.is_bool(ssl)
        self.__ssl = ssl
        return self

    def get_ssl(self):
        return self.__ssl

    def set_client_cert(self, client_cert):
        ValueChecker.is_string(client_cert)
        self.__client_cert = client_cert
        return self

    def get_client_cert(self):
        return self.__client_cert

    def set_client_key(self, client_key):
        ValueChecker.is_string(client_key)
        self.__client_key = client_key
        return self

    def get_client_key(self):
        return self.__client_key

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            id = 'check_' + id
            check = CheckPageContent(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('page_content'):
            PageContentCommand.create('page_content')

        return check

    def validate(self):
        if None is self.__domain:
            raise Exception('You have to specify a domain for ' + self.get_id())
