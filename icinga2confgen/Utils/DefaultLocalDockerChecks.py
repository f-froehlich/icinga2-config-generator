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

from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.Utils.DefaultLocalChecks import DefaultLocalChecks
from icinga2confgen.ValueChecker import ValueChecker


class DefaultLocalDockerChecks(DefaultLocalChecks):

    def __init__(self, servers=[], notifications=[], sudoers=[], additional_users=[]):
        DefaultLocalChecks.__init__(self, servers, notifications, sudoers, additional_users)
        self.__check_docker_running = True
        self.__check_containerd_running = True
        self.__inherit = True

    def set_inherit(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__inherit = enabled

        return self

    def is_inherit(self):
        return self.__inherit

    def check_docker_running(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__check_docker_running = enabled

        return self

    def is_checking_docker_running(self):
        return self.__check_docker_running

    def check_containerd_running(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__check_containerd_running = enabled

        return self

    def is_checking_containerd_running(self):
        return self.__check_containerd_running

    def apply(self):
        if self.__inherit:
            DefaultLocalChecks.apply(self)

        for server in DefaultLocalChecks.get_server(self):
            if True is self.__check_docker_running:
                self.create_running_check_arguments('docker', 'dockerd', server)

            if True is self.__check_containerd_running:
                check = self.create_running_check_arguments('containerd', 'containerd', server)
                check.add_service_group(ServiceGroup.create('docker'))
