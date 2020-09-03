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
from Checks.CheckApt import CheckApt
from Checks.CheckDisk import CheckDisk
from Checks.CheckLoad import CheckLoad
from Checks.CheckNTPTime import CheckNTPTime
from Checks.CheckSWAP import CheckSWAP
from Checks.CheckUsers import CheckUsers
from Groups.ServiceGroup import ServiceGroup


class DefaultLocalChecks:

    def __init__(self, servers=[]):
        self.__servers = servers
        self.__check_load = True
        self.__check_apt = True
        self.__check_users = True
        self.__check_swap = True
        self.__check_ntp_time = True
        self.__check_disk = True

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

    def apply(self):
        for server in self.__servers:
            if True is self.__check_apt:
                check = CheckApt.create('apt') \
                    .set_display_name('APT') \
                    .add_service_group(ServiceGroup.create('apt').set_display_name('APT'))
                server.add_check(check)

            if True is self.__check_load:
                check = CheckLoad.create('load') \
                    .set_display_name('Load') \
                    .add_service_group(ServiceGroup.create('load').set_display_name('Load'))
                server.add_check(check)

            if True is self.__check_ntp_time:
                check = CheckNTPTime.create('ntp_time') \
                    .set_display_name('NTP Time') \
                    .add_service_group(ServiceGroup.create('ntp_time').set_display_name('NTP Time'))
                server.add_check(check)

            if True is self.__check_swap:
                check = CheckSWAP.create('swap') \
                    .set_display_name('SWAP') \
                    .add_service_group(ServiceGroup.create('swap').set_display_name('SWAP'))
                server.add_check(check)

            if True is self.__check_users:
                check = CheckUsers.create('users') \
                    .set_display_name('Users') \
                    .add_service_group(ServiceGroup.create('users').set_display_name('Users'))
                server.add_check(check)

            if True is self.__check_disk:
                check = CheckDisk.create('disk') \
                    .set_display_name('Disk') \
                    .add_service_group(ServiceGroup.create('disk').set_display_name('Disk'))
                server.add_check(check)
