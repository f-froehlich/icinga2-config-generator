#!/usr/bin/python3
# -*- coding: utf-8
import typing

from icinga2confgen.Commands.Command import Command
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker

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

T = typing.TypeVar('T', bound='CheckSSLCertCommand')


class CheckSSLCertCommand(Command):

    def __init__(self: T, id: str):
        Command.__init__(self, id)

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = CheckSSLCertCommand(id)
            ConfigBuilder.add_command(id, command)
        elif not isinstance(command, CheckSSLCertCommand):
            raise Exception('Id must be for an instance of CheckSSLCertCommand but other instance is returned')

        return command

    def get_command_definition(self: T) -> str:
        return '[ "$matteocorti_plugin_dir$" + "/' + self.get_command() + '"]'

    def get_command(self: T) -> str:
        return 'check_ssl_cert'

    def get_arguments(self: T) -> str:
        config = """{
    "--file" = {
        value = "$command_matteocorti_ssl_cert_file$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_file$") != false }}
    }
    "--host" = {
        value = "$command_matteocorti_ssl_cert_host$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_host$") != false }}
    } 
    "--clientcert" = {
        value = "$command_matteocorti_ssl_cert_clientcert$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_clientcert$") != false }}
    }
    "--check-ciphers" = {
        value = "$command_matteocorti_ssl_cert_check_ciphers$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_check_ciphers$") != false }}
    }
    "--check-ssl-labs-warn" = {
        value = "$command_matteocorti_ssl_cert_check_ssl_labs_warn$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_check_ssl_labs_warn$") != false }}
    }
    "--clientpass" = {
        value = "$command_matteocorti_ssl_cert_clientpass$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_clientpass$") != false }}
    }
    "--configuration" = {
        value = "$command_matteocorti_ssl_cert_configuration$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_configuration$") != false }}
    }
    "--curl-bin" = {
        value = "$command_matteocorti_ssl_cert_curl_bin$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_curl_bin$") != false }}
    }
    "--custom-http-header" = {
        value = "$command_matteocorti_ssl_cert_custom_http_header$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_custom_http_header$") != false }}
    }
    "--date" = {
        value = "$command_matteocorti_ssl_cert_date$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_date$") != false }}
    }
    "--debug-file" = {
        value = "$command_matteocorti_ssl_cert_debug_file$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_debug_file$") != false }}
    }
    "--dig-bin" = {
        value = "$command_matteocorti_ssl_cert_dig_bin$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_dig_bin$") != false }}
    }
    "--email" = {
        value = "$command_matteocorti_ssl_cert_email$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_email$") != false }}
    }
    
    "--file-bin" = {
        value = "$command_matteocorti_ssl_cert_file_bin$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_file_bin$") != false }}
    }
    "--fingerprint" = {
        value = "$command_matteocorti_ssl_cert_fingerprint$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_fingerprint$") != false }}
    }
    "--format" = {
        value = "$command_matteocorti_ssl_cert_format$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_format$") != false }}
    }
    "--grep-bin" = {
        value = "$command_matteocorti_ssl_cert_grep_bin$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_grep_bin$") != false }}
    }
    "--http-headers-path" = {
        value = "$command_matteocorti_ssl_cert_http_headers_path$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_http_headers_path$") != false }}
    }
    "--issuer" = {
        value = "$command_matteocorti_ssl_cert_issuer$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_issuer$") != false }}
    }
    "--inetproto" = {
        value = "$command_matteocorti_ssl_cert_inetproto$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_inetproto$") != false }}
    }
    "--issuer-cert-cache" = {
        value = "$command_matteocorti_ssl_cert_issuer_cert_cache$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_issuer_cert_cache$") != false }}
    }
    "--jks-alias" = {
        value = "$command_matteocorti_ssl_cert_jks_alias$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_jks_alias$") != false }}
    }
    "--clientkey" = {
        value = "$command_matteocorti_ssl_cert_clientkey$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_clientkey$") != false }}
    }
    "--check-ssl-labs" = {
        value = "$command_matteocorti_ssl_cert_check_ssl_labs$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_check_ssl_labs$") != false }}
    }
    "--maximum-validity" = {
        value = "$command_matteocorti_ssl_cert_maximum_validity$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_maximum_validity$") != false }}
    }
    "--nmap-bin" = {
        value = "$command_matteocorti_ssl_cert_nmap_bin$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_nmap_bin$") != false }}
    }
    "--not-issued-by" = {
        value = "$command_matteocorti_ssl_cert_not_issued_by$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_not_issued_by$") != false }}
    }
    "--not-valid-longer-than" = {
        value = "$command_matteocorti_ssl_cert_not_valid_longer_than$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_not_valid_longer_than$") != false }}
    }
    "--org" = {
        value = "$command_matteocorti_ssl_cert_org$"
        set_if = {{ macro("$command_ssl_org$") != false }}
    }
    "--openssl" = {
        value = "$command_matteocorti_ssl_cert_openssl$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_openssl$") != false }}
    }
    "--path" = {
        value = "$command_matteocorti_ssl_cert_path$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_path$") != false }}
    }
    "--precision" = {
        value = "$command_matteocorti_ssl_cert_precision$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_precision$") != false }}
    }
    "--protocol" = {
        value = "$command_matteocorti_ssl_cert_protocol$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_protocol$") != false }}
    }
    "--password" = {
        value = "$command_matteocorti_ssl_cert_password$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_password$") != false }}
    }
    "--proxy" = {
        value = "$command_matteocorti_ssl_cert_proxy$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_proxy$") != false }}
    }
    "--python-bin" = {
        value = "$command_matteocorti_ssl_cert_python_bin$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_python_bin$") != false }}
    }
    "--rootcert" = {
        value = "$command_matteocorti_ssl_cert_rootcert$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_rootcert$") != false }}
    }
    "--require-dnssec" = {
        set_if = "$command_matteocorti_ssl_cert_require_dnssec$"
    }
    "--require-http_header" = {
        value = "$command_matteocorti_ssl_cert_require_http_header$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_require_http_header$") != false }}
    }
    "--require-no-http_header" = {
        value = "$command_matteocorti_ssl_cert_require_no_http_header$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_require_no_http_header$") != false }}
    }
    "--resolve" = {
        value = "$command_matteocorti_ssl_cert_resolve$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_resolve$") != false }}
    }
    "--rootcert-dir" = {
        value = "$command_matteocorti_ssl_cert_rootcert_dir$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_rootcert_dir$") != false }}
    }
    "--rootcert-file" = {
        value = "$command_matteocorti_ssl_cert_rootcert_dir$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_rootcert_file$") != false }}
    }
    "--serial" = {
        value = "$command_matteocorti_ssl_cert_serial$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_serial$") != false }}
    }
    "--sni" = {
        value = "$command_matteocorti_ssl_cert_sni$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_sni$") != false }}
    }
    "--timeout" = {
        value = "$command_matteocorti_ssl_cert_timeout$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_timeout$") != false }}
    }
    "--temp" = {
        value = "$command_matteocorti_ssl_cert_temp$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_temp$") != false }}
    }
    "--url" = {
        value = "$command_matteocorti_ssl_cert_url$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_url$") != false }}
    }
    "--user-agent" = {
        value = "$command_matteocorti_ssl_cert_user_agent$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_user_agent$") != false }}
    }
    "--xmpphost" = {
        value = "$command_matteocorti_ssl_cert_xmpphost$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_xmpphost$") != false }}
    }
    "--security-level" = {
        value = "$command_matteocorti_ssl_cert_security_level$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_security_level$") != false }}
    }
    "--port" = {
        value = "$command_matteocorti_ssl_cert_port$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_port$") != false }}
    }
    "--ocsp-critical" = {
        value = "$command_matteocorti_ssl_cert_ocsp_critical$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_ocsp_critical$") != false }}
    }
    "--ocsp-warning" = {
        value = "$command_matteocorti_ssl_cert_ocsp_warning$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_ocsp_warning$") != false }}
    }
    "--critical" = {
        value = "$command_matteocorti_ssl_cert_critical$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_critical$") != false }}
    }
    "--warning" = {
        value = "$command_matteocorti_ssl_cert_warning$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_warning$") != false }}
    }
    "--element" = {
        value = "$command_matteocorti_ssl_cert_element$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_element$") != false }}
    }
    "--long-output" = {
        value = "$command_matteocorti_ssl_cert_long_output$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_long_output$") != false }}
    }
    "--require-client-cert" = {
        value = "$command_matteocorti_ssl_cert_require_client_cert$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_require_client_cert$") != false }}
    }
    "--skip-element" = {
        value = "$command_matteocorti_ssl_cert_skip_element$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_skip_element$") != false }}
        repeat_key = true
    }
    "--dane" = {
        value = "$command_matteocorti_ssl_cert_dane$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_dane$") != false }}
        repeat_key = true
    }
    "--match" = {
        value = "$command_matteocorti_ssl_cert_match$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_match$") != false }}
        repeat_key = true
    }
    "--require-purpose" = {
        value = "$command_matteocorti_ssl_cert_require_purpose$"
        set_if = {{ macro("$command_matteocorti_ssl_cert_require_purpose$") != false }}
        repeat_key = true
    }
    "--verbose" = {
        set_if = "$command_matteocorti_ssl_cert_verbose$"
    }
    "--terse" = {
        set_if = "$command_matteocorti_ssl_cert_terse$"
    }
    "--tls1" = {
        set_if = "$command_matteocorti_ssl_cert_tls1$"
    }
    "--tls1_1" = {
        set_if = "$command_matteocorti_ssl_cert_tls1_1$"
    }
    "--tls1_2" = {
        set_if = "$command_matteocorti_ssl_cert_tls1_2$"
    }
    "--tls1_3" = {
        set_if = "$command_matteocorti_ssl_cert_tls1_3$"
    }
    "--ssl2" = {
        set_if = "$command_matteocorti_ssl_cert_ssl2$"
    }
    "--ssl3" = {
        set_if = "$command_matteocorti_ssl_cert_ssl3$"
    }
    "--selfsigned" = {
        set_if = "$command_matteocorti_ssl_cert_selfsigned$"
    }
    "--rsa" = {
        set_if = "$command_matteocorti_ssl_cert_rsa$"
    }
    "--require-purpose-critical" = {
        set_if = "$command_matteocorti_ssl_cert_require_purpose_critical$"
    }
    "--require-no-ssl2" = {
        set_if = "$command_matteocorti_ssl_cert_require_no_ssl2$"
    }
    "--require-no-ssl3" = {
        set_if = "$command_matteocorti_ssl_cert_require_no_ssl3$"
    }
    "--require-no-tls1" = {
        set_if = "$command_matteocorti_ssl_cert_require_no_tls1$"
    }
    "--require-no-tls1_1" = {
        set_if = "$command_matteocorti_ssl_cert_require_no_tls1_1$"
    }
    "--require-ocsp-stapling" = {
        set_if = "$command_matteocorti_ssl_cert_require_ocsp_stapling$"
    }
    "--no-perf" = {
        set_if = "$command_matteocorti_ssl_cert_no_perf$"
    }
    "--no-proxy" = {
        set_if = "$command_matteocorti_ssl_cert_no_proxy$"
    }
    "--no-proxy-curl" = {
        set_if = "$command_matteocorti_ssl_cert_no_proxy_curl$"
    }
    "--no-proxy-s_client" = {
        set_if = "$command_matteocorti_ssl_cert_no_proxy_s_client$"
    }
    "--no-ssl2" = {
        set_if = "$command_matteocorti_ssl_cert_no_ssl2$"
    }
    "--no-ssl3" = {
        set_if = "$command_matteocorti_ssl_cert_no_ssl3$"
    }
    "--no-tls1" = {
        set_if = "$command_matteocorti_ssl_cert_no_tls1$"
    }
    "--no-tls1_1" = {
        set_if = "$command_matteocorti_ssl_cert_no_tls1_1$"
    }
    "--no-tls1_2" = {
        set_if = "$command_matteocorti_ssl_cert_no_tls1_2$"
    }
    "--no-tls1_3" = {
        set_if = "$command_matteocorti_ssl_cert_no_tls1_3$"
    }
    "--info" = {
        set_if = "$command_matteocorti_ssl_cert_info$"
    }
    "--init-host-cache" = {
        set_if = "$command_matteocorti_ssl_cert_init_host_cache$"
    }
    "--ignore-altnames" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_altnames$"
    }
    "--ignore-connection-problems" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_connection_problems$"
    }
    "--ignore-exp" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_exp$"
    }
    "--ignore-http-headers" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_http_headers$"
    }
    "--ignore-host-cn" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_host_cn$"
    }
    "--ignore-incomplete-chain" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_incomplete_chain$"
    }
    "--ignore-maximum-validity" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_maximum_validity$"
    }
    "--ignore-ocsp" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_ocsp$"
    }
    "--ignore-ocsp-errors" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_ocsp_errors$"
    }
    "--ignore-ocsp-timeout" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_ocsp_timeout$"
    }
    "--ignore-sct" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_sct$"
    }
    "--ignore-sig-alg" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_sig_alg$"
    }
    "--ignore-ssl-labs-cache" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_ssl_labs_cache$"
    }
    "--ignore-ssl-labs-errors" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_ssl_labs_errors$"
    }
    "--ignore-tls-renegotiation" = {
        set_if = "$command_matteocorti_ssl_cert_ignore_tls_renegotiation$"
    }
    "--http-use-get" = {
        set_if = "$command_matteocorti_ssl_cert_http_use_get$"
    }
    "--first-element-only" = {
        set_if = "$command_matteocorti_ssl_cert_first_element_only$"
    }
    "--force-dconv-date" = {
        set_if = "$command_matteocorti_ssl_cert_force_dconv_date$"
    }
    "--force-perl-date" = {
        set_if = "$command_matteocorti_ssl_cert_force_perl_date$"
    }
    "--ecdsa" = {
        set_if = "$command_matteocorti_ssl_cert_ecdsa$"
    }
    "--dtls" = {
        set_if = "$command_matteocorti_ssl_cert_dtls$"
    }
    "--dtls1" = {
        set_if = "$command_matteocorti_ssl_cert_dtls1$"
    }
    "--dtls1_2" = {
        set_if = "$command_matteocorti_ssl_cert_dtls1_2$"
    }
    "--debug" = {
        set_if = "$command_matteocorti_ssl_cert_debug$"
    }
    "--debug-cert" = {
        set_if = "$command_matteocorti_ssl_cert_debug_cert$"
    }
    "--debug-headers" = {
        set_if = "$command_matteocorti_ssl_cert_debug_headers$"
    }
    "--debug-time" = {
        set_if = "$command_matteocorti_ssl_cert_debug_time$"
    }
    "--default-format" = {
        set_if = "$command_matteocorti_ssl_cert_default_format$"
    }
    "--crl" = {
        set_if = "$command_matteocorti_ssl_cert_crl$"
    }
    "--check-ciphers-warnings" = {
        set_if = "$command_matteocorti_ssl_cert_check_ciphers_warnings$"
    }
    "--check-http-headers" = {
        set_if = "$command_matteocorti_ssl_cert_check_http_headers$"
    }
    "--check-chain" = {
        set_if = "$command_matteocorti_ssl_cert_check_chain$"
    }
    "--noauth" = {
        set_if = "$command_matteocorti_ssl_cert_noauth$"
    }
    "--all" = {
        set_if = "$command_matteocorti_ssl_cert_all$"
    }
    "--all-local" = {
        set_if = "$command_matteocorti_ssl_cert_all_local$"
    }
    "--allow-empty-san" = {
        set_if = "$command_matteocorti_ssl_cert_allow_empty_san$"
    }
    "-4" = {
        set_if = "$command_matteocorti_ssl_cert_ipv4$"
    }
    "-6" = {
        set_if = "$command_matteocorti_ssl_cert_ipv6$"
    }
}
"""

        return config
