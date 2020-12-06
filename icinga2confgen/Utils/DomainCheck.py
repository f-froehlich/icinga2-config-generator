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
from icinga2confgen.Checks.MonitoringPlugins.CheckDNSSECExpire import CheckDNSSECExpire
from icinga2confgen.Checks.NagiosPlugins.CheckDig import CheckDig
from icinga2confgen.Helpers.RemoteCheckManager import RemoteCheckManager


class DomainCheck(RemoteCheckManager):

    def __init__(self, domain_configs=[], checkserver=[], notifications=[]):
        RemoteCheckManager.__init__(self, servers=[], checkserver=checkserver, notifications=notifications)
        self.__domain_configs = domain_configs

    def add_domainconfig(self, config):
        self.__domain_configs.append(config)

    def apply(self):

        for config in self.__domain_configs:
            domain = config[0]
            ipv4 = config[1]
            ipv6 = config[2]
            dnssec = config[3]
            base_id = ''.join(e for e in domain if e.isalnum())

            if True is dnssec:
                dnssec_check = CheckDNSSECExpire.create('dnssec_expiry') \
                    .add_dns_domain(domain)

                self.apply_check(dnssec_check)

            if None is not ipv4:
                ipv4_check = CheckDig.create('domain_address_ipv4_' + base_id)
                ipv4_check.set_record_type('A') \
                    .set_question(domain) \
                    .set_expected_address(ipv4) \
                    .set_display_name(ipv4_check.get_display_name() + ' ' + domain)

                self.apply_check(ipv4_check)

            if None is not ipv6:
                ipv6_check = CheckDig.create('domain_address_ipv6_' + base_id)
                ipv6_check.set_record_type('AAAA') \
                    .set_question(domain) \
                    .set_expected_address(ipv6) \
                    .set_display_name(ipv6_check.get_display_name() + ' ' + domain)
                self.apply_check(ipv6_check)
