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
from Checks.CheckPing4 import CheckPing4
from Checks.CheckPing6 import CheckPing6

class DefaultRemoteChecks:

    def __init__(self, servers=[], checkserver=[], notifications=[]):
        self.__checkserver = checkserver
        self.__notifications = notifications
        self.__servers = servers
        self.__check_ping = True


    def check_ping(self, enabled):
        self.__check_ping = enabled

        return self

    def is_checking_ping(self):
        return self.__check_ping

    def apply_check(self, check):
        for notification in self.__notifications:
            check.add_notification(notification)

        for checkserver in self.__checkserver:
            checkserver.add_check(check)

    def apply(self):
        for server in self.__servers:
            base_id = 'remote_checks_' + server.get_id()
            ipv4 = server.get_ipv4()
            ipv6 = server.get_ipv6()


            if True is self.__check_ping:
                ping_service_group = ServiceGroup.create('ping').set_display_name('Ping')
                ping4_service_group = ServiceGroup.create('ping4').set_display_name('Ping 4')
                ping6_service_group = ServiceGroup.create('ping6').set_display_name('Ping 6')
                if None is not ipv4:
                    check = CheckPing4.create(base_id + '_ping4') \
                        .set_address(ipv4) \
                        .add_service_group(ping_service_group) \
                        .add_service_group(ping4_service_group) \
                        .set_display_name('Ping ipv4 ' + server.get_display_name())
                    self.apply_check(check)
                if None is not ipv6:
                    check = CheckPing4.create(base_id + '_ping6') \
                        .set_address(ipv6) \
                        .add_service_group(ping_service_group) \
                        .add_service_group(ping6_service_group) \
                        .set_display_name('Ping ipv6 ' + server.get_display_name())
                    self.apply_check(check)
