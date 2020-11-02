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
from icinga2confgen.Commands.MonitoringPlugins.HttpCommand import HttpCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckHttp(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckHttp', 'http')
        self.__vhost = None
        self.__ip = None
        self.__port = None
        self.__use_ipv4 = False
        self.__use_ipv6 = False
        self.__ssl = False
        self.__ssl_protocol = None
        self.__sni = False
        self.__certificate = False
        self.__certificate_warning_days = 29
        self.__certificate_critical_days = 15
        self.__continue_after_certificate = False
        self.__client_cert = None
        self.__client_cert_key = None
        self.__expect = 'HTTP/1.1 200'
        self.__expect_header = None
        self.__expect_content = None
        self.__uri = "/"
        self.__post_data = None
        self.__method = None
        self.__no_body = False
        self.__max_age = None
        self.__content_type = None
        self.__linespan = False
        self.__regex = None
        self.__eregi = None
        self.__invert_regex = False
        self.__authorization = False
        self.__authorization_username = None
        self.__authorization_password = None
        self.__proxy_authorization = False
        self.__proxy_authorization_username = None
        self.__proxy_authorization_password = None
        self.__useragent = None
        self.__header = None
        self.__extended_perfdata = False
        self.__show_url = False
        self.__link = False
        self.__onredirect = None
        self.__pagesize = None
        self.__pagesize_min = None
        self.__pagesize_max = None
        self.__warning = 7
        self.__critical = 15
        self.__timeout = 10
        self.add_service_group(ServiceGroup.create('webserver'))

    def set_vhost(self, vhost):
        ValueChecker.is_string(vhost)
        self.__vhost = vhost

        return self

    def get_vhost(self):
        return self.__vhost

    def set_ip(self, ip):
        ValueChecker.is_string(ip)
        self.__ip = ip

        return self

    def get_ip(self):
        return self.__ip

    def set_port(self, port):
        ValueChecker.is_number(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    def set_ssl(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__ssl = enabled
        return self

    def get_ssl(self):
        return self.__ssl

    def set_ssl_protocol(self, protocol):
        ValueChecker.is_string(protocol)
        self.__ssl_protocol = protocol
        return self

    def get_ssl_protocol(self):
        return self.__ssl_protocol

    def set_sni(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__sni = enabled
        return self

    def get_sni(self):
        return self.__sni

    def set_certificate_check(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__certificate = enabled
        return self

    def get_certificate_check(self):
        return self.__certificate

    def set_certificate_warning_days(self, days):
        ValueChecker.is_number(days)
        self.__certificate_warning_days = days
        return self

    def get_certificate_warning_days(self):
        return self.__certificate_warning_days

    def set_certificate_critical_days(self, days):
        ValueChecker.is_number(days)
        self.__certificate_critical_days = days
        return self

    def get_certificate_critical_days(self):
        return self.__certificate_critical_days

    def set_continue_after_certificate(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__continue_after_certificate = enabled
        return self

    def get_continue_after_certificate(self):
        return self.__continue_after_certificate

    def set_client_cert_file(self, path):
        ValueChecker.is_string(path)
        self.__client_cert = path
        return self

    def get_client_cert_file(self):
        return self.__client_cert

    def set_client_cert_key_file(self, path):
        ValueChecker.is_string(path)
        self.__client_cert_key = path
        return self

    def get_client_cert_key_file(self):
        return self.__client_cert_key

    def set_expect(self, expect):
        ValueChecker.is_string(expect)
        self.__expect = expect
        return self

    def get_expect(self):
        return self.__expect

    def set_expect_header(self, expect):
        ValueChecker.is_string(expect)
        self.__expect_header = expect
        return self

    def get_expect_header(self):
        return self.__expect_header

    def set_expect_content(self, expect):
        ValueChecker.is_string(expect)
        self.__expect_content = expect
        return self

    def get_expect_content(self):
        return self.__expect_content

    def set_uri(self, uri):
        ValueChecker.is_string(uri)
        self.__uri = uri
        return self

    def get_uri(self):
        return self.__uri

    def set_post_data(self, post_data):
        ValueChecker.is_string(post_data)
        self.__post_data = post_data
        return self

    def get_post_data(self):
        return self.__post_data

    def set_method(self, method):
        ValueChecker.is_http_method(method)
        self.__method = method
        return self

    def get_method(self):
        return self.__method

    def set_no_body(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__no_body = enabled
        return self

    def get_no_body(self):
        return self.__no_body

    def set_max_age(self, age):
        ValueChecker.is_number(age)
        self.__max_age = age
        return self

    def get_max_age(self):
        return self.__max_age

    def set_content_type(self, content_type):
        ValueChecker.is_string(content_type)
        self.__content_type = content_type
        return self

    def get_content_type(self):
        return self.__content_type

    def set_linespan(self, linespan):
        ValueChecker.is_bool(linespan)
        self.__linespan = linespan
        return self

    def get_linespan(self):
        return self.__linespan

    def set_regex(self, regex):
        ValueChecker.is_string(regex)
        self.__regex = regex
        return self

    def get_regex(self):
        return self.__regex

    def set_regex_case_insensitive(self, regex_case_insensitive):
        ValueChecker.is_string(regex_case_insensitive)
        self.__eregi = regex_case_insensitive
        return self

    def get_regex_case_insensitive(self):
        return self.__eregi

    def set_invert_regex(self, invert_regex):
        ValueChecker.is_bool(invert_regex)
        self.__invert_regex = invert_regex
        return self

    def get_invert_regex(self):
        return self.__invert_regex

    def set_authorization(self, username, password):
        ValueChecker.is_string(username)
        ValueChecker.is_string(password)
        self.__authorization = True
        self.__authorization_username = username
        self.__authorization_password = password
        return self

    def disable_authorization(self):
        self.__authorization = False

    def get_authorization(self):
        return {
            'enabled': self.__authorization,
            'username': self.__authorization_username,
            'password': self.__authorization_password
        }

    def set_proxy_authorization(self, username, password):
        ValueChecker.is_string(username)
        ValueChecker.is_string(password)
        self.__proxy_authorization = True
        self.__proxy_authorization_username = username
        self.__proxy_authorization_password = password
        return self

    def disable_proxy_authorization(self):
        self.__proxy_authorization = False
        return self

    def get_proxy_authorization(self):
        return {
            'enabled': self.__proxy_authorization,
            'username': self.__proxy_authorization_username,
            'password': self.__proxy_authorization_password
        }

    def set_useragent(self, agent):
        ValueChecker.is_string(agent)
        self.__useragent = agent
        return self

    def get_useragent(self):
        return self.__useragent

    def set_header(self, header):
        ValueChecker.is_array(header)
        self.__header = header
        return self

    def get_header(self):
        return self.__header

    def set_extended_perfdata(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__extended_perfdata = enabled
        return self

    def get_extended_perfdata(self):
        return self.__extended_perfdata

    def set_onredirect(self, onredirect):
        ValueChecker.is_string(onredirect)
        self.__onredirect = onredirect
        return self

    def get_onredirect(self):
        return self.__onredirect

    def set_pagesize(self, min, max):
        ValueChecker.is_number(min)
        ValueChecker.is_number(max)
        self.__pagesize_min = min
        self.__pagesize_max = max
        self.__pagesize = True
        return self

    def disable_pagesize(self):
        self.__pagesize = False
        return self

    def get_pagesize(self):
        return {
            'enabled': self.__pagesize,
            'min': self.__pagesize_min,
            'max': self.__pagesize_max
        }

    def set_warning_response_time(self, time):
        ValueChecker.is_number(time)
        self.__warning = time
        return self

    def get_warning_response_time(self):
        return self.__warning

    def set_critical_response_time(self, time):
        ValueChecker.is_number(time)
        self.__critical = time
        return self

    def get_critical_response_time(self):
        return self.__critical

    def set_timeout(self, seconds):
        ValueChecker.is_number(seconds)
        self.__timeout = seconds
        return self

    def get_timeout(self):
        return self.__timeout

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckHttp(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('http'):
            HttpCommand.create('http')

        return check

    def validate(self):
        if None is self.__vhost and None is self.__ip:
            raise Exception('You have to specify a vhost or ip for ' + self.get_id())
