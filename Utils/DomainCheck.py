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
from Checks.CheckDNSSECExpire import CheckDNSSECExpire
from Checks.CheckDig import CheckDig
from Groups.ServiceGroup import ServiceGroup
from Servers.Server import Server


class DomainCheck:

    def __init__(self, domain_configs=[]):
        self.__domain_configs = domain_configs

    def add_domainconfig(self, config):
        self.__domain_configs.append(config)

    def apply(self):

        server_dummy = Server.create('domaincheck_dummy') \
            .set_display_name('Domaincheck server') \
            .set_ipv4('127.0.0.1')

        for config in self.__domain_configs:
            domain = config[0]
            ipv4 = config[1]
            ipv6 = config[2]
            dnssec = config[3]
            base_id = ''.join(e for e in domain if e.isalnum())

            if True is dnssec:
                dnssec_check = CheckDNSSECExpire.create(base_id + '_dnssec') \
                    .set_zone(domain) \
                    .add_service_group(ServiceGroup.create('dnssec_check'))

                server_dummy.add_check(dnssec_check)

            if None is not ipv4:
                ipv4_check = CheckDig.create(base_id + '_ipv4') \
                    .set_record_type('A') \
                    .set_question(domain) \
                    .set_expected_address(ipv4) \
                    .add_service_group(ServiceGroup.create('dns_check'))

                server_dummy.add_check(ipv4_check)

            if None is not ipv6:
                ipv4_check = CheckDig.create(base_id + '_ipv6') \
                    .set_record_type('AAAA') \
                    .set_question(domain) \
                    .set_expected_address(ipv6) \
                    .add_service_group(ServiceGroup.create('dns_check'))

                server_dummy.add_check(ipv4_check)
