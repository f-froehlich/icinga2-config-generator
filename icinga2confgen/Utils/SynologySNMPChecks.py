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
from typing import List, Tuple

from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckCPUFanStatus import CheckCPUFanStatus
from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckDiskTemperature import CheckDiskTemperature
from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckGPUInfo import CheckGPUInfo
from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckPowerStatus import CheckPowerStatus
from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckRAIDStatus import CheckRAIDStatus
from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckSMART import CheckSMART
from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckServiceRunning import CheckServiceRunning
from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckServiceUsed import CheckServiceUsed
from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckSpaceIO import CheckSpaceIO
from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckStorageIO import CheckStorageIO
from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckSystemStatus import CheckSystemStatus
from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckTemperature import CheckTemperature
from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckUpgrade import CheckUpgrade
from icinga2confgen.Checks.MonitoringPlugins.SNMP.UCD_DISKIO_MIB.CheckLoad import CheckLoad as DiskLoad
from icinga2confgen.Checks.MonitoringPlugins.SNMP.UCD_SNMP_MIB.CheckLoad import CheckLoad as CPULoad
from icinga2confgen.Checks.MonitoringPlugins.SNMP.UCD_SNMP_MIB.CheckMemory import CheckMemory
from icinga2confgen.Checks.Other.CheckSynologyStatus import CheckSynologyStatus
from icinga2confgen.Helpers.RemoteCheckManager import RemoteCheckManager
from icinga2confgen.Notification.Notification import Notification
from icinga2confgen.Servers.Server import Server
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class SynologySNMPChecks(RemoteCheckManager):

    def __init__(self, servers: List[Server] = [], checkserver: List[Server] = [],
                 notifications: List[Notification] = []):
        RemoteCheckManager.__init__(self, servers=servers, checkserver=checkserver, notifications=notifications)
        self.__check_general_status: bool = True
        self.__check_system_status: bool = True
        self.__check_temperature: bool = True
        self.__check_upgrade: bool = True
        self.__check_cpu_fan_status: bool = True
        self.__check_raid_status: bool = True
        self.__check_power_status: bool = True
        self.__check_disk_temperature: bool = True
        self.__check_smart: bool = True
        self.__check_gpu_info: bool = True
        self.__check_space_io: bool = True
        self.__check_storage_io: bool = True
        self.__check_service_used: bool = True
        self.__check_service_running: bool = True
        self.__check_disk_load: bool = True
        self.__check_cpu_load: bool = True
        self.__check_memory: bool = True
        self.__services: List[Tuple[str, int, int]] = []

    def check_general_status(self, enabled: bool):
        self.__check_general_status = enabled

        return self

    def is_checking_general_status(self) -> bool:
        return self.__check_general_status

    def check_system_status(self, enabled: bool):
        self.__check_system_status = enabled

        return self

    def is_checking_system_status(self) -> bool:
        return self.__check_system_status

    def check_temperature(self, enabled: bool):
        self.__check_temperature = enabled

        return self

    def is_checking_temperature(self) -> bool:
        return self.__check_temperature

    def check_upgrade(self, enabled: bool):
        self.__check_upgrade = enabled

        return self

    def is_checking_upgrade(self) -> bool:
        return self.__check_upgrade

    def check_cpu_fan_status(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_cpu_fan_status = enabled

        return self

    def is_checking_cpu_fan_status(self):
        return self.__check_cpu_fan_status

    def check_raid_status(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_raid_status = enabled

        return self

    def is_checking_raid_status(self):
        return self.__check_raid_status

    def check_power_status(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_power_status = enabled

        return self

    def is_checking_power_status(self):
        return self.__check_power_status

    def check_disk_temperature(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_disk_temperature = enabled

        return self

    def is_checking_disk_temperature(self):
        return self.__check_disk_temperature

    def check_gpu_info(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_gpu_info = enabled

        return self

    def is_checking_gpu_info(self):
        return self.__check_gpu_info

    def check_smart(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_smart = enabled

        return self

    def is_checking_smart(self):
        return self.__check_smart

    def check_space_io(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_space_io = enabled

        return self

    def is_checking_space_io(self):
        return self.__check_space_io

    def check_storage_io(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_storage_io = enabled

        return self

    def is_checking_storage_io(self):
        return self.__check_storage_io

    def check_service_used(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_service_used = enabled

        return self

    def is_checking_service_used(self):
        return self.__check_service_used

    def check_service_running(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_service_running = enabled

        return self

    def is_checking_service_running(self):
        return self.__check_service_running

    def check_disk_load(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_disk_load = enabled

        return self

    def is_checking_disk_load(self):
        return self.__check_disk_load

    def check_cpu_load(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_cpu_load = enabled

        return self

    def is_checking_cpu_load(self):
        return self.__check_cpu_load

    def check_memory(self, enabled: bool):
        ValueChecker.is_bool(enabled)
        self.__check_memory = enabled

        return self

    def is_checking_memory(self):
        return self.__check_memory

    def add_service(self, service: str, warning: int, critical: int):
        self.__services.append((service, warning, critical))

        return self

    def remove_service(self, service: str):
        for s in self.__services:
            if service == s[0]:
                self.__services.remove(s)
                return

    def apply(self):
        for server in self.get_servers():
            ipv4 = server.get_ipv4()
            ipv6 = server.get_ipv6()
            memory_count = server.get_custom_var('memory_count')
            disk_count = server.get_custom_var('disk_count')
            volume_count = server.get_custom_var('volume_count')
            raid_count = server.get_custom_var('raid_count')
            gpu_count = server.get_custom_var('gpu_count')
            username = server.get_custom_var('snmp_username')
            password = server.get_custom_var('password')

            if None is ipv4 and None is ipv6:
                raise Exception(
                    'Require IPv4 or IPv6 for server "{server}"'.format(server=server.get_id()))
            elif None is not ipv4:
                ip = ipv4
            else:
                ip = ipv6

            if None is disk_count or not isinstance(disk_count, int):
                raise Exception(
                    'Require custom var "disk_count" as integer for server "{server}"'.format(server=server.get_id()))
            if None is volume_count or not isinstance(volume_count, int):
                raise Exception(
                    'Require custom var "volume_count" as integer for server "{server}"'.format(server=server.get_id()))
            if None is raid_count or not isinstance(raid_count, int):
                raise Exception(
                    'Require custom var "raid_count" as integer for server "{server}"'.format(server=server.get_id()))
            if None is gpu_count or not isinstance(gpu_count, int):
                raise Exception(
                    'Require custom var "gpu_count" as integer for server "{server}"'.format(server=server.get_id()))

            if None is username:
                raise Exception(
                    'Require custom var "snmp_username" for server "{server}"'.format(server=server.get_id()))

            if None is password:
                raise Exception(
                    'Require custom var "snmp_password" for server "{server}"'.format(server=server.get_id()))

            for checkserver in self.get_checkservers():
                base_id = 'synology_checks_' + server.get_id() + '_' + checkserver.get_id()

                if self.__check_general_status:
                    check = CheckSynologyStatus.create('synology_status_' + base_id)
                    check.set_host(ip) \
                        .set_user(username) \
                        .set_password(password) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check, server, checkserver)

                if self.__check_system_status:
                    check = CheckSystemStatus.create('synology_system_status_' + base_id)
                    check.set_host(ip) \
                        .set_username(username) \
                        .set_password(password) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check, server, checkserver)

                if self.__check_temperature:
                    check = CheckTemperature.create('synology_temperature_' + base_id)
                    check.set_host(ip) \
                        .set_username(username) \
                        .set_password(password) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check, server, checkserver)

                if self.__check_upgrade:
                    check = CheckUpgrade.create('synology_upgrade_' + base_id)
                    check.set_host(ip) \
                        .set_username(username) \
                        .set_password(password) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check, server, checkserver)

                if self.__check_cpu_fan_status:
                    check = CheckCPUFanStatus.create('synology_cpu_fan_status_' + base_id)
                    check.set_host(ip) \
                        .set_username(username) \
                        .set_password(password) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check, server, checkserver)

                if self.__check_raid_status:
                    check = CheckRAIDStatus.create('synology_raid_status_' + base_id)
                    check.set_host(ip) \
                        .set_username(username) \
                        .set_password(password) \
                        .set_raids(raid_count) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check, server, checkserver)

                if self.__check_power_status:
                    check = CheckPowerStatus.create('synology_power_status_' + base_id)
                    check.set_host(ip) \
                        .set_username(username) \
                        .set_password(password) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check, server, checkserver)

                if self.__check_disk_temperature:
                    check = CheckDiskTemperature.create('synology_disk_temperature_' + base_id)
                    check.set_host(ip) \
                        .set_username(username) \
                        .set_password(password) \
                        .set_disks(disk_count) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                    self.apply_check(check, server, checkserver)

                if self.__check_gpu_info:
                    for gpu in range(0, gpu_count):
                        check = CheckGPUInfo.create(f'synology_gpu_info_{gpu}_{base_id}')
                        check.set_host(ip) \
                            .set_username(username) \
                            .set_password(password) \
                            .set_gpu(gpu) \
                            .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                        self.apply_check(check, server, checkserver)

                if self.__check_smart:
                    for disk in range(0, disk_count):
                        check = CheckSMART.create(f'synology_smart_{disk}_{base_id}')
                        check.set_host(ip) \
                            .set_username(username) \
                            .set_password(password) \
                            .set_disk(disk) \
                            .set_display_name(check.get_display_name() + ' Disk ' + str(disk))
                        self.apply_check(check, server, checkserver)

                if self.__check_space_io:
                    for volume in range(1, volume_count + 1):
                        check = CheckSpaceIO.create(f'synology_space_io_{volume}_{base_id}')
                        check.set_host(ip) \
                            .set_username(username) \
                            .set_password(password) \
                            .set_volume(volume) \
                            .set_display_name(check.get_display_name() + ' Volume ' + str(volume))
                        self.apply_check(check, server, checkserver)

                if self.__check_storage_io:
                    for disk in range(1, disk_count + 1):
                        check = CheckStorageIO.create(f'synology_storage_io_{disk}_{base_id}')
                        check.set_host(ip) \
                            .set_username(username) \
                            .set_password(password) \
                            .set_disk(disk) \
                            .set_display_name(check.get_display_name() + ' Disk ' + str(volume))
                        self.apply_check(check, server, checkserver)

                if self.__check_service_used:
                    for service in self.__services:
                        check = CheckServiceUsed.create(f'synology_service_used_{ValueMapper.canonicalize_for_id(service[0])}_{base_id}')
                        check.set_host(ip) \
                            .set_username(username) \
                            .set_password(password) \
                            .set_service(service[0]) \
                            .set_warning(service[1]) \
                            .set_critical(service[2]) \
                            .set_display_name(check.get_display_name() + ' ' + service[0])

                        self.apply_check(check, server, checkserver)

                if self.__check_service_running:
                    check = CheckServiceRunning.create(f'synology_service_running_{base_id}')
                    check.set_host(ip) \
                        .set_username(username) \
                        .set_password(password) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())

                    for service in self.__services:
                        check.add_service(service[0])

                    self.apply_check(check, server, checkserver)

                if self.__check_disk_load:
                    for disk in range(1, disk_count + 1):
                        check = DiskLoad.create(f'synology_disk_load_{disk}_{base_id}')
                        check.set_host(ip) \
                            .set_username(username) \
                            .set_password(password) \
                            .set_disks(disk) \
                            .set_display_name(check.get_display_name() + ' ' + server.get_display_name())

                        self.apply_check(check, server, checkserver)

                if self.__check_cpu_load:
                    check = CPULoad.create(f'synology_cpu_load_{base_id}')
                    check.set_host(ip) \
                        .set_username(username) \
                        .set_password(password) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())

                    self.apply_check(check, server, checkserver)

                if self.__check_memory:
                    check = CheckMemory.create(f'synology_memory_{base_id}')
                    check.set_host(ip) \
                        .set_username(username) \
                        .set_password(password) \
                        .set_memory(memory_count) \
                        .set_display_name(check.get_display_name() + ' ' + server.get_display_name())

                    self.apply_check(check, server, checkserver)
