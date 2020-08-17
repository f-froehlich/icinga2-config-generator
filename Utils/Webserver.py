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
from Checks.Check import Check
from Checks.CheckApt import CheckApt
from Checks.CheckDNSSECExpire import CheckDNSSECExpire
from Checks.CheckDenyTlsVersion import CheckDenyTlsVersion
from Checks.CheckDisk import CheckDisk
from Checks.CheckDummy import CheckDummy
from Checks.CheckHttp import CheckHttp
from Checks.CheckLoad import CheckLoad
from Checks.CheckNTPTime import CheckNTPTime
from Checks.CheckPing import CheckPing
from Checks.CheckSSH import CheckSSH
from Checks.CheckSWAP import CheckSWAP
from Checks.CheckUsers import CheckUsers
from ConfigBuilder import ConfigBuilder
from Groups.HostGroup import HostGroup
from Groups.ServiceGroup import ServiceGroup
from Servers.VHost import VHost


class Webserver:

    def __init__(self, vhostconfig=[], servers=[]):
        self.__servers = servers
        self.__vhostconfigs = vhostconfig
        self.__validate_zone = True
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

        self.__check_ssh = True
        self.__check_load = True
        self.__check_apt = True
        self.__check_users = True
        self.__check_swap = True
        self.__check_ntp_time = True
        self.__check_disk = True

    def validate_zone(self, enabled):
        self.__validate_zone = enabled

        return self

    def is_validating_zone(self):
        return self.__validate_zone

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

    def check_ssh(self, enabled):
        self.__check_ssh = enabled

        return self

    def is_checking_ssh(self):
        return self.__check_ssh

    def check_load(self, enabled):
        self.__check_load = enabled

        return self

    def is_checking_load(self):
        return self.__check_load

    def check_apt(self, enabled):
        self.__check_apt = enabled

        return self

    def is_checking_apt(self):
        return self.__check_apt

    def check_users(self, enabled):
        self.__check_users = enabled

        return self

    def is_checking_users(self):
        return self.__check_users

    def check_swap(self, enabled):
        self.__check_swap = enabled

        return self

    def is_checking_swap(self):
        return self.__check_swap

    def check_ntp_time(self, enabled):
        self.__check_ntp_time = enabled

        return self

    def is_checking_ntp_time(self):
        return self.__check_ntp_time

    def check_disk(self, enabled):
        self.__check_disk = enabled

        return self

    def is_checking_disk(self):
        return self.__check_disk

    def add_server(self, server):
        self.__servers.append(server)

    def add_vhostconfig(self, config):
        self.__vhostconfigs.append(config)

    def apply(self):
        for config in self.__vhostconfigs:
            domain = config[0]
            uri = config[1]
            additional_checks = config[2]
            base_id = ''.join(e for e in domain if e.isalnum())

            ping_check = CheckPing.create(base_id + '_ping') \
                .add_service_group(ServiceGroup.create('ping'))

            vhost = VHost.create(base_id).set_hostname(domain)
            vhost.add_check(ping_check)
            if True is self.__validate_zone:
                zone_check = CheckDNSSECExpire.create(base_id + '_dnssec') \
                    .set_zone(domain) \
                    .add_service_group(ServiceGroup.create('dnssec_check'))

                vhost.add_check(zone_check)

            if True is self.__validate_certificate:
                certificate_check = CheckHttp.create(base_id + '_certificate') \
                    .set_uri(uri) \
                    .set_ssl(True) \
                    .set_certificate_check(True) \
                    .add_service_group(ServiceGroup.create('certificate_check')) \
                    .add_service_group(ServiceGroup.create('https_server'))
                vhost.add_check(certificate_check)

            if True is self.__validate_http_redirect:
                redirect_check = CheckHttp.create(base_id + '_http_redirect') \
                    .set_uri(uri) \
                    .set_ssl(False) \
                    .set_port(80) \
                    .set_expect('301') \
                    .add_service_group(ServiceGroup.create('http_redirect_check')) \
                    .add_service_group(ServiceGroup.create('https_server'))

                vhost.add_check(redirect_check)
            elif True is self.__warn_no_http_redirect:
                redirect_check = CheckDummy.create(base_id + '_missing_http_redirect') \
                    .set_state(1) \
                    .set_text('No http redirect setup for ' + domain) \
                    .add_service_group(ServiceGroup.create('missing_http_redirect_check')) \
                    .add_service_group(ServiceGroup.create('https_server'))

                vhost.add_check(redirect_check)

            if True is self.__validate_allow_tls1:
                tls1_check = CheckHttp.create(base_id + '_allow_tls1') \
                    .set_uri(uri) \
                    .set_ssl_protocol('1.1') \
                    .add_service_group(ServiceGroup.create('tls_check')) \
                    .add_service_group(ServiceGroup.create('insecure_https_server'))
                vhost.add_check(tls1_check)
            elif True is self.__validate_deny_tls1:
                tls1_check = CheckDenyTlsVersion.create(base_id + '_deny_tls1') \
                    .set_domain(domain) \
                    .set_protocol('1.0') \
                    .add_service_group(ServiceGroup.create('tls_check')) \
                    .add_service_group(ServiceGroup.create('deny_insecure_tls')) \
                    .add_service_group(ServiceGroup.create('deny_insecure_tls_1_0'))
                vhost.add_check(tls1_check)

            if True is self.__validate_allow_tls1_1:
                tls1_1_check = CheckHttp.create(base_id + '_allow_tls1_1') \
                    .set_uri(uri) \
                    .set_ssl_protocol('1.1') \
                    .add_service_group(ServiceGroup.create('tls_check')) \
                    .add_service_group(ServiceGroup.create('insecure_https_server'))
                vhost.add_check(tls1_1_check)
            elif True is self.__validate_deny_tls1_1:
                tls1_1_check = CheckDenyTlsVersion.create(base_id + '_deny_tls1_1') \
                    .set_domain(domain) \
                    .set_protocol('1.1') \
                    .add_service_group(ServiceGroup.create('tls_check')) \
                    .add_service_group(ServiceGroup.create('deny_insecure_tls')) \
                    .add_service_group(ServiceGroup.create('deny_insecure_tls_1_1'))
                vhost.add_check(tls1_1_check)

            if True is self.__validate_allow_tls1_2:
                tls1_2_check = CheckHttp.create(base_id + '_allow_tls1_2') \
                    .set_uri(uri) \
                    .set_ssl_protocol('1.2') \
                    .add_service_group(ServiceGroup.create('tls_check')) \
                    .add_service_group(ServiceGroup.create('secure_https_server'))
                vhost.add_check(tls1_2_check)
            elif True is self.__validate_deny_tls1_2:
                tls1_2_check = CheckDenyTlsVersion.create(base_id + '_deny_tls1_2') \
                    .set_domain(domain) \
                    .set_protocol('1.2') \
                    .add_service_group(ServiceGroup.create('tls_check')) \
                    .add_service_group(ServiceGroup.create('deny_secure_tls')) \
                    .add_service_group(ServiceGroup.create('deny_secure_tls_1_2'))
                vhost.add_check(tls1_2_check)

            if True is self.__validate_allow_tls1_3:
                tls1_3_check = CheckHttp.create(base_id + '_allow_tls1_3') \
                    .set_uri(uri) \
                    .set_ssl_protocol('1.3') \
                    .add_service_group(ServiceGroup.create('tls_check')) \
                    .add_service_group(ServiceGroup.create('secure_https_server')) \
                    .add_service_group(ServiceGroup.create('modern_https_server'))

                vhost.add_check(tls1_3_check)
            elif True is self.__validate_deny_tls1_3:
                tls1_3_check = CheckDenyTlsVersion.create(base_id + '_deny_tls1_3') \
                    .set_domain(domain) \
                    .set_protocol('1.3') \
                    .add_service_group(ServiceGroup.create('tls_check')) \
                    .add_service_group(ServiceGroup.create('deny_secure_tls')) \
                    .add_service_group(ServiceGroup.create('deny_secure_tls_1_3'))
                vhost.add_check(tls1_3_check)

            # additional checks
            for check in additional_checks:
                if isinstance(check, Check):
                    vhost.add_check(check)

                elif isinstance(check, str):
                    check = ConfigBuilder.get_check(check)
                    if None is check:
                        raise Exception('Check does not exist yet!')
                    vhost.add_check(check)
                else:
                    raise Exception('You can only add Check or id of Check!')

            for server in self.__servers:
                server.add_vhost(vhost) \
                    .add_hostgroup(HostGroup.create('webserver'))

        for server in self.__servers:

            if True is self.__check_apt:
                check = CheckApt.create(server.get_id() + '_apt') \
                    .set_check_type('ssh') \
                    .add_service_group(ServiceGroup.create('apt'))
                server.add_check(check) \
                    .add_hostgroup(HostGroup.create('apt'))

            if True is self.__check_load:
                check = CheckLoad.create(server.get_id() + '_load') \
                    .set_check_type('ssh') \
                    .add_service_group(ServiceGroup.create('load'))
                server.add_check(check)

            if True is self.__check_ntp_time:
                check = CheckNTPTime.create(server.get_id() + '_ntp_time') \
                    .set_check_type('ssh') \
                    .add_service_group(ServiceGroup.create('ntp_time'))
                server.add_check(check)

            if True is self.__check_swap:
                check = CheckSWAP.create(server.get_id() + '_swap') \
                    .set_check_type('ssh') \
                    .add_service_group(ServiceGroup.create('swap'))
                server.add_check(check)

            if True is self.__check_users:
                check = CheckUsers.create(server.get_id() + '_users') \
                    .set_check_type('ssh') \
                    .add_service_group(ServiceGroup.create('users'))
                server.add_check(check)

            if True is self.__check_ssh:
                check = CheckSSH.create(server.get_id() + '_ssh') \
                    .set_hostname(server.get_ipv4() or server.get_ipv6()) \
                    .set_port(10) \
                    .add_service_group(ServiceGroup.create('ssh'))
                server.add_check(check) \
                    .add_hostgroup(HostGroup.create('ssh'))

            if True is self.__check_disk:
                check = CheckDisk.create(server.get_id() + '_disk') \
                    .add_service_group(ServiceGroup.create('disk'))
                server.add_check(check)
