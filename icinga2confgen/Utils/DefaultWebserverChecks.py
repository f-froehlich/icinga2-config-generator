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
from icinga2confgen.Checks.Icinga2Confgen.CheckDenyTlsVersion import CheckDenyTlsVersion
from icinga2confgen.Checks.MonitoringPlugins.CheckDummy import CheckDummy
from icinga2confgen.Checks.MonitoringPlugins.CheckHttp import CheckHttp
from icinga2confgen.Groups.HostGroup import HostGroup
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class DefaultWebserverChecks:

    def __init__(self, vhostconfig=[], servers=[], checkserver=[], notifications=[]):
        self.__checkserver = checkserver
        self.__notifications = notifications
        self.__servers = servers
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

    def get_servers(self):
        return self.__servers

    def get_checkservers(self):
        return self.__checkserver

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

    def apply_notification_to_check(self, check):
        for notification in self.__notifications:
            check.add_notification(notification)

    def apply(self):
        for config in self.__vhostconfigs:
            service_baseid = config[0]
            domain = config[1]
            uri = config[2]

            for checkserver in self.__checkserver:
                for server in self.__servers:
                    base_id = service_baseid + '_' + server.get_id() + '_' + ValueMapper.canonicalize_for_id(domain)
                    server_ipv4 = server.get_ipv4()
                    server_ipv6 = server.get_ipv6()

                    if None is server_ipv4 and None is server_ipv6:
                        raise Exception('It is required to set the ipv4 or ipv6 on the server with id "' +
                                        server.get_id() + '", before you can apply this checks!')

                    server.add_hostgroup(HostGroup.create('webserver'))

                    if None is not server_ipv4:
                        http_check = CheckHttp.create('web_access_default_ipv4_' + base_id)
                        http_check.set_ip(server_ipv4) \
                            .set_vhost(domain) \
                            .set_uri(uri) \
                            .set_ssl(True) \
                            .set_sni(self.__sni) \
                            .set_display_name(http_check.get_display_name() + ' ' + domain)
                        self.apply_notification_to_check(http_check)
                        checkserver.add_check(http_check)
                    if None is not server_ipv6:
                        http_check = CheckHttp.create('web_access_default_ipv6_' + base_id)
                        http_check.set_ip(server_ipv6) \
                            .set_vhost(domain) \
                            .set_uri(uri) \
                            .set_ssl(True) \
                            .set_sni(self.__sni) \
                            .set_display_name(http_check.get_display_name() + ' ' + domain)
                        self.apply_notification_to_check(http_check)
                        checkserver.add_check(http_check)

                    if True is self.__validate_certificate:
                        if None is not server_ipv4:
                            certificate_check = CheckHttp.create('web_access_certificate_ipv4_' + base_id)
                            certificate_check.set_ip(server_ipv4) \
                                .set_vhost(domain) \
                                .set_uri(uri) \
                                .set_ssl(True) \
                                .set_sni(self.__sni) \
                                .set_certificate_check(True) \
                                .set_check_interval('3h') \
                                .add_service_group(ServiceGroup.create('certificate_check')) \
                                .set_display_name(certificate_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(certificate_check)
                            checkserver.add_check(certificate_check)
                        if None is not server_ipv6:
                            certificate_check = CheckHttp.create('web_access_certificate_ipv6_' + base_id)
                            certificate_check.set_ip(server_ipv6) \
                                .set_vhost(domain) \
                                .set_uri(uri) \
                                .set_ssl(True) \
                                .set_sni(self.__sni) \
                                .set_certificate_check(True) \
                                .set_check_interval('3h') \
                                .add_service_group(ServiceGroup.create('certificate_check')) \
                                .set_display_name(certificate_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(certificate_check)

                            checkserver.add_check(certificate_check)
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
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('http_redirect')) \
                                .set_display_name(redirect_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(redirect_check)
                            checkserver.add_check(redirect_check)

                        if None is not server_ipv6:
                            redirect_check = CheckHttp.create('web_access_http_redirect_ipv6_' + base_id)
                            redirect_check.set_ip(server_ipv6) \
                                .set_vhost(domain) \
                                .set_uri(uri) \
                                .set_ssl(False) \
                                .set_sni(self.__sni) \
                                .set_port(80) \
                                .set_expect('HTTP/1.1 30') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('http_redirect')) \
                                .set_display_name(redirect_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(redirect_check)
                            checkserver.add_check(redirect_check)

                        server.add_hostgroup(HostGroup.create('http_redirect'))

                    elif True is self.__warn_no_http_redirect:
                        redirect_check = CheckDummy.create('web_access_missing_http_redirect_' + base_id)
                        redirect_check.set_state(1) \
                            .set_text(redirect_check.get_display_name() + ' ' + domain) \
                            .set_check_interval('6h') \
                            .add_service_group(ServiceGroup.create('missing_http_redirect_check')) \
                            .set_display_name(redirect_check.get_display_name() + ' ' + domain)

                        checkserver.add_check(redirect_check)
                        self.apply_notification_to_check(redirect_check)
                        server.add_hostgroup(HostGroup.create('no_http_redirect'))

                    else:
                        server.add_hostgroup(HostGroup.create('http_redirect_unchecked'))

                    if True is self.__validate_allow_tls1:
                        if None is not server_ipv4:
                            tls1_check = CheckHttp.create('web_access_allow_tls1_ipv4_' + base_id)
                            tls1_check.set_ip(server_ipv4) \
                                .set_vhost(domain) \
                                .set_uri(uri) \
                                .set_sni(self.__sni) \
                                .set_ssl_protocol('1.1') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_check')) \
                                .set_display_name(tls1_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(tls1_check)
                            checkserver.add_check(tls1_check)

                        if None is not server_ipv6:
                            tls1_check = CheckHttp.create('web_access_allow_tls1_ipv6_' + base_id)
                            tls1_check.set_ip(server_ipv6) \
                                .set_vhost(domain) \
                                .set_uri(uri) \
                                .set_sni(self.__sni) \
                                .set_ssl_protocol('1.1') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_check')) \
                                .set_display_name(tls1_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(tls1_check)
                            checkserver.add_check(tls1_check)

                        server.add_hostgroup(HostGroup.create('insecure_webserver'))
                        server.add_hostgroup(HostGroup.create('insecure_TLSv1_0_Webserver'))
                    elif True is self.__validate_deny_tls1:
                        if None is not server_ipv4:
                            tls1_check = CheckDenyTlsVersion.create('web_access_deny_tls1_ipv4_' + base_id)
                            tls1_check.set_address(server_ipv4) \
                                .set_domain(domain) \
                                .set_protocol('1.0') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_check')) \
                                .set_display_name(tls1_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(tls1_check)
                            checkserver.add_check(tls1_check)

                        if None is not server_ipv6:
                            tls1_check = CheckDenyTlsVersion.create('web_access_deny_tls1_ipv6_' + base_id)
                            tls1_check.set_address(server_ipv6) \
                                .set_domain(domain) \
                                .set_protocol('1.0') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_check')) \
                                .set_display_name(tls1_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(tls1_check)
                            checkserver.add_check(tls1_check)

                        server.add_hostgroup(HostGroup.create('deny_insecure_TLSv1_0_webserver'))
                    else:
                        server.add_hostgroup(HostGroup.create('deny_insecure_TLSv1_0_unchecked'))

                    if True is self.__validate_allow_tls1_1:
                        if None is not server_ipv4:
                            tls1_1_check = CheckHttp.create('web_access_allow_tls1_1_ipv4_' + base_id)
                            tls1_1_check.set_vhost(domain) \
                                .set_ip(server_ipv4) \
                                .set_uri(uri) \
                                .set_sni(self.__sni) \
                                .set_ssl_protocol('1.1') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_1_check')) \
                                .set_display_name(tls1_1_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(tls1_1_check)
                            checkserver.add_check(tls1_1_check)

                        if None is not server_ipv6:
                            tls1_1_check = CheckHttp.create('web_access_allow_tls1_1_ipv6_' + base_id)
                            tls1_1_check.set_vhost(domain) \
                                .set_ip(server_ipv6) \
                                .set_uri(uri) \
                                .set_sni(self.__sni) \
                                .set_ssl_protocol('1.1') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_1_check')) \
                                .set_display_name(tls1_1_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(tls1_1_check)
                            checkserver.add_check(tls1_1_check)

                        server.add_hostgroup(HostGroup.create('insecure_webserver'))
                        server.add_hostgroup(HostGroup.create('insecure_TLSv1_1_webserver'))

                    elif True is self.__validate_deny_tls1_1:
                        if None is not server_ipv4:
                            tls1_1_check = CheckDenyTlsVersion.create('web_access_deny_tls1_1_ipv4_' + base_id)
                            tls1_1_check.set_address(server_ipv4) \
                                .set_domain(domain) \
                                .set_protocol('1.1') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_1_check')) \
                                .set_display_name(tls1_1_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(tls1_1_check)
                            checkserver.add_check(tls1_1_check)

                        if None is not server_ipv6:
                            tls1_1_check = CheckDenyTlsVersion.create('web_access_deny_tls1_1_ipv6_' + base_id)
                            tls1_1_check.set_address(server_ipv6) \
                                .set_domain(domain) \
                                .set_protocol('1.1') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_1_check')) \
                                .set_display_name(tls1_1_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(tls1_1_check)
                            checkserver.add_check(tls1_1_check)

                        server.add_hostgroup(HostGroup.create('deny_insecure_TLSv1_1_Webserver'))
                    else:
                        server.add_hostgroup(HostGroup.create('deny_insecure_TLSv1_1_unchecked'))

                    if True is self.__validate_allow_tls1_2:
                        if None is not server_ipv4:
                            tls1_2_check = CheckHttp.create('web_access_allow_tls1_2_ipv4_' + base_id)
                            tls1_2_check.set_vhost(domain) \
                                .set_ip(server_ipv4) \
                                .set_uri(uri) \
                                .set_sni(self.__sni) \
                                .set_ssl_protocol('1.2') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_2_check')) \
                                .set_display_name(tls1_2_check.get_display_name() + ' ' + domain)

                            self.apply_notification_to_check(tls1_2_check)
                            checkserver.add_check(tls1_2_check)

                        if None is not server_ipv6:
                            tls1_2_check = CheckHttp.create('web_access_allow_tls1_2_ipv6_' + base_id)
                            tls1_2_check.set_vhost(domain) \
                                .set_ip(server_ipv6) \
                                .set_uri(uri) \
                                .set_sni(self.__sni) \
                                .set_ssl_protocol('1.2') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_2_check')) \
                                .set_display_name(tls1_2_check.get_display_name() + ' ' + domain)

                            self.apply_notification_to_check(tls1_2_check)
                            checkserver.add_check(tls1_2_check)

                        server.add_hostgroup(HostGroup.create('secure_webserver'))
                        server.add_hostgroup(HostGroup.create('secure_TLSv1_2_webserver'))

                    elif True is self.__validate_deny_tls1_2:
                        if None is not server_ipv4:
                            tls1_2_check = CheckDenyTlsVersion.create('web_access_deny_tls1_2_ipv4_' + base_id)
                            tls1_2_check.set_address(server_ipv4) \
                                .set_domain(domain) \
                                .set_protocol('1.2') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_2_check')) \
                                .set_display_name(tls1_2_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(tls1_2_check)
                            checkserver.add_check(tls1_2_check)

                        if None is not server_ipv6:
                            tls1_2_check = CheckDenyTlsVersion.create('web_access_deny_tls1_2_ipv6_' + base_id)
                            tls1_2_check.set_address(server_ipv6) \
                                .set_domain(domain) \
                                .set_protocol('1.2') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_2_check')) \
                                .set_display_name(tls1_2_check.get_display_name() + ' ' + domain)
                            self.apply_notification_to_check(tls1_2_check)
                            checkserver.add_check(tls1_2_check)

                        server.add_hostgroup(HostGroup.create('insecure_webserver'))
                        server.add_hostgroup(HostGroup.create('deny_secure_TLSv1_2_webserver'))


                    else:
                        server.add_hostgroup(HostGroup.create('secure_TLSv1_2_unchecked'))

                    if True is self.__validate_allow_tls1_3:
                        if None is not server_ipv4:
                            tls1_3_check = CheckHttp.create('web_access_allow_tls1_3_ipv4_' + base_id)
                            tls1_3_check.set_ip(server_ipv4) \
                                .set_vhost(domain) \
                                .set_uri(uri) \
                                .set_sni(self.__sni) \
                                .set_ssl_protocol('1.3') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_3_check')) \
                                .set_display_name(tls1_3_check.get_display_name() + ' ' + domain)

                            self.apply_notification_to_check(tls1_3_check)
                            checkserver.add_check(tls1_3_check)

                        if None is not server_ipv6:
                            tls1_3_check = CheckHttp.create('web_access_allow_tls1_3_ipv6_' + base_id)
                            tls1_3_check.set_ip(server_ipv6) \
                                .set_vhost(domain) \
                                .set_uri(uri) \
                                .set_sni(self.__sni) \
                                .set_ssl_protocol('1.3') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_3_check')) \
                                .set_display_name(tls1_3_check.get_display_name() + ' ' + domain)

                            self.apply_notification_to_check(tls1_3_check)
                            checkserver.add_check(tls1_3_check)

                        server.add_hostgroup(HostGroup.create('secure_webserver'))
                        server.add_hostgroup(HostGroup.create('secure_TLSv1_3_Webserver'))

                    elif True is self.__validate_deny_tls1_3:
                        if None is not server_ipv4:
                            tls1_3_check = CheckDenyTlsVersion.create('web_access_deny_tls1_2_ipv4_' + base_id)
                            tls1_3_check.set_address(server_ipv4) \
                                .set_domain(domain) \
                                .set_protocol('1.3') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_3_check')) \
                                .set_display_name(tls1_3_check.get_display_name() + ' ' + domain)

                            self.apply_notification_to_check(tls1_3_check)
                            checkserver.add_check(tls1_3_check)

                        if None is not server_ipv6:
                            tls1_3_check = CheckDenyTlsVersion.create('web_access_deny_tls1_2_ipv6_' + base_id)
                            tls1_3_check.set_address(server_ipv6) \
                                .set_domain(domain) \
                                .set_protocol('1.3') \
                                .set_check_interval('6h') \
                                .add_service_group(ServiceGroup.create('tls_1_3_check')) \
                                .set_display_name(tls1_3_check.get_display_name() + ' ' + domain)

                            self.apply_notification_to_check(tls1_3_check)
                            checkserver.add_check(tls1_3_check)

                        server.add_hostgroup(HostGroup.create('insecure_webserver'))
                        server.add_hostgroup(HostGroup.create('deny_secure_TLSv1_3_webserver'))
                    else:
                        server.add_hostgroup(HostGroup.create('secure_TLSv1_3_unchecked'))
