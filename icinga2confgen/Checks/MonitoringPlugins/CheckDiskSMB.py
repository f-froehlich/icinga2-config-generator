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

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.MonitoringPlugins.DiskSMBCommand import DiskSMBCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckDiskSMB(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckDiskSMB', 'disk_smb')
        self.__host = None
        self.__warning = 85
        self.__critical = 95
        self.__share = None
        self.__workgroup = None
        self.__ip = None
        self.__user = None
        self.__password = None
        self.__port = 445
        self.add_service_group(ServiceGroup.create('disk'))

    def set_host(self, host):
        ValueChecker.is_string(host)
        self.__host = host
        return self

    def get_host(self):
        return self.__host

    def set_warning(self, warning):
        ValueChecker.is_number(warning)
        self.__warning = warning
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, critical):
        ValueChecker.is_number(critical)
        self.__critical = critical
        return self

    def get_critical(self):
        return self.__critical

    def set_share(self, share):
        ValueChecker.is_string(share)
        self.__share = share
        return self

    def get_share(self):
        return self.__share

    def set_workgroup(self, workgroup):
        ValueChecker.is_string(workgroup)
        self.__workgroup = workgroup
        return self

    def get_workgroup(self):
        return self.__workgroup

    def set_ip(self, ip):
        ValueChecker.is_string(ip)
        self.__ip = ip
        return self

    def get_ip(self):
        return self.__ip

    def set_user(self, user):
        ValueChecker.is_string(user)
        self.__user = user
        return self

    def get_user(self):
        return self.__user

    def set_password(self, password):
        ValueChecker.is_string(password)
        self.__password = password
        return self

    def get_password(self):
        return self.__password

    def set_port(self, port):
        ValueChecker.is_number(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckDiskSMB(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('disk_smb'):
            DiskSMBCommand.create('disk_smb')

        return check

    def validate(self):
        if None is self.__share:
            raise Exception('You have to specify a share for ' + self.get_id())
        if None is self.__ip:
            raise Exception('You have to specify an ip for ' + self.get_id())
        if None is self.__user:
            raise Exception('You have to specify a user for ' + self.get_id())
        if None is self.__password:
            raise Exception('You have to specify a password for ' + self.get_id())
