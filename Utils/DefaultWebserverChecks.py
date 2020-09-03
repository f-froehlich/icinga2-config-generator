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
from Checks.CheckDenyTlsVersion import CheckDenyTlsVersion
from Checks.CheckDummy import CheckDummy
from Checks.CheckHttp import CheckHttp
from Groups.HostGroup import HostGroup
from Groups.ServiceGroup import ServiceGroup


class DefaultWebserverChecks:

    def __init__(self, vhostconfig=[], servers=[], checkserver=[]):
        self.__checkserver = checkserver
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

    def validate_certificate(self, enabled):
        self.__validate_certificate = enabled

        return self

    def is_validating_certificate(self):
        return self.__validate_certificate

    def validate_http_redirect(self, enabled):
        self.__validate_http_redirect = enabled

        return self

    def is_validating_http_redirect(self):
        return self.__validate_http_redirect

    def warn_no_http_redirect(self, enabled):
        self.__warn_no_http_redirect = enabled

        return self

    def is_warn_no_http_redirect(self):
        return self.__warn_no_http_redirect

    def validate_allow_tls1(self, enabled):
        self.__validate_allow_tls1 = enabled

        return self

    def is_validating_allow_tls1(self):
        return self.__validate_allow_tls1

    def validate_deny_tls1(self, enabled):
        self.__validate_deny_tls1 = enabled

        return self

    def is_validating_deny_tls1(self):
        return self.__validate_deny_tls1

    def validate_allow_tls1_1(self, enabled):
        self.__validate_allow_tls1_1 = enabled

        return self

    def is_validating_allow_tls1_1(self):
        return self.__validate_allow_tls1_1

    def validate_deny_tls1_1(self, enabled):
        self.__validate_deny_tls1_1 = enabled

        return self

    def is_validating_deny_tls1_1(self):
        return self.__validate_deny_tls1_1

    def validate_allow_tls1_2(self, enabled):
        self.__validate_allow_tls1_2 = enabled

        return self

    def is_validating_allow_tls1_2(self):
        return self.__validate_allow_tls1_2

    def validate_deny_tls1_2(self, enabled):
        self.__validate_deny_tls1_2 = enabled

        return self

    def is_validating_deny_tls1_2(self):
        return self.__validate_deny_tls1_2

    def validate_allow_tls1_3(self, enabled):
        self.__validate_allow_tls1_3 = enabled

        return self

    def is_validating_allow_tls1_3(self):
        return self.__validate_allow_tls1_3

    def validate_deny_tls1_3(self, enabled):
        self.__validate_deny_tls1_3 = enabled

        return self

    def is_validating_deny_tls1_3(self):
        return self.__validate_deny_tls1_3

    def apply(self):
        for config in self.__vhostconfigs:
            domain = config[0]
            uri = config[1]

            for checkserver in self.__checkserver:
                for server in self.__servers:
                    base_id = ''.join(e for e in domain + server.get_id() if e.isalnum())
                    server_ip = server.get_ipv4()
                    if None is server_ip:
                        server_ip = server.get_ipv6()

                    server.add_hostgroup(HostGroup.create('webserver').set_display_name('Webserver'))

                    if True is self.__validate_certificate:
                        certificate_check = CheckHttp.create(base_id + '_certificate') \
                            .set_ip(server_ip) \
                            .set_vhost(domain) \
                            .set_uri(uri) \
                            .set_ssl(True) \
                            .set_certificate_check(True) \
                            .add_service_group(
                            ServiceGroup.create('certificate_check').set_display_name('Certificate Check')
                        ) \
                            .add_service_group(ServiceGroup.create('https').set_display_name('Https')) \
                            .set_display_name('Certificate expire ' + domain)

                        checkserver.add_check(certificate_check)
                    else:
                        server.add_hostgroup(
                            HostGroup.create('no_certificate_check')
                                .set_display_name('No certificate check Webserver')
                        )

                    if True is self.__validate_http_redirect:
                        redirect_check = CheckHttp.create(base_id + '_http_redirect') \
                            .set_ip(server_ip) \
                            .set_vhost(domain) \
                            .set_uri(uri) \
                            .set_ssl(False) \
                            .set_port(80) \
                            .set_expect('301') \
                            .add_service_group(
                            ServiceGroup.create('http_redirect_check').set_display_name('Http to https redirect')
                        ) \
                            .add_service_group(ServiceGroup.create('https').set_display_name('Https')) \
                            .set_display_name('Http to https redirect ' + domain)
                        server.add_hostgroup(
                            HostGroup.create('http_redirect').set_display_name('Http to https redirect Webserver')
                        )
                        checkserver.add_check(redirect_check)
                    elif True is self.__warn_no_http_redirect:
                        redirect_check = CheckDummy.create(base_id + '_missing_http_redirect') \
                            .set_state(1) \
                            .set_text('No http redirect setup for ' + domain) \
                            .add_service_group(
                            ServiceGroup.create('missing_http_redirect_check')
                                .set_display_name('Missing http to https redirect check')
                        ) \
                            .add_service_group(ServiceGroup.create('http').set_display_name('Http')) \
                            .set_display_name('Http to https redirect ' + domain)

                        checkserver.add_check(redirect_check)
                        server.add_hostgroup(
                            HostGroup.create('no_http_redirect').set_display_name('No http to https redirect Webserver')
                        )
                    else:
                        server.add_hostgroup(
                            HostGroup.create('http_redirect_unchecked')
                                .set_display_name('Http to https redirect Webserver unchecked')
                        )

                    if True is self.__validate_allow_tls1:
                        tls1_check = CheckHttp.create(base_id + '_allow_tls1') \
                            .set_ip(server_ip) \
                            .set_vhost(domain) \
                            .set_uri(uri) \
                            .set_ssl_protocol('1.1') \
                            .add_service_group(ServiceGroup.create('tls_check').set_display_name('TLS Check')) \
                            .add_service_group(ServiceGroup.create('tls_1_check').set_display_name('TLS 1.0')) \
                            .set_display_name('Allow TLS 1.0 ' + domain)

                        checkserver.add_check(tls1_check)
                        server.add_hostgroup(
                            HostGroup.create('insecure_webserver').set_display_name('Insecure Webserver')
                        )
                        server.add_hostgroup(
                            HostGroup.create('insecure_TLSv1_0_Webserver')
                                .set_display_name('Insecure TLS 1.0 Webserver')
                        )
                    elif True is self.__validate_deny_tls1:
                        tls1_check = CheckDenyTlsVersion.create(base_id + '_deny_tls1') \
                            .set_address(server_ip) \
                            .set_domain(domain) \
                            .set_protocol('1.0') \
                            .add_service_group(ServiceGroup.create('tls_check').set_display_name('TLS Check')) \
                            .add_service_group(ServiceGroup.create('tls_1_check').set_display_name('TLS 1.0')) \
                            .set_display_name('Deny TLS 1.0 ' + domain)
                        server.add_hostgroup(
                            HostGroup.create('deny_insecure_TLSv1_0_Webserver')
                                .set_display_name('Deny insecure TLS 1.0 Webserver')
                        )
                        checkserver.add_check(tls1_check)
                    else:
                        server.add_hostgroup(
                            HostGroup.create('deny_insecure_TLSv1_0_unchecked')
                                .set_display_name('Deny insecure TLS 1.0 unchecked')
                        )

                    if True is self.__validate_allow_tls1_1:
                        tls1_1_check = CheckHttp.create(base_id + '_allow_tls1_1') \
                            .set_vhost(domain) \
                            .set_ip(server_ip) \
                            .set_uri(uri) \
                            .set_ssl_protocol('1.1') \
                            .add_service_group(ServiceGroup.create('tls_check').set_display_name('TLS Check')) \
                            .add_service_group(ServiceGroup.create('tls_1_1_check').set_display_name('TLS 1.1')) \
                            .set_display_name('Allow TLS 1.1 ' + domain)

                        checkserver.add_check(tls1_1_check)
                        server.add_hostgroup(
                            HostGroup.create('insecure_webserver').set_display_name('Insecure Webserver')
                        )
                        server.add_hostgroup(
                            HostGroup.create('insecure_TLSv1_1_webserver')
                                .set_display_name('Insecure TLS 1.1 Webserver')
                        )

                    elif True is self.__validate_deny_tls1_1:
                        tls1_1_check = CheckDenyTlsVersion.create(base_id + '_deny_tls1_1') \
                            .set_address(server_ip) \
                            .set_domain(domain) \
                            .set_protocol('1.1') \
                            .add_service_group(ServiceGroup.create('tls_check').set_display_name('TLS Check')) \
                            .add_service_group(ServiceGroup.create('tls_1_1_check').set_display_name('TLS 1.1')) \
                            .set_display_name('Deny TLS 1.1 ' + domain)
                        server.add_hostgroup(
                            HostGroup.create('deny_insecure_TLSv1_1_Webserver')
                                .set_display_name('Deny insecure TLS 1.1 Webserver')
                        )
                        checkserver.add_check(tls1_1_check)
                    else:
                        server.add_hostgroup(
                            HostGroup.create('deny_insecure_TLSv1_1_unchecked')
                                .set_display_name('Inecure TLS 1.1 unchecked')
                        )

                    if True is self.__validate_allow_tls1_2:
                        tls1_2_check = CheckHttp.create(base_id + '_allow_tls1_2') \
                            .set_vhost(domain) \
                            .set_ip(server_ip) \
                            .set_uri(uri) \
                            .set_ssl_protocol('1.2') \
                            .add_service_group(ServiceGroup.create('tls_check').set_display_name('TLS Check')) \
                            .add_service_group(ServiceGroup.create('tls_1_2_check').set_display_name('TLS 1.2')) \
                            .set_display_name('Allow TLS 1.2 ' + domain)

                        checkserver.add_check(tls1_2_check)
                        server.add_hostgroup(HostGroup.create('secure_webserver').set_display_name('Secure Webserver'))
                        server.add_hostgroup(
                            HostGroup.create('secure_TLSv1_2_webserver').set_display_name('Secure TLS 1.2 Webserver')
                        )

                    elif True is self.__validate_deny_tls1_2:
                        tls1_2_check = CheckDenyTlsVersion.create(base_id + '_deny_tls1_2') \
                            .set_address(server_ip) \
                            .set_domain(domain) \
                            .set_protocol('1.2') \
                            .add_service_group(ServiceGroup.create('tls_check').set_display_name('TLS Check')) \
                            .add_service_group(ServiceGroup.create('tls_1_2_check').set_display_name('TLS 1.2')) \
                            .set_display_name('Deny TLS 1.2 ' + domain)

                        server.add_hostgroup(HostGroup.create('insecure_webserver'))
                        server.add_hostgroup(
                            HostGroup.create('deny_secure_TLSv1_2_webserver') \
                                .set_display_name('Deny secure TLS 1.2 Webserver')
                        )

                        checkserver.add_check(tls1_2_check)
                    else:
                        server.add_hostgroup(
                            HostGroup.create('secure_TLSv1_2_unchecked').set_display_name('Secure TLS 1.2 unchecked')
                        )

                    if True is self.__validate_allow_tls1_3:
                        tls1_3_check = CheckHttp.create(base_id + '_allow_tls1_3') \
                            .set_ip(server_ip) \
                            .set_vhost(domain) \
                            .set_uri(uri) \
                            .set_ssl_protocol('1.3') \
                            .add_service_group(ServiceGroup.create('tls_check').set_display_name('TLS Check')) \
                            .add_service_group(ServiceGroup.create('tls_1_3_check').set_display_name('TLS 1.3')) \
                            .set_display_name('Allow TLS 1.3 ' + domain)

                        checkserver.add_check(tls1_3_check)
                        server.add_hostgroup(HostGroup.create('secure_webserver').set_display_name('Secure Webserver'))
                        server.add_hostgroup(
                            HostGroup.create('secure_TLSv1_3_Webserver').set_display_name('Secure TLS 1.3 Webserver')
                        )

                    elif True is self.__validate_deny_tls1_3:
                        tls1_3_check = CheckDenyTlsVersion.create(base_id + '_deny_tls1_3') \
                            .set_address(server_ip) \
                            .set_domain(domain) \
                            .set_protocol('1.3') \
                            .add_service_group(ServiceGroup.create('tls_check').set_display_name('TLS Check')) \
                            .add_service_group(ServiceGroup.create('tls_1_3_check').set_display_name('TLS 1.3')) \
                            .set_display_name('Deny TLS 1.3 ' + domain)

                        checkserver.add_check(tls1_3_check)

                        server.add_hostgroup(HostGroup.create('insecure_webserver'))
                        server.add_hostgroup(
                            HostGroup.create('deny_secure_TLSv1_3_webserver') \
                                .set_display_name('Deny secure TLS 1.3 Webserver')
                        )
                    else:
                        server.add_hostgroup(
                            HostGroup.create('secure_TLSv1_3_unchecked').set_display_name('Secure TLS 1.3 unchecked')
                        )
