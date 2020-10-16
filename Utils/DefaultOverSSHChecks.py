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
from Checks.CheckApt import CheckApt
from Checks.CheckYum import CheckYum
from Checks.CheckDisk import CheckDisk
from Checks.CheckLoad import CheckLoad
from Checks.CheckNTPTime import CheckNTPTime
from Checks.CheckSWAP import CheckSWAP
from Checks.CheckUsers import CheckUsers
from Groups.ServiceGroup import ServiceGroup
from Checks.CheckSSH import CheckSSH


class DefaultOverSSHChecks:

    def __init__(self, servers=[], notifications=[]):
        self.__notifications = notifications
        self.__servers = servers
        self.__check_load = True
        self.__check_apt = True
        self.__check_yum = False
        self.__check_users = True
        self.__check_swap = True
        self.__check_ntp_time = True
        self.__check_disk = True
        self.__check_partitions = []

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

    def check_yum(self, enabled):
        self.__check_yum = enabled

        return self

    def add_partition(self, id, path, warning_percent, critical_percent):
        self.__check_partitions.append((id, path, warning_percent, critical_percent))

        return self

    def is_checking_yum(self):
        return self.__check_yum

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

    def apply_notification_to_check(self, check):
        for notification in self.__notifications:
            check.add_notification(notification)

    def apply(self):
        for server in self.__servers:

            if True is self.__check_apt:
                check = CheckApt.create('apt_' + server.get_id()) \
                    .set_check_type('ssh') \
                    .set_display_name('APT') \
                    .add_service_group(ServiceGroup.create('apt').set_display_name('APT'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_yum:
                check = CheckYum.create('yum_' + server.get_id()) \
                    .set_check_type('ssh') \
                    .set_display_name('YUM') \
                    .add_service_group(ServiceGroup.create('yum').set_display_name('YUM'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_load:
                check = CheckLoad.create('load_' + server.get_id()) \
                    .set_check_type('ssh') \
                    .set_display_name('Load') \
                    .add_service_group(ServiceGroup.create('load').set_display_name('Load'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_ntp_time:
                check = CheckNTPTime.create('ntp_time_' + server.get_id()) \
                    .set_check_type('ssh') \
                    .set_display_name('NTP Time') \
                    .add_service_group(ServiceGroup.create('ntp_time').set_display_name('NTP Time'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_swap:
                check = CheckSWAP.create('swap_' + server.get_id()) \
                    .set_check_type('ssh') \
                    .set_display_name('SWAP') \
                    .add_service_group(ServiceGroup.create('swap').set_display_name('SWAP'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_users:
                check = CheckUsers.create('users_' + server.get_id()) \
                    .set_check_type('ssh') \
                    .set_display_name('Users') \
                    .add_service_group(ServiceGroup.create('users').set_display_name('Users'))
                self.apply_notification_to_check(check)
                server.add_check(check)

        if True is self.__check_disk:
            if len(self.__check_partitions) == 0:
                check = CheckDisk.create('disk_' +  server.get_id()) \
                    .set_check_type('ssh') \
                    .set_display_name('Disk ') \
                    .add_service_group(ServiceGroup.create('disk').set_display_name('Disk'))
                self.apply_notification_to_check(check)
                server.add_check(check)
            else:
                for config in self.__check_partitions:
                    check = CheckDisk.create('disk_' + config[0] +  server.get_id()) \
                        .set_check_type('ssh') \
                        .set_display_name('Disk ' + config[0]) \
                        .set_partition(config[1]) \
                        .set_warning_percent(config[2]) \
                        .set_critical_percent(config[3]) \
                        .add_service_group(ServiceGroup.create('disk').set_display_name('Disk'))
                    self.apply_notification_to_check(check)
                    server.add_check(check)

