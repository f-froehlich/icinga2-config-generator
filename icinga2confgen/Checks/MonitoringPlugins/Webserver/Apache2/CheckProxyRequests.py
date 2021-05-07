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
from __future__ import annotations

import typing
from typing import List

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.MonitoringPlugins.Webserver.Apache2.ProxyRequestsCommand import ProxyRequestsCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='CheckProxyRequests')


class CheckProxyRequests(Check):

    def __init__(self: T, id: str):
        Check.__init__(self, id, 'CheckProxyRequests', 'monitoring_plugins_webserver_apache2_proxy_requests')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('webserver'))
        self.set_check_interval('24h')

        self.__allow: List[str] = []

    def set_allow(self: T, allow: List[str]) -> T:
        self.__allow = allow
        return self

    def get_allow(self: T) -> List[str]:

        return self.__allow

    def add_allow(self, file: str) -> T:
        if file not in self.__allow:
            self.__allow.append(file)

        return self

    def remove_allow(self, file: str) -> T:
        if file in self.__allow:
            self.__allow.remove(file)

        return self

    def validate(self):
        pass

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckProxyRequests(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckProxyRequests):
            raise Exception('Id must be for an instance of CheckProxyRequests but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_webserver_apache2_proxy_requests'):
            ProxyRequestsCommand.create('monitoring_plugins_webserver_apache2_proxy_requests')

        return check
