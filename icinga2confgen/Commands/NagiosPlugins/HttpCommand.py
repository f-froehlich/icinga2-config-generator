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

from icinga2confgen.Commands.Command import Command
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker


class HttpCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = HttpCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_http'

    def get_arguments(self):
        return """{
    "--hostname" = {
      value = "$command_http_vhost$"
    }
    "--IP-address" = {
      value = "$command_http_ip$"
    }
    "--port" = {
      value = "$command_http_port$"
      set_if = {{ macro("$command_http_port$") != false }}
    }
    "--use-ipv4" = {
      set_if = {{ macro("$command_http_v4$") != false }}
    }
    "--use-ipv6" = {
      set_if = "$command_http_v6$"
    }
    "-S" = {
      set_if = "$command_http_ssl$"
    }
    "--ssl" = {
      value = "$command_http_ssl_protocol$"
      set_if = {{ macro("$command_http_ssl_protocol$") != false }}
    }
    "--sni" = {
      set_if = "$command_http_sni$"
    }
    "--certificate" = {
      value = "$command_http_certificate_warning_days$,$command_http_certificate_critical_days$"
      set_if = {{ macro("$command_http_certificate$") != false }}
    }
    "--continue-after-certificate" = {
      set_if = "$command_http_continue_after_certificate$"
    }
    "--client-cert" = {
      value = "$command_http_client_cert$"
      set_if = {{ macro("$command_http_client_cert$") != false }}
    }
    "--private-key" = {
      value = "$command_http_client_cert_key$"
      set_if = {{ macro("$command_http_client_cert_key$") != false }}
    }
    "--expect" = {
      value = "$command_http_expect$"
      set_if = {{ macro("$command_http_expect$") != false }}
    }
    "--header-string" = {
      value = "$command_http_expect_header$"
      set_if = {{ macro("$command_http_expect_header$") != false }}
    }
    "--string" = {
      value = "$command_http_expect_content$"
      set_if = {{ macro("$command_http_expect_content$") != false }}
    }
    "--url" = {
      value = "$command_http_uri$"
    }
    "--post" = {
      value = "$command_http_post_data$"
      set_if = {{ macro("$command_http_post_data$") != false }}
    }
    "--method" = {
      value = "$command_http_method$"
      set_if = {{ macro("$command_http_method$") != false }}
    }
    "--no-body" = {
      set_if = "$command_http_no_body$"
    }
    "--max-age" = {
      value = "$command_http_max_age$"
      set_if = {{ macro("$command_http_max_age$") != false }}
    }
    "--content-type" = {
      value = "$command_http_content_type$"
      set_if = {{ macro("$command_http_content_type$") != false }}
    }
    "--linespan" = {
      set_if = "$command_http_linespan$"
    }
    "--regex" = {
      value = "$command_http_regex$"
      set_if = {{ macro("$command_http_regex$") != false }}
    }
    "--eregi" = {
      value = "$command_http_eregi$"
      set_if = {{ macro("$command_http_eregi$") != false }}
    }
    "--invert-regex" = {
      set_if = "$command_http_invert_regex$"
    }
    "--authorization" = {
      value = "$command_http_authorization_username$:$command_http_authorization_password$"
      set_if = {{ macro("$command_http_authorization$") != false }}
    }
    "--proxy-authorization" = {
      value = "$command_http_proxy_authorization_username$:$command_http_proxy_authorization_password$"
      set_if = {{ macro("$command_http_proxy_authorization$") != false }}
    }
    "--useragent" = {
      value = "$command_http_useragent$"
      set_if = {{ macro("$command_http_useragent$") != false }}
    }
    "--header" = {
      value = "$command_http_header$"
      set_if = {{ macro("$command_http_header$") != false }}
    }
    "--extended-perfdata" = {
      set_if = "$command_http_extended_perfdata$"
    }
    "--show-url" = {
      set_if = "$command_http_show_url$"
    }
    "--link" = {
      set_if = "$command_http_link$"
    }
    "--onredirect" = {
      value = "$command_http_onredirect$"
      set_if = "$command_http_onredirect$"
    }
    "--pagesize" = {
      value = "$command_http_pagesize_min$:$command_http_pagesize_max$"
      set_if = {{ macro("$command_http_pagesize$") != false }}
    }
    "--warning" = {
      value = "$command_http_warning$"
      set_if = {{ macro("$command_http_warning$") != false }}
    }
    "--critical" = {
      value = "$command_http_critical$"
      set_if = {{ macro("$command_http_critical$") != false }}
    }
    "--timeout" = {
      value = "$command_http_timeout$"
      set_if = {{ macro("$command_http_timeout$") != false }}
    }
  }
"""
