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
from Checks.MonitoringPlugins.CheckApt import CheckApt
from Checks.NagiosPlugins.CheckYum import CheckYum
from Checks.MonitoringPlugins.CheckDisk import CheckDisk
from Checks.MonitoringPlugins.CheckLoad import CheckLoad
from Checks.MonitoringPlugins.CheckNTPTime import CheckNTPTime
from Checks.MonitoringPlugins.CheckSWAP import CheckSWAP
from Checks.MonitoringPlugins.CheckProcs import CheckProcs
from Checks.MonitoringPlugins.CheckUsers import CheckUsers
from Groups.ServiceGroup import ServiceGroup


class DefaultLocalChecks:

    def __init__(self, servers=[], notifications=[]):
        self.__servers = servers
        self.__notifications = notifications
        self.__check_type = 'local'
        self.__check_load = True
        self.__check_apt = True
        self.__check_yum = False
        self.__check_users = True
        self.__check_swap = True
        self.__check_ntp_time = True
        self.__check_disk = True
        self.__check_sshd_running = True
        self.__check_mysqld_running = True
        self.__check_cron_running = True
        self.__check_rsyslogd_running = True
        self.__check_nginx_running = False
        self.__check_apache_running = False
        self.__check_httpd_running = False
        self.__check_php_fpm_running = False
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

    def check_sshd_running(self, enabled):
        self.__check_sshd_running = enabled

        return self

    def is_checking_sshd_running(self):
        return self.__check_sshd_running

    def check_mysqld_running(self, enabled):
        self.__check_mysqld_running = enabled

        return self

    def is_checking_mysqld_running(self):
        return self.__check_mysqld_running

    def check_cron_running(self, enabled):
        self.__check_cron_running = enabled

        return self

    def is_checking_cron_running(self):
        return self.__check_cron_running

    def check_rsyslogd_running(self, enabled):
        self.__check_rsyslogd_running = enabled

        return self

    def is_checking_rsyslogd_running(self):
        return self.__check_rsyslogd_running

    def check_nginx_running(self, enabled):
        self.__check_nginx_running = enabled

        return self

    def is_checking_nginx_running(self):
        return self.__check_nginx_running

    def check_apache_running(self, enabled):
        self.__check_apache_running = enabled

        return self

    def is_checking_apache_running(self):
        return self.__check_apache_running

    def check_httpd_running(self, enabled):
        self.__check_httpd_running = enabled

        return self

    def is_checking_httpd_running(self):
        return self.__check_httpd_running

    def check_php_fpm_running(self, enabled):
        self.__check_php_fpm_running = enabled

        return self

    def is_checking_php_fpm_running(self):
        return self.__check_php_fpm_running

    def add_server(self, server):
        self.__servers.append(server)

    def add_partition(self, id, path, warning_percent, critical_percent):
        self.__check_partitions.append((id, path, warning_percent, critical_percent))

        return self

    def add_notification(self, notification):
        self.__notifications.append(notification)
        return self

    def apply_notification_to_check(self, check):
        for notification in self.__notifications:
            check.add_notification(notification)
        return self

    def set_check_type(self, type):
        self.__check_type = type

    def apply(self):
        for server in self.__servers:
            if True is self.__check_apt:
                check = CheckApt.create('apt_' + server.get_id()) \
                    .set_display_name('APT') \
                    .set_check_type(self.__check_type) \
                    .add_service_group(ServiceGroup.create('apt').set_display_name('APT'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_yum:
                check = CheckYum.create('yum_' + server.get_id()) \
                    .set_display_name('YUM') \
                    .set_check_type(self.__check_type) \
                    .add_service_group(ServiceGroup.create('yum').set_display_name('YUM'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_load:
                check = CheckLoad.create('load_' + server.get_id()) \
                    .set_display_name('Load') \
                    .set_check_type(self.__check_type) \
                    .add_service_group(ServiceGroup.create('load').set_display_name('Load'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_ntp_time:
                check = CheckNTPTime.create('ntp_time_' + server.get_id()) \
                    .set_display_name('NTP Time') \
                    .set_check_type(self.__check_type) \
                    .add_service_group(ServiceGroup.create('ntp_time').set_display_name('NTP Time'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_swap:
                check = CheckSWAP.create('swap_' + server.get_id()) \
                    .set_display_name('SWAP') \
                    .set_check_type(self.__check_type) \
                    .add_service_group(ServiceGroup.create('swap').set_display_name('SWAP'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_users:
                check = CheckUsers.create('users_' + server.get_id()) \
                    .set_display_name('Users') \
                    .set_check_type(self.__check_type) \
                    .add_service_group(ServiceGroup.create('users').set_display_name('Users'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_sshd_running:
                check = CheckProcs.create('proc_sshd_' + server.get_id()) \
                    .set_display_name('Running sshd') \
                    .set_check_type(self.__check_type) \
                    .set_critical_range('1:') \
                    .set_command('sshd') \
                    .add_service_group(ServiceGroup.create('procs').set_display_name('Procs')) \
                    .add_service_group(ServiceGroup.create('sshd').set_display_name('sshd'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_mysqld_running:
                check = CheckProcs.create('proc_mysqld_' + server.get_id()) \
                    .set_display_name('Running mysqld') \
                    .set_check_type(self.__check_type) \
                    .set_critical_range('1:') \
                    .set_command('mysqld') \
                    .add_service_group(ServiceGroup.create('procs').set_display_name('Procs')) \
                    .add_service_group(ServiceGroup.create('mysqld').set_display_name('mysqld'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_cron_running:
                check = CheckProcs.create('proc_cron_' + server.get_id()) \
                    .set_display_name('Running cron') \
                    .set_check_type(self.__check_type) \
                    .set_critical_range('1:') \
                    .set_command('cron') \
                    .add_service_group(ServiceGroup.create('procs').set_display_name('Procs')) \
                    .add_service_group(ServiceGroup.create('cron').set_display_name('cron'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_rsyslogd_running:
                check = CheckProcs.create('proc_rsyslogd_' + server.get_id()) \
                    .set_display_name('Running rsyslogd') \
                    .set_check_type(self.__check_type) \
                    .set_critical_range('1:') \
                    .set_command('rsyslogd') \
                    .add_service_group(ServiceGroup.create('procs').set_display_name('Procs')) \
                    .add_service_group(ServiceGroup.create('rsyslogd').set_display_name('rsyslogd'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_nginx_running:
                check = CheckProcs.create('proc_nginx_' + server.get_id()) \
                    .set_display_name('Running nginx') \
                    .set_check_type(self.__check_type) \
                    .set_critical_range('1:') \
                    .set_command('nginx') \
                    .add_service_group(ServiceGroup.create('procs').set_display_name('Procs')) \
                    .add_service_group(ServiceGroup.create('webserver').set_display_name('Webserver')) \
                    .add_service_group(ServiceGroup.create('nginx').set_display_name('nginx'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_apache_running:
                check = CheckProcs.create('proc_apache_' + server.get_id()) \
                    .set_display_name('Running apache') \
                    .set_check_type(self.__check_type) \
                    .set_critical_range('1:') \
                    .set_command('apache2') \
                    .add_service_group(ServiceGroup.create('procs').set_display_name('Procs')) \
                    .add_service_group(ServiceGroup.create('webserver').set_display_name('Webserver')) \
                    .add_service_group(ServiceGroup.create('apache').set_display_name('apache'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_httpd_running:
                check = CheckProcs.create('proc_httpd_' + server.get_id()) \
                    .set_display_name('Running httpd') \
                    .set_check_type(self.__check_type) \
                    .set_critical_range('1:') \
                    .set_command('httpd') \
                    .add_service_group(ServiceGroup.create('procs').set_display_name('Procs')) \
                    .add_service_group(ServiceGroup.create('webserver').set_display_name('Webserver')) \
                    .add_service_group(ServiceGroup.create('httpd').set_display_name('httpd'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_php_fpm_running:
                check = CheckProcs.create('proc_php_fpm_' + server.get_id()) \
                    .set_display_name('Running php_fpm') \
                    .set_check_type(self.__check_type) \
                    .set_critical_range('1:') \
                    .set_command('php-fpm') \
                    .add_service_group(ServiceGroup.create('procs').set_display_name('Procs')) \
                    .add_service_group(ServiceGroup.create('php_fpm').set_display_name('php_fpm'))
                self.apply_notification_to_check(check)
                server.add_check(check)

            if True is self.__check_disk:
                if len(self.__check_partitions) == 0:
                    check = CheckDisk.create('disk_' + server.get_id()) \
                        .set_display_name('Disk ') \
                        .set_check_type(self.__check_type) \
                        .add_service_group(ServiceGroup.create('disk').set_display_name('Disk'))
                    self.apply_notification_to_check(check)
                    server.add_check(check)
                else:
                    for config in self.__check_partitions:
                        check = CheckDisk.create('disk_' + config[0] + server.get_id()) \
                            .set_display_name('Disk ' + config[0]) \
                            .set_check_type(self.__check_type) \
                            .set_partition(config[1]) \
                            .set_warning_percent(config[2]) \
                            .set_critical_percent(config[3]) \
                            .add_service_group(ServiceGroup.create('disk').set_display_name('Disk'))
                        self.apply_notification_to_check(check)
                        server.add_check(check)
