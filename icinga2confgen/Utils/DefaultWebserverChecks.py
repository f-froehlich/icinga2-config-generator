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
from icinga2confgen.Checks.MonitoringPlugins.CheckDenyTlsVersion import CheckDenyTlsVersion
from icinga2confgen.Checks.NagiosPlugins.CheckDummy import CheckDummy
from icinga2confgen.Checks.NagiosPlugins.CheckHttp import CheckHttp
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.HostGroup import HostGroup
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.Helpers.RemoteCheckManager import RemoteCheckManager
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class DefaultWebserverChecks(RemoteCheckManager):

    def __init__(self, vhostconfig=[], servers=[], checkserver=[], notifications=[]):
        RemoteCheckManager.__init__(self, servers=servers, checkserver=checkserver, notifications=notifications)
        self.__vhostconfigs = vhostconfig
        self.__validate_certificate = True
        self.__validate_http_redirect = True
        self.__warn_no_http_redirect = True
        self.__validate_allow_tls1 = False
        self.__validate_deny_tls1 = True
        self.__validate_allow_tls1_1 = False
        self.__validate_deny_tls1_1 = True
        self.__validate_allow_tls1_2 = True
        self.__validate_deny_tls1_2 = False
        self.__validate_allow_tls1_3 = True
        self.__validate_deny_tls1_3 = False
        self.__sni = True

    def get_vhostconfigs(self):
        return self.__vhostconfigs

    def validate_certificate(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_certificate = enabled

        return self

    def is_validating_certificate(self):
        return self.__validate_certificate

    def validate_http_redirect(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_http_redirect = enabled

        return self

    def is_validating_http_redirect(self):
        return self.__validate_http_redirect

    def warn_no_http_redirect(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__warn_no_http_redirect = enabled

        return self

    def is_warn_no_http_redirect(self):
        return self.__warn_no_http_redirect

    def validate_allow_tls1(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_allow_tls1 = enabled

        return self

    def is_validating_allow_tls1(self):
        return self.__validate_allow_tls1

    def validate_deny_tls1(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_deny_tls1 = enabled

        return self

    def is_validating_deny_tls1(self):
        ValueChecker.is_bool(enabled)
        return self.__validate_deny_tls1

    def validate_allow_tls1_1(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_allow_tls1_1 = enabled

        return self

    def is_validating_allow_tls1_1(self):
        return self.__validate_allow_tls1_1

    def validate_deny_tls1_1(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_deny_tls1_1 = enabled

        return self

    def is_validating_deny_tls1_1(self):
        return self.__validate_deny_tls1_1

    def validate_allow_tls1_2(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_allow_tls1_2 = enabled

        return self

    def is_validating_allow_tls1_2(self):
        return self.__validate_allow_tls1_2

    def validate_deny_tls1_2(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_deny_tls1_2 = enabled

        return self

    def is_validating_deny_tls1_2(self):
        return self.__validate_deny_tls1_2

    def validate_allow_tls1_3(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_allow_tls1_3 = enabled

        return self

    def is_validating_allow_tls1_3(self):
        return self.__validate_allow_tls1_3

    def validate_deny_tls1_3(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_deny_tls1_3 = enabled

        return self

    def is_validating_deny_tls1_3(self):
        return self.__validate_deny_tls1_3

    def set_sni(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__sni = enabled

        return self

    def get_sni(self):
        return self.__sni

    def get_default_access_check(self, service_baseid, server, domain):
        base_id = service_baseid + '_' + server.get_id() + '_' + ValueMapper.canonicalize_for_id(domain)
        return {
            'ipv4': ConfigBuilder.get_check('web_access_default_ipv4_' + base_id),
            'ipv6': ConfigBuilder.get_check('web_access_default_ipv6_' + base_id)
        }

    def apply(self):
        for config in self.__vhostconfigs:
            service_baseid = config[0]
            domain = config[1]
            uri = config[2]

            for server in self.get_servers():
                base_id = service_baseid + '_' + server.get_id() + '_' + ValueMapper.canonicalize_for_id(domain)
                server_ipv4 = server.get_ipv4()
                server_ipv6 = server.get_ipv6()

                if None is server_ipv4 and None is server_ipv6:
                    raise Exception('It is required to set the ipv4 or ipv6 on the server with id "' +
                                    server.get_id() + '", before you can apply this checks!')

                server.add_hostgroup(HostGroup.create('webserver'))

                default_ipv4_http_check = None
                default_ipv6_http_check = None
                if None is not server_ipv4:
                    default_ipv4_http_check = CheckHttp.create('web_access_default_ipv4_' + base_id)
                    default_ipv4_http_check.set_ip(server_ipv4) \
                        .set_vhost(domain) \
                        .set_uri(uri) \
                        .set_ssl(True) \
                        .set_sni(self.__sni) \
                        .set_display_name(default_ipv4_http_check.get_display_name() + ' ' + domain)
                    self.apply_check(default_ipv4_http_check)

                if None is not server_ipv6:
                    default_ipv6_http_check = CheckHttp.create('web_access_default_ipv6_' + base_id)
                    default_ipv6_http_check.set_ip(server_ipv6) \
                        .set_ipv6(True) \
                        .set_vhost(domain) \
                        .set_uri(uri) \
                        .set_ssl(True) \
                        .set_sni(self.__sni) \
                        .set_display_name(default_ipv6_http_check.get_display_name() + ' ' + domain)
                    self.apply_check(default_ipv6_http_check)

                if None == default_ipv4_http_check and None == default_ipv6_http_check:
                    raise Exception('Server "' + server.get_id()
                                    + '" has no IPv4 and no IPv6 address set. Can\'t go further right now.')

                if True is self.__validate_certificate:
                    if None is not server_ipv4:
                        certificate_check = CheckHttp.create('web_access_certificate_ipv4_' + base_id)
                        certificate_check.set_ip(server_ipv4) \
                            .set_vhost(domain) \
                            .set_uri(uri) \
                            .set_ssl(True) \
                            .set_sni(self.__sni) \
                            .set_certificate_check(True) \
                            .set_check_interval('15m') \
                            .add_service_group(ServiceGroup.create('certificate_check')) \
                            .set_display_name(certificate_check.get_display_name() + ' ' + domain)

                        self.apply_check(certificate_check, default_ipv4_http_check)

                    if None is not server_ipv6:
                        certificate_check = CheckHttp.create('web_access_certificate_ipv6_' + base_id)
                        certificate_check.set_ip(server_ipv6) \
                            .set_ipv6(True) \
                            .set_vhost(domain) \
                            .set_uri(uri) \
                            .set_ssl(True) \
                            .set_sni(self.__sni) \
                            .set_certificate_check(True) \
                            .set_check_interval('15m') \
                            .add_service_group(ServiceGroup.create('certificate_check')) \
                            .set_display_name(certificate_check.get_display_name() + ' ' + domain)

                        self.apply_check(certificate_check, default_ipv6_http_check)

                else:
                    server.add_hostgroup(HostGroup.create('no_certificate_check'))

                if True is self.__validate_http_redirect:
                    if None is not server_ipv4:
                        redirect_check = CheckHttp.create('web_access_http_redirect_ipv4_' + base_id)
                        redirect_check.set_ip(server_ipv4) \
                            .set_vhost(domain) \
                            .set_uri(uri) \
                            .set_ssl(False) \
                            .set_sni(self.__sni) \
                            .set_port(80) \
                            .set_expect('HTTP/1.1 30') \
                            .set_check_interval('15m') \
                            .add_service_group(ServiceGroup.create('http_redirect')) \
                            .set_display_name(redirect_check.get_display_name() + ' ' + domain)

                        self.apply_check(redirect_check, default_ipv4_http_check)

                    if None is not server_ipv6:
                        redirect_check = CheckHttp.create('web_access_http_redirect_ipv6_' + base_id)
                        redirect_check.set_ip(server_ipv6) \
                            .set_ipv6(True) \
                            .set_vhost(domain) \
                            .set_uri(uri) \
                            .set_ssl(False) \
                            .set_sni(self.__sni) \
                            .set_port(80) \
                            .set_expect('HTTP/1.1 30') \
                            .set_check_interval('15m') \
                            .add_service_group(ServiceGroup.create('http_redirect')) \
                            .set_display_name(redirect_check.get_display_name() + ' ' + domain)

                        self.apply_check(redirect_check, default_ipv6_http_check)

                    server.add_hostgroup(HostGroup.create('http_redirect'))

                elif True is self.__warn_no_http_redirect:
                    redirect_check = CheckDummy.create('web_access_missing_http_redirect_' + base_id)
                    redirect_check.set_state(1) \
                        .set_text(redirect_check.get_display_name() + ' ' + domain) \
                        .set_check_interval('15m') \
                        .add_service_group(ServiceGroup.create('missing_http_redirect_check')) \
                        .add_service_group(ServiceGroup.create('webserver')) \
                        .set_display_name(redirect_check.get_display_name() + ' ' + domain)

                    self.apply_check(redirect_check)
                    server.add_hostgroup(HostGroup.create('no_http_redirect'))

                else:
                    server.add_hostgroup(HostGroup.create('http_redirect_unchecked'))

                self.add_tls_check(base_id, default_ipv4_http_check, default_ipv6_http_check, domain,
                                   server, server_ipv4, server_ipv6, uri, '1.0', self.__validate_allow_tls1,
                                   self.__validate_deny_tls1, True)

                self.add_tls_check(base_id, default_ipv4_http_check, default_ipv6_http_check, domain,
                                   server, server_ipv4, server_ipv6, uri, '1.1', self.__validate_allow_tls1_1,
                                   self.__validate_deny_tls1_1, True)

                self.add_tls_check(base_id, default_ipv4_http_check, default_ipv6_http_check, domain,
                                   server, server_ipv4, server_ipv6, uri, '1.2', self.__validate_allow_tls1_2,
                                   self.__validate_deny_tls1_2, False)

                self.add_tls_check(base_id, default_ipv4_http_check, default_ipv6_http_check, domain,
                                   server, server_ipv4, server_ipv6, uri, '1.3', self.__validate_allow_tls1_3,
                                   self.__validate_deny_tls1_3, False)

    def add_tls_check(self, base_id, default_ipv4_http_check, default_ipv6_http_check, domain, server,
                      server_ipv4, server_ipv6, uri, protocol, allow, deny, insecure):
        protocol_id = protocol.replace('.', '_')

        if insecure:
            server.add_hostgroup(HostGroup.create('insecure_webserver'))
        else:
            server.add_hostgroup(HostGroup.create('secure_webserver'))

        if allow:
            if None is not server_ipv4:
                tls_check = CheckHttp.create('web_access_allow_tls' + protocol_id + '_ipv4_' + base_id)
                tls_check.set_ip(server_ipv4) \
                    .set_vhost(domain) \
                    .set_uri(uri) \
                    .set_sni(self.__sni) \
                    .set_ssl_protocol(protocol) \
                    .set_check_interval('15m') \
                    .add_service_group(ServiceGroup.create('tls_' + protocol_id + '_check')) \
                    .add_service_group(ServiceGroup.create('tls')) \
                    .set_display_name(tls_check.get_display_name() + ' ' + domain)

                self.apply_check(tls_check, default_ipv4_http_check)

            if None is not server_ipv6:
                tls_check = CheckHttp.create('web_access_allow_tls' + protocol_id + '_ipv6_' + base_id)
                tls_check.set_ip(server_ipv6) \
                    .set_vhost(domain) \
                    .set_uri(uri) \
                    .set_sni(self.__sni) \
                    .set_ssl_protocol(protocol) \
                    .set_check_interval('15m') \
                    .add_service_group(ServiceGroup.create('tls_' + protocol_id + '_check')) \
                    .add_service_group(ServiceGroup.create('tls')) \
                    .set_display_name(tls_check.get_display_name() + ' ' + domain)

                self.apply_check(tls_check, default_ipv6_http_check)

            if insecure:
                server.add_hostgroup(HostGroup.create('insecure_webserver'))
                server.add_hostgroup(HostGroup.create('insecure_TLSv' + protocol_id + '_Webserver'))
            else:
                server.add_hostgroup(HostGroup.create('secure_webserver'))
                server.add_hostgroup(HostGroup.create('secure_TLSv' + protocol_id + '_Webserver'))

        elif deny:
            if None is not server_ipv4:
                tls_check = CheckDenyTlsVersion.create('web_access_deny_tls' + protocol_id + '_ipv4_' + base_id)
                tls_check.set_address(server_ipv4) \
                    .set_domain(domain) \
                    .set_protocol(protocol) \
                    .set_check_interval('15m') \
                    .add_service_group(ServiceGroup.create('tls_' + protocol_id + '_check')) \
                    .set_display_name(tls_check.get_display_name() + ' ' + domain)

                self.apply_check(tls_check, default_ipv4_http_check)

            if None is not server_ipv6:
                tls_check = CheckDenyTlsVersion.create('web_access_deny_tls' + protocol_id + '_ipv6_' + base_id)
                tls_check.set_address(server_ipv6) \
                    .set_domain(domain) \
                    .set_protocol(protocol) \
                    .set_check_interval('15m') \
                    .add_service_group(ServiceGroup.create('tls_' + protocol_id + '_check')) \
                    .set_display_name(tls_check.get_display_name() + ' ' + domain)
                self.apply_check(tls_check, default_ipv6_http_check)

            server.add_hostgroup(HostGroup.create('deny_insecure_TLSv' + protocol_id + '_webserver'))

            if insecure:
                server.add_hostgroup(HostGroup.create('deny_insecure_TLSv' + protocol_id + '_Webserver'))
            else:
                server.add_hostgroup(HostGroup.create('deny_secure_TLSv' + protocol_id + '_Webserver'))
        else:
            server.add_hostgroup(HostGroup.create('deny_insecure_TLSv' + protocol_id + '_unchecked'))
