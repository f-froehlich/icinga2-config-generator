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
from Checks.CheckDNSSECExpire import CheckDNSSECExpire
from Checks.CheckDig import CheckDig
from Groups.ServiceGroup import ServiceGroup
from Servers.Server import Server


class DomainCheck:

    def __init__(self, domain_configs=[], checkserver=[]):
        self.__domain_configs = domain_configs
        self.__checkserver = checkserver

    def add_domainconfig(self, config):
        self.__domain_configs.append(config)

    def add_checkserver(self, checkserver):
        self.__checkserver.append(checkserver)

    def apply(self):

        for checkserver in self.__checkserver:

            for config in self.__domain_configs:
                domain = config[0]
                ipv4 = config[1]
                ipv6 = config[2]
                dnssec = config[3]
                base_id = ''.join(e for e in domain if e.isalnum())

                if True is dnssec:
                    dnssec_check = CheckDNSSECExpire.create(base_id + '_dnssec') \
                        .set_zone(domain) \
                        .add_service_group(ServiceGroup.create('dnssec_check').set_display_name('DNSSEC')) \
                        .set_display_name('DNSSEC ' + domain) \
                        .set_check_interval('15m')

                    checkserver.add_check(dnssec_check)

                if None is not ipv4:
                    ipv4_check = CheckDig.create(base_id + '_ipv4') \
                        .set_record_type('A') \
                        .set_question(domain) \
                        .set_expected_address(ipv4) \
                        .add_service_group(ServiceGroup.create('dns_check').set_display_name('DNS')) \
                        .set_display_name('DNS A ' + domain) \
                        .set_check_interval('5m')

                    checkserver.add_check(ipv4_check)

                if None is not ipv6:
                    ipv4_check = CheckDig.create(base_id + '_ipv6') \
                        .set_record_type('AAAA') \
                        .set_question(domain) \
                        .set_expected_address(ipv6) \
                        .add_service_group(ServiceGroup.create('dns_check').set_display_name('DNS')) \
                        .set_display_name('DNS AAAA ' + domain) \
                        .set_check_interval('5m')

                    checkserver.add_check(ipv4_check)
