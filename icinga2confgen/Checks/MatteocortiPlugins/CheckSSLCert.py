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
from __future__ import annotations

import typing
from typing import Union

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.MatteocortiPlugins.CheckSSLCertCommand import CheckSSLCertCommand
from icinga2confgen.Commands.Other.SynologyStatusCommand import SynologyStatusCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='CheckSSLCert')


class CheckSSLCert(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckSSLCert', 'ssl_cert')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('webserver'))
        self.add_service_group(ServiceGroup.create('tls'))
        self.add_service_group(ServiceGroup.create('certificate_check'))

        self.__verbose: bool = False
        self.__terse: bool = False
        self.__tls1: bool = False
        self.__tls1_1: bool = False
        self.__tls1_2: bool = False
        self.__tls1_3: bool = False
        self.__ssl2: bool = False
        self.__ssl3: bool = False
        self.__selfsigned: bool = False
        self.__rsa: bool = False
        self.__require_purpose_critical: bool = False
        self.__require_no_ssl2: bool = False
        self.__require_no_ssl3: bool = False
        self.__require_no_tls1: bool = False
        self.__require_no_tls1_1: bool = False
        self.__require_ocsp_stapling: bool = False
        self.__no_perf: bool = False
        self.__no_proxy: bool = False
        self.__no_proxy_curl: bool = False
        self.__no_proxy_s_client: bool = False
        self.__no_ssl2: bool = False
        self.__no_ssl3: bool = False
        self.__no_tls1: bool = False
        self.__no_tls1_1: bool = False
        self.__no_tls1_2: bool = False
        self.__no_tls1_3: bool = False
        self.__info: bool = False
        self.__init_host_cache: bool = False
        self.__ignore_altnames: bool = False
        self.__ignore_connection_problems: bool = False
        self.__ignore_exp: bool = False
        self.__ignore_http_headers: bool = False
        self.__ignore_incomplete_chain: bool = False
        self.__ignore_host_cn: bool = False
        self.__ignore_maximum_validity: bool = False
        self.__ignore_ocsp: bool = False
        self.__ignore_ocsp_errors: bool = False
        self.__ignore_ocsp_timeout: bool = False
        self.__ignore_sct: bool = False
        self.__ignore_sig_alg: bool = False
        self.__ignore_ssl_labs_cache: bool = False
        self.__ignore_ssl_labs_errors: bool = False
        self.__ignore_tls_renegotiation: bool = False
        self.__http_use_get: bool = False
        self.__first_element_only: bool = False
        self.__force_dconv_date: bool = False
        self.__force_perl_date: bool = False
        self.__ecdsa: bool = False
        self.__dtls: bool = False
        self.__dtls1: bool = False
        self.__dtls1_2: bool = False
        self.__debug: bool = False
        self.__debug_cert: bool = False
        self.__debug_headers: bool = False
        self.__debug_time: bool = False
        self.__default_format: bool = False
        self.__crl: bool = False
        self.__check_ciphers_warnings: bool = False
        self.__check_http_headers: bool = False
        self.__check_chain: bool = False
        self.__noauth: bool = False
        self.__all: bool = False
        self.__all_local: bool = False
        self.__allow_empty_scan: bool = False
        self.__ipv4: bool = False
        self.__ipv6: bool = False

        # string values
        self.__file: Union[str, None] = None
        self.__host: Union[str, None] = None
        self.__clientcert: Union[str, None] = None
        self.__check_ciphers: Union[str, None] = None
        self.__check_ssl_labs_warn: Union[str, None] = None
        self.__clientpass: Union[str, None] = None
        self.__configuration: Union[str, None] = None
        self.__custom_http_header: Union[str, None] = None
        self.__curl_bin: Union[str, None] = None
        self.__date: Union[str, None] = None
        self.__debug_file: Union[str, None] = None
        self.__dig_bin: Union[str, None] = None
        self.__email: Union[str, None] = None
        self.__file_bin: Union[str, None] = None
        self.__fingerprint: Union[str, None] = None
        self.__grep_bin: Union[str, None] = None
        self.__format: Union[str, None] = None
        self.__http_headers_path: Union[str, None] = None
        self.__issuer: Union[str, None] = None
        self.__inetproto: Union[str, None] = None
        self.__issuer_cert_cache: Union[str, None] = None
        self.__jks_alias: Union[str, None] = None
        self.__clientkey: Union[str, None] = None
        self.__check_ssl_labs: Union[str, None] = None
        self.__maximum_validity: Union[str, None] = None
        self.__nmap_bin: Union[str, None] = None
        self.__not_issued_by: Union[str, None] = None
        self.__not_valid_longer_than: Union[str, None] = None
        self.__org: Union[str, None] = None
        self.__openssl: Union[str, None] = None
        self.__path: Union[str, None] = None
        self.__precision: Union[str, None] = None
        self.__protocol: Union[str, None] = None
        self.__password: Union[str, None] = None
        self.__proxy: Union[str, None] = None
        self.__python_bin: Union[str, None] = None
        self.__rootcert: Union[str, None] = None
        self.__require_dnssec: Union[str, None] = None
        self.__require_http_header: Union[str, None] = None
        self.__require_no_http_header: Union[str, None] = None
        self.__resolve: Union[str, None] = None
        self.__rootcert_dir: Union[str, None] = None
        self.__rootcert_file: Union[str, None] = None
        self.__serial: Union[str, None] = None
        self.__sni: Union[str, None] = None
        self.__timeout: Union[str, None] = None
        self.__temp: Union[str, None] = None
        self.__url: Union[str, None] = None
        self.__xmpphost: Union[str, None] = None
        self.__user_agent: Union[str, None] = None

        self.__security_level: Union[int, None] = None
        self.__port: Union[int, None] = None
        self.__ocsp_critical: Union[int, None] = None
        self.__ocsp_warning: Union[int, None] = None
        self.__critical: Union[int, None] = None
        self.__warning: Union[int, None] = None
        self.__element: Union[int, None] = None

        self.__long_output: Union[str, None] = None
        self.__long_output_values: typing.List[str] = []
        self.__require_client_cert: Union[str, None] = None
        self.__require_client_cert_values: typing.List[str] = []

        self.__skip_element: typing.List[int] = []
        self.__dane: typing.List[str] = []
        self.__match: typing.List[str] = []
        self.__require_purpose: typing.List[str] = []

    def set_skip_element(self: T, skip_element: typing.List[int]) -> T:
        self.__skip_element = skip_element
        return self

    def get_skip_element(self: T) -> typing.List[int]:
        return self.__skip_element

    def add_skip_element(self: T, skip_element: int) -> T:
        self.__skip_element.append(skip_element)
        return self

    def remove_skip_element(self: T, skip_element: int) -> T:
        if skip_element in self.__skip_element:
            self.__skip_element.remove(skip_element)
        return self

    def set_dane(self: T, dane: typing.List[str]) -> T:
        self.__dane = dane
        return self

    def get_dane(self: T) -> typing.List[str]:
        return self.__dane

    def add_dane(self: T, dane: str) -> T:
        self.__dane.append(dane)
        return self

    def remove_dane(self: T, dane: str) -> T:
        if dane in self.__dane:
            self.__dane.remove(dane)
        return self

    def set_match(self: T, match: typing.List[str]) -> T:
        self.__match = match
        return self

    def get_match(self: T) -> typing.List[str]:
        return self.__match

    def add_match(self: T, match: str) -> T:
        self.__match.append(match)
        return self

    def remove_match(self: T, match: str) -> T:
        if match in self.__match:
            self.__match.remove(match)
        return self

    def set_require_purpose(self: T, require_purpose: typing.List[str]) -> T:
        self.__require_purpose = require_purpose
        return self

    def get_require_purpose(self: T) -> typing.List[str]:
        return self.__require_purpose

    def add_require_purpose(self: T, require_purpose: str) -> T:
        self.__require_purpose.append(require_purpose)
        return self

    def remove_require_purpose(self: T, require_purpose: str) -> T:
        if require_purpose in self.__require_purpose:
            self.__require_purpose.remove(require_purpose)
        return self

    def set_long_output(self: T, long_output: typing.List[str]) -> T:
        self.__long_output_values = long_output
        if 0 != len(self.__long_output_values):
            self.__long_output = ",".join(long_output)
        else:
            self.__long_output = None
        return self

    def add_long_output(self: T, long_output: str) -> T:
        self.__long_output_values.append(long_output)
        self.__long_output = ",".join(self.__long_output_values)

        return self

    def remove_long_output(self: T, long_output: str) -> T:
        if long_output in self.__long_output_values:
            self.__long_output_values.remove(long_output)
            if 0 != len(self.__long_output_values):
                self.__long_output = ",".join(self.__long_output_values)
            else:
                self.__long_output = None
        return self

    def get_long_output(self) -> typing.List[str]:
        return self.__long_output_values

    def set_require_client_cert(self: T, require_client_cert: typing.List[str]) -> T:
        self.__require_client_cert_values = require_client_cert
        if 0 != len(self.__require_client_cert_values):
            self.__require_client_cert = ",".join(require_client_cert)
        else:
            self.__require_client_cert = None
        return self

    def add_require_client_cert(self: T, require_client_cert: str) -> T:
        self.__require_client_cert_values.append(require_client_cert)
        self.__require_client_cert = ",".join(self.__require_client_cert_values)

        return self

    def remove_require_client_cert(self: T, require_client_cert: str) -> T:
        if require_client_cert in self.__require_client_cert_values:
            self.__require_client_cert_values.remove(require_client_cert)
            if 0 != len(self.__require_client_cert_values):
                self.__require_client_cert = ",".join(self.__require_client_cert_values)
            else:
                self.__require_client_cert = None
        return self

    def get_require_client_cert(self) -> typing.List[str]:
        return self.__require_client_cert_values

    def set_security_level(self: T, security_level: int) -> T:
        self.__security_level = security_level
        return self

    def get_security_level(self: T) -> Union[int, None]:
        return self.__security_level

    def set_port(self: T, port: int) -> T:
        self.__port = port
        return self

    def get_port(self: T) -> Union[int, None]:
        return self.__port

    def set_ocsp_critical(self: T, ocsp_critical: int) -> T:
        self.__ocsp_critical = ocsp_critical
        return self

    def get_ocsp_critical(self: T) -> Union[int, None]:
        return self.__ocsp_critical

    def set_ocsp_warning(self: T, ocsp_warning: int) -> T:
        self.__ocsp_warning = ocsp_warning
        return self

    def get_ocsp_warning(self: T) -> Union[int, None]:
        return self.__ocsp_warning

    def set_critical(self: T, critical: int) -> T:
        self.__critical = critical
        return self

    def get_critical(self: T) -> Union[int, None]:
        return self.__critical

    def set_warning(self: T, warning: int) -> T:
        self.__warning = warning
        return self

    def get_warning(self: T) -> Union[int, None]:
        return self.__warning

    def set_element(self: T, element: int) -> T:
        self.__element = element
        return self

    def get_element(self: T) -> Union[int, None]:
        return self.__element

    def set_verbose(self: T, verbose: bool) -> T:
        self.__verbose = verbose
        return self

    def get_verbose(self: T) -> bool:
        return self.__verbose

    def set_terse(self: T, terse: bool) -> T:
        self.__terse = terse
        return self

    def get_terse(self: T) -> bool:
        return self.__terse

    def set_tls1(self: T, tls1: bool) -> T:
        self.__tls1 = tls1
        return self

    def get_tls1(self: T) -> bool:
        return self.__tls1

    def set_tls1_1(self: T, tls1_1: bool) -> T:
        self.__tls1_1 = tls1_1
        return self

    def get_tls1_1(self: T) -> bool:
        return self.__tls1_1

    def set_tls1_2(self: T, tls1_2: bool) -> T:
        self.__tls1_2 = tls1_2
        return self

    def get_tls1_2(self: T) -> bool:
        return self.__tls1_2

    def set_tls1_3(self: T, tls1_3: bool) -> T:
        self.__tls1_3 = tls1_3
        return self

    def get_tls1_3(self: T) -> bool:
        return self.__tls1_3

    def set_ssl2(self: T, ssl2: bool) -> T:
        self.__ssl2 = ssl2
        return self

    def get_ssl2(self: T) -> bool:
        return self.__ssl2

    def set_ssl3(self: T, ssl3: bool) -> T:
        self.__ssl3 = ssl3
        return self

    def get_ssl3(self: T) -> bool:
        return self.__ssl3

    def set_selfsigned(self: T, selfsigned: bool) -> T:
        self.__selfsigned = selfsigned
        return self

    def get_selfsigned(self: T) -> bool:
        return self.__selfsigned

    def set_rsa(self: T, rsa: bool) -> T:
        self.__rsa = rsa
        return self

    def get_rsa(self: T) -> bool:
        return self.__rsa

    def set_require_purpose_critical(self: T, require_purpose_critical: bool) -> T:
        self.__require_purpose_critical = require_purpose_critical
        return self

    def get_require_purpose_critical(self: T) -> bool:
        return self.__require_purpose_critical

    def set_require_no_ssl2(self: T, require_no_ssl2: bool) -> T:
        self.__require_no_ssl2 = require_no_ssl2
        return self

    def get_require_no_ssl2(self: T) -> bool:
        return self.__require_no_ssl2

    def set_require_no_ssl3(self: T, require_no_ssl3: bool) -> T:
        self.__require_no_ssl3 = require_no_ssl3
        return self

    def get_require_no_ssl3(self: T) -> bool:
        return self.__require_no_ssl3

    def set_require_no_tls1(self: T, require_no_tls1: bool) -> T:
        self.__require_no_tls1 = require_no_tls1
        return self

    def get_require_no_tls1(self: T) -> bool:
        return self.__require_no_tls1

    def set_require_no_tls1_1(self: T, require_no_tls1_1: bool) -> T:
        self.__require_no_tls1_1 = require_no_tls1_1
        return self

    def get_require_no_tls1_1(self: T) -> bool:
        return self.__require_no_tls1_1

    def set_require_ocsp_stapling(self: T, require_ocsp_stapling: bool) -> T:
        self.__require_ocsp_stapling = require_ocsp_stapling
        return self

    def get_require_ocsp_stapling(self: T) -> bool:
        return self.__require_ocsp_stapling

    def set_no_perf(self: T, no_perf: bool) -> T:
        self.__no_perf = no_perf
        return self

    def get_no_perf(self: T) -> bool:
        return self.__no_perf

    def set_no_proxy(self: T, no_proxy: bool) -> T:
        self.__no_proxy = no_proxy
        return self

    def get_no_proxy(self: T) -> bool:
        return self.__no_proxy

    def set_no_proxy_curl(self: T, no_proxy_curl: bool) -> T:
        self.__no_proxy_curl = no_proxy_curl
        return self

    def get_no_proxy_curl(self: T) -> bool:
        return self.__no_proxy_curl

    def set_no_proxy_s_client(self: T, no_proxy_s_client: bool) -> T:
        self.__no_proxy_s_client = no_proxy_s_client
        return self

    def get_no_proxy_s_client(self: T) -> bool:
        return self.__no_proxy_s_client

    def set_no_ssl2(self: T, no_ssl2: bool) -> T:
        self.__no_ssl2 = no_ssl2
        return self

    def get_no_ssl2(self: T) -> bool:
        return self.__no_ssl2

    def set_no_ssl3(self: T, no_ssl3: bool) -> T:
        self.__no_ssl3 = no_ssl3
        return self

    def get_no_ssl3(self: T) -> bool:
        return self.__no_ssl3

    def set_no_tls1(self: T, no_tls1: bool) -> T:
        self.__no_tls1 = no_tls1
        return self

    def get_no_tls1(self: T) -> bool:
        return self.__no_tls1

    def set_no_tls1_1(self: T, no_tls1_1: bool) -> T:
        self.__no_tls1_1 = no_tls1_1
        return self

    def get_no_tls1_1(self: T) -> bool:
        return self.__no_tls1_1

    def set_no_tls1_2(self: T, no_tls1_2: bool) -> T:
        self.__no_tls1_2 = no_tls1_2
        return self

    def get_no_tls1_2(self: T) -> bool:
        return self.__no_tls1_2

    def set_no_tls1_3(self: T, no_tls1_3: bool) -> T:
        self.__no_tls1_3 = no_tls1_3
        return self

    def get_no_tls1_3(self: T) -> bool:
        return self.__no_tls1_3

    def set_info(self: T, info: bool) -> T:
        self.__info = info
        return self

    def get_info(self: T) -> bool:
        return self.__info

    def set_init_host_cache(self: T, init_host_cache: bool) -> T:
        self.__init_host_cache = init_host_cache
        return self

    def get_init_host_cache(self: T) -> bool:
        return self.__init_host_cache

    def set_ignore_altnames(self: T, ignore_altnames: bool) -> T:
        self.__ignore_altnames = ignore_altnames
        return self

    def get_ignore_altnames(self: T) -> bool:
        return self.__ignore_altnames

    def set_ignore_connection_problems(self: T, ignore_connection_problems: bool) -> T:
        self.__ignore_connection_problems = ignore_connection_problems
        return self

    def get_ignore_connection_problems(self: T) -> bool:
        return self.__ignore_connection_problems

    def set_ignore_exp(self: T, ignore_exp: bool) -> T:
        self.__ignore_exp = ignore_exp
        return self

    def get_ignore_exp(self: T) -> bool:
        return self.__ignore_exp

    def set_ignore_http_headers(self: T, ignore_http_headers: bool) -> T:
        self.__ignore_http_headers = ignore_http_headers
        return self

    def get_ignore_http_headers(self: T) -> bool:
        return self.__ignore_http_headers

    def set_ignore_incomplete_chain(self: T, ignore_incomplete_chain: bool) -> T:
        self.__ignore_incomplete_chain = ignore_incomplete_chain
        return self

    def get_ignore_incomplete_chain(self: T) -> bool:
        return self.__ignore_incomplete_chain

    def set_ignore_host_cn(self: T, ignore_host_cn: bool) -> T:
        self.__ignore_host_cn = ignore_host_cn
        return self

    def get_ignore_host_cn(self: T) -> bool:
        return self.__ignore_host_cn

    def set_ignore_maximum_validity(self: T, ignore_maximum_validity: bool) -> T:
        self.__ignore_maximum_validity = ignore_maximum_validity
        return self

    def get_ignore_maximum_validity(self: T) -> bool:
        return self.__ignore_maximum_validity

    def set_ignore_ocsp(self: T, ignore_ocsp: bool) -> T:
        self.__ignore_ocsp = ignore_ocsp
        return self

    def get_ignore_ocsp(self: T) -> bool:
        return self.__ignore_ocsp

    def set_ignore_ocsp_errors(self: T, ignore_ocsp_errors: bool) -> T:
        self.__ignore_ocsp_errors = ignore_ocsp_errors
        return self

    def get_ignore_ocsp_errors(self: T) -> bool:
        return self.__ignore_ocsp_errors

    def set_ignore_ocsp_timeout(self: T, ignore_ocsp_timeout: bool) -> T:
        self.__ignore_ocsp_timeout = ignore_ocsp_timeout
        return self

    def get_ignore_ocsp_timeout(self: T) -> bool:
        return self.__ignore_ocsp_timeout

    def set_ignore_sct(self: T, ignore_sct: bool) -> T:
        self.__ignore_sct = ignore_sct
        return self

    def get_ignore_sct(self: T) -> bool:
        return self.__ignore_sct

    def set_ignore_sig_alg(self: T, ignore_sig_alg: bool) -> T:
        self.__ignore_sig_alg = ignore_sig_alg
        return self

    def get_ignore_sig_alg(self: T) -> bool:
        return self.__ignore_sig_alg

    def set_ignore_ssl_labs_cache(self: T, ignore_ssl_labs_cache: bool) -> T:
        self.__ignore_ssl_labs_cache = ignore_ssl_labs_cache
        return self

    def get_ignore_ssl_labs_cache(self: T) -> bool:
        return self.__ignore_ssl_labs_cache

    def set_ignore_ssl_labs_errors(self: T, ignore_ssl_labs_errors: bool) -> T:
        self.__ignore_ssl_labs_errors = ignore_ssl_labs_errors
        return self

    def get_ignore_ssl_labs_errors(self: T) -> bool:
        return self.__ignore_ssl_labs_errors

    def set_ignore_tls_renegotiation(self: T, ignore_tls_renegotiation: bool) -> T:
        self.__ignore_tls_renegotiation = ignore_tls_renegotiation
        return self

    def get_ignore_tls_renegotiation(self: T) -> bool:
        return self.__ignore_tls_renegotiation

    def set_http_use_get(self: T, http_use_get: bool) -> T:
        self.__http_use_get = http_use_get
        return self

    def get_http_use_get(self: T) -> bool:
        return self.__http_use_get

    def set_first_element_only(self: T, first_element_only: bool) -> T:
        self.__first_element_only = first_element_only
        return self

    def get_first_element_only(self: T) -> bool:
        return self.__first_element_only

    def set_force_dconv_date(self: T, force_dconv_date: bool) -> T:
        self.__force_dconv_date = force_dconv_date
        return self

    def get_force_dconv_date(self: T) -> bool:
        return self.__force_dconv_date

    def set_force_perl_date(self: T, force_perl_date: bool) -> T:
        self.__force_perl_date = force_perl_date
        return self

    def get_force_perl_date(self: T) -> bool:
        return self.__force_perl_date

    def set_ecdsa(self: T, ecdsa: bool) -> T:
        self.__ecdsa = ecdsa
        return self

    def get_ecdsa(self: T) -> bool:
        return self.__ecdsa

    def set_dtls(self: T, dtls: bool) -> T:
        self.__dtls = dtls
        return self

    def get_dtls(self: T) -> bool:
        return self.__dtls

    def set_dtls1(self: T, dtls1: bool) -> T:
        self.__dtls1 = dtls1
        return self

    def get_dtls1(self: T) -> bool:
        return self.__dtls1

    def set_dtls1_2(self: T, dtls1_2: bool) -> T:
        self.__dtls1_2 = dtls1_2
        return self

    def get_dtls1_2(self: T) -> bool:
        return self.__dtls1_2

    def set_debug(self: T, debug: bool) -> T:
        self.__debug = debug
        return self

    def get_debug(self: T) -> bool:
        return self.__debug

    def set_debug_cert(self: T, debug_cert: bool) -> T:
        self.__debug_cert = debug_cert
        return self

    def get_debug_cert(self: T) -> bool:
        return self.__debug_cert

    def set_debug_headers(self: T, debug_headers: bool) -> T:
        self.__debug_headers = debug_headers
        return self

    def get_debug_headers(self: T) -> bool:
        return self.__debug_headers

    def set_debug_time(self: T, debug_time: bool) -> T:
        self.__debug_time = debug_time
        return self

    def get_debug_time(self: T) -> bool:
        return self.__debug_time

    def set_default_format(self: T, default_format: bool) -> T:
        self.__default_format = default_format
        return self

    def get_default_format(self: T) -> bool:
        return self.__default_format

    def set_crl(self: T, crl: bool) -> T:
        self.__crl = crl
        return self

    def get_crl(self: T) -> bool:
        return self.__crl

    def set_check_ciphers_warnings(self: T, check_ciphers_warnings: bool) -> T:
        self.__check_ciphers_warnings = check_ciphers_warnings
        return self

    def get_check_ciphers_warnings(self: T) -> bool:
        return self.__check_ciphers_warnings

    def set_check_http_headers(self: T, check_http_headers: bool) -> T:
        self.__check_http_headers = check_http_headers
        return self

    def get_check_http_headers(self: T) -> bool:
        return self.__check_http_headers

    def set_check_chain(self: T, check_chain: bool) -> T:
        self.__check_chain = check_chain
        return self

    def get_check_chain(self: T) -> bool:
        return self.__check_chain

    def set_noauth(self: T, noauth: bool) -> T:
        self.__noauth = noauth
        return self

    def get_noauth(self: T) -> bool:
        return self.__noauth

    def set_all(self: T, all: bool) -> T:
        self.__all = all
        return self

    def get_all(self: T) -> bool:
        return self.__all

    def set_all_local(self: T, all_local: bool) -> T:
        self.__all_local = all_local
        return self

    def get_all_local(self: T) -> bool:
        return self.__all_local

    def set_allow_empty_scan(self: T, allow_empty_scan: bool) -> T:
        self.__allow_empty_scan = allow_empty_scan
        return self

    def get_allow_empty_scan(self: T) -> bool:
        return self.__allow_empty_scan

    def set_ipv4(self: T, ipv4: bool) -> T:
        self.__ipv4 = ipv4
        return self

    def get_ipv4(self: T) -> bool:
        return self.__ipv4

    def set_ipv6(self: T, ipv6: bool) -> T:
        self.__ipv6 = ipv6
        return self

    def get_ipv6(self: T) -> bool:
        return self.__ipv6

    ###############################
    ###############################
    ###############################
    ###############################
    ###############################
    #######  STRING VALUES  #######
    ###############################
    ###############################
    ###############################
    ###############################
    ###############################

    def set_file(self: T, file) -> T:
        self.__file = file
        return self

    def get_file(self: T) -> Union[str, None]:
        return self.__file

    def set_host(self: T, host) -> T:
        self.__host = host
        return self

    def get_host(self: T) -> Union[str, None]:
        return self.__host

    def set_clientcert(self: T, clientcert) -> T:
        self.__clientcert = clientcert
        return self

    def get_clientcert(self: T) -> Union[str, None]:
        return self.__clientcert

    def set_check_ciphers(self: T, check_ciphers) -> T:
        self.__check_ciphers = check_ciphers
        return self

    def get_check_ciphers(self: T) -> Union[str, None]:
        return self.__check_ciphers

    def set_check_ssl_labs_warn(self: T, check_ssl_labs_warn) -> T:
        self.__check_ssl_labs_warn = check_ssl_labs_warn
        return self

    def get_check_ssl_labs_warn(self: T) -> Union[str, None]:
        return self.__check_ssl_labs_warn

    def set_clientpass(self: T, clientpass) -> T:
        self.__clientpass = clientpass
        return self

    def get_clientpass(self: T) -> Union[str, None]:
        return self.__clientpass

    def set_configuration(self: T, configuration) -> T:
        self.__configuration = configuration
        return self

    def get_configuration(self: T) -> Union[str, None]:
        return self.__configuration

    def set_custom_http_header(self: T, custom_http_header) -> T:
        self.__custom_http_header = custom_http_header
        return self

    def get_custom_http_header(self: T) -> Union[str, None]:
        return self.__custom_http_header

    def set_curl_bin(self: T, curl_bin) -> T:
        self.__curl_bin = curl_bin
        return self

    def get_curl_bin(self: T) -> Union[str, None]:
        return self.__curl_bin

    def set_date(self: T, date) -> T:
        self.__date = date
        return self

    def get_date(self: T) -> Union[str, None]:
        return self.__date

    def set_debug_file(self: T, debug_file) -> T:
        self.__debug_file = debug_file
        return self

    def get_debug_file(self: T) -> Union[str, None]:
        return self.__debug_file

    def set_dig_bin(self: T, dig_bin) -> T:
        self.__dig_bin = dig_bin
        return self

    def get_dig_bin(self: T) -> Union[str, None]:
        return self.__dig_bin

    def set_email(self: T, email) -> T:
        self.__email = email
        return self

    def get_email(self: T) -> Union[str, None]:
        return self.__email

    def set_file_bin(self: T, file_bin) -> T:
        self.__file_bin = file_bin
        return self

    def get_file_bin(self: T) -> Union[str, None]:
        return self.__file_bin

    def set_fingerprint(self: T, fingerprint) -> T:
        self.__fingerprint = fingerprint
        return self

    def get_fingerprint(self: T) -> Union[str, None]:
        return self.__fingerprint

    def set_grep_bin(self: T, grep_bin) -> T:
        self.__grep_bin = grep_bin
        return self

    def get_grep_bin(self: T) -> Union[str, None]:
        return self.__grep_bin

    def set_format(self: T, format) -> T:
        self.__format = format
        return self

    def get_format(self: T) -> Union[str, None]:
        return self.__format

    def set_http_headers_path(self: T, http_headers_path) -> T:
        self.__http_headers_path = http_headers_path
        return self

    def get_http_headers_path(self: T) -> Union[str, None]:
        return self.__http_headers_path

    def set_issuer(self: T, issuer) -> T:
        self.__issuer = issuer
        return self

    def get_issuer(self: T) -> Union[str, None]:
        return self.__issuer

    def set_inetproto(self: T, inetproto) -> T:
        self.__inetproto = inetproto
        return self

    def get_inetproto(self: T) -> Union[str, None]:
        return self.__inetproto

    def set_issuer_cert_cache(self: T, issuer_cert_cache) -> T:
        self.__issuer_cert_cache = issuer_cert_cache
        return self

    def get_issuer_cert_cache(self: T) -> Union[str, None]:
        return self.__issuer_cert_cache

    def set_jks_alias(self: T, jks_alias) -> T:
        self.__jks_alias = jks_alias
        return self

    def get_jks_alias(self: T) -> Union[str, None]:
        return self.__jks_alias

    def set_clientkey(self: T, clientkey) -> T:
        self.__clientkey = clientkey
        return self

    def get_clientkey(self: T) -> Union[str, None]:
        return self.__clientkey

    def set_check_ssl_labs(self: T, check_ssl_labs) -> T:
        self.__check_ssl_labs = check_ssl_labs
        return self

    def get_check_ssl_labs(self: T) -> Union[str, None]:
        return self.__check_ssl_labs

    def set_maximum_validity(self: T, maximum_validity) -> T:
        self.__maximum_validity = maximum_validity
        return self

    def get_maximum_validity(self: T) -> Union[str, None]:
        return self.__maximum_validity

    def set_nmap_bin(self: T, nmap_bin) -> T:
        self.__nmap_bin = nmap_bin
        return self

    def get_nmap_bin(self: T) -> Union[str, None]:
        return self.__nmap_bin

    def set_not_issued_by(self: T, not_issued_by) -> T:
        self.__not_issued_by = not_issued_by
        return self

    def get_not_issued_by(self: T) -> Union[str, None]:
        return self.__not_issued_by

    def set_not_valid_longer_than(self: T, not_valid_longer_than) -> T:
        self.__not_valid_longer_than = not_valid_longer_than
        return self

    def get_not_valid_longer_than(self: T) -> Union[str, None]:
        return self.__not_valid_longer_than

    def set_org(self: T, org) -> T:
        self.__org = org
        return self

    def get_org(self: T) -> Union[str, None]:
        return self.__org

    def set_openssl(self: T, openssl) -> T:
        self.__openssl = openssl
        return self

    def get_openssl(self: T) -> Union[str, None]:
        return self.__openssl

    def set_path(self: T, path) -> T:
        self.__path = path
        return self

    def get_path(self: T) -> Union[str, None]:
        return self.__path

    def set_precision(self: T, precision) -> T:
        self.__precision = precision
        return self

    def get_precision(self: T) -> Union[str, None]:
        return self.__precision

    def set_protocol(self: T, protocol) -> T:
        self.__protocol = protocol
        return self

    def get_protocol(self: T) -> Union[str, None]:
        return self.__protocol

    def set_password(self: T, password) -> T:
        self.__password = password
        return self

    def get_password(self: T) -> Union[str, None]:
        return self.__password

    def set_proxy(self: T, proxy) -> T:
        self.__proxy = proxy
        return self

    def get_proxy(self: T) -> Union[str, None]:
        return self.__proxy

    def set_python_bin(self: T, python_bin) -> T:
        self.__python_bin = python_bin
        return self

    def get_python_bin(self: T) -> Union[str, None]:
        return self.__python_bin

    def set_rootcert(self: T, rootcert) -> T:
        self.__rootcert = rootcert
        return self

    def get_rootcert(self: T) -> Union[str, None]:
        return self.__rootcert

    def set_require_dnssec(self: T, require_dnssec) -> T:
        self.__require_dnssec = require_dnssec
        return self

    def get_require_dnssec(self: T) -> Union[str, None]:
        return self.__require_dnssec

    def set_require_http_header(self: T, require_http_header) -> T:
        self.__require_http_header = require_http_header
        return self

    def get_require_http_header(self: T) -> Union[str, None]:
        return self.__require_http_header

    def set_require_no_http_header(self: T, require_no_http_header) -> T:
        self.__require_no_http_header = require_no_http_header
        return self

    def get_require_no_http_header(self: T) -> Union[str, None]:
        return self.__require_no_http_header

    def set_resolve(self: T, resolve) -> T:
        self.__resolve = resolve
        return self

    def get_resolve(self: T) -> Union[str, None]:
        return self.__resolve

    def set_rootcert_dir(self: T, rootcert_dir) -> T:
        self.__rootcert_dir = rootcert_dir
        return self

    def get_rootcert_dir(self: T) -> Union[str, None]:
        return self.__rootcert_dir

    def set_rootcert_file(self: T, rootcert_file) -> T:
        self.__rootcert_file = rootcert_file
        return self

    def get_rootcert_file(self: T) -> Union[str, None]:
        return self.__rootcert_file

    def set_serial(self: T, serial) -> T:
        self.__serial = serial
        return self

    def get_serial(self: T) -> Union[str, None]:
        return self.__serial

    def set_sni(self: T, sni) -> T:
        self.__sni = sni
        return self

    def get_sni(self: T) -> Union[str, None]:
        return self.__sni

    def set_timeout(self: T, timeout) -> T:
        self.__timeout = timeout
        return self

    def get_timeout(self: T) -> Union[str, None]:
        return self.__timeout

    def set_temp(self: T, temp) -> T:
        self.__temp = temp
        return self

    def get_temp(self: T) -> Union[str, None]:
        return self.__temp

    def set_url(self: T, url) -> T:
        self.__url = url
        return self

    def get_url(self: T) -> Union[str, None]:
        return self.__url

    def set_xmpphost(self: T, xmpphost) -> T:
        self.__xmpphost = xmpphost
        return self

    def get_xmpphost(self: T) -> Union[str, None]:
        return self.__xmpphost

    def set_user_agent(self: T, user_agent) -> T:
        self.__user_agent = user_agent
        return self

    def get_user_agent(self: T) -> Union[str, None]:
        return self.__user_agent

    def validate(self):

        if None is self.__host and None is self.__file:
            raise Exception("You need to set host or file")

        elif None is not self.__host and None is not self.__file:
            raise Exception("You need to set host or file but you set both")

    @staticmethod
    def create(id: str, force_create: bool = False) -> CheckSSLCert:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckSSLCert(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckSSLCert):
            raise Exception('Id must be for an instance of CheckSSLCert but other instance is returned')

        if None is ConfigBuilder.get_command('matteocorti_ssl_cert'):
            CheckSSLCertCommand.create('matteocorti_ssl_cert')

        return check
