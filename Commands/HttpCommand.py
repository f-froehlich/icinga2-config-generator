#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, commands, checks, ... in python
#
#  Copyright (c) 2020 Fabian Fröhlich <mail@f-froehlich.de> https://f-froehlich.de
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

from Commands.Command import Command
from ConfigBuilder import ConfigBuilder


class HttpCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id):
        ConfigBuilder.validate_id(id)
        command = ConfigBuilder.get_command(id)
        if None is command:
            id = 'command_' + id
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
      set_if = "$command_http_port$"
    }
    "--use-ipv4" = {
      set_if = "$command_http_v4$"
    }
    "--use-ipv6" = {
      set_if = "$command_http_v6$"
    }
    "--ssl" = {
      set_if = "$command_http_ssl$"
    }
    "--ssl=2" = {
      set_if = "$command_http_sslv2$"
    }
    "--ssl=2+" = {
      set_if = "$command_http_sslv2_greater$"
    }
    "--ssl=3" = {
      set_if = "$command_http_sslv3$"
    }
    "--ssl=3+" = {
      set_if = "$command_http_sslv3_greater$"
    }
    "--ssl=1" = {
      set_if = "$command_http_tlsv1$"
    }
    "--ssl=1+" = {
      set_if = "$command_http_tlsv1_greater$"
    }
    "--ssl=1.1" = {
      set_if = "$command_http_sslv1_1$"
    }
    "--ssl=1.1+" = {
      set_if = "$command_http_sslv1_1_greater$"
    }
    "--ssl=1.2" = {
      set_if = "$command_http_sslv1_2$"
    }
    "--ssl=1.2+" = {
      set_if = "$command_http_sslv1_2_greater$"
    }
    "--ssl=1.3" = {
      set_if = "$command_http_sslv1_3$"
    }
    "--ssl=1.3+" = {
      set_if = "$command_http_sslv1_3_greater$"
    }
    "--sni" = {
      set_if = "$command_http_sni$"
    }
    "--certificate" = {
      value = "$command_http_certificate_warning_days$,$command_http_certificate_critical_days$"
      set_if = "$command_http_certificate$"
    }
    "--continue-after-certificate" = {
      set_if = "$command_http_continue_after_certificate$"
    }
    "--client-cert" = {
      value = "$command_http_client_cert$"
      set_if = "$command_http_client_cert$"
    }
    "--private-key" = {
      value = "$command_http_client_cert_key$"
      set_if = "$command_http_client_cert_key$"
    }
    "--expect" = {
      value = "$command_http_expect$"
      set_if = "$command_http_expect$"
    }
    "--header-string" = {
      value = "$command_http_expect_header$"
      set_if = "$command_http_expect_header$"
    }
    "--string" = {
      value = "$command_http_expect_content$"
      set_if = "$command_http_expect_content$"
    }
    "--url" = {
      value = "$command_http_uri$"
    }
    "--post" = {
      value = "$command_http_post_data$"
      set_if = "$command_http_post_data$"
    }
    "--method" = {
      value = "$command_http_method$"
      set_if = "$command_http_method$"
    }
    "--no-body" = {
      set_if = "$command_http_no_body$"
    }
    "--max-age" = {
      value = "$command_http_max_age$"
      set_if = "$command_http_max_age$"
    }
    "--content-type" = {
      value = "$command_http_content_type$"
      set_if = "$command_http_content_type$"
    }
    "--linespan" = {
      set_if = "$command_http_linespan$"
    }
    "--regex" = {
      value = "$command_http_regex$"
      set_if = "$command_http_regex$"
    }
    "--eregi" = {
      value = "$command_http_eregi$"
      set_if = "$command_http_eregi$"
    }
    "--invert-regex" = {
      set_if = "$command_http_invert_regex$"
    }
    "--authorization" = {
      value = "$command_http_authorization_username$:$command_http_authorization_password$"
      set_if = "$command_http_authorization$"
    }
    "--proxy-authorization" = {
      value = "$command_http_proxy_authorization_username$:$command_http_proxy_authorization_password$"
      set_if = "$command_http_proxy_authorization$"
    }
    "--useragent" = {
      value = "$command_http_useragent$"
      set_if = "$command_http_useragent$"
    }
    "--header" = {
      value = "$command_http_header$"
      set_if = "$command_http_header$"
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
      set_if = "$command_http_pagesize$"
    }
    "--warning" = {
      value = "$command_http_warning$"
      set_if = "$command_http_warning$"
    }
    "--critical" = {
      value = "$command_http_critical$"
      set_if = "$command_http_critical$"
    }
    "--timeout" = {
      value = "$command_http_timeout$"
      set_if = "$command_http_timeout$"
    }
  }
"""
