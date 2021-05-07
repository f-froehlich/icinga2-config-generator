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
import typing

from icinga2confgen.Checks.MonitoringPlugins.Webserver.Apache2.CheckProxyRequests import CheckProxyRequests
from icinga2confgen.Utils.DefaultLocalChecks import DefaultLocalChecks
from icinga2confgen.ValueChecker import ValueChecker

T = typing.TypeVar('T', bound='DefaultLocalWebserverChecks')


class DefaultLocalWebserverChecks(DefaultLocalChecks):

    def __init__(self: T, servers=[], notifications=[], sudoers=[], additional_users=[]):
        DefaultLocalChecks.__init__(self, servers, notifications, sudoers, additional_users)
        self.__inherit = True

        self.__check_apache2_proxy_requests = True

    def set_inherit(self: T, enabled: bool) -> T:
        ValueChecker.is_bool(enabled)
        self.__inherit = enabled

        return self

    def is_inherit(self: T) -> bool:
        return self.__inherit

    def check_apache2_proxy_requests(self: T, enabled: bool) -> T:
        ValueChecker.is_bool(enabled)
        self.__check_apache2_proxy_requests = enabled

        return self

    def is_checking_apache2_proxy_requests(self) -> bool:
        return self.__check_apache2_proxy_requests

    def apply(self: T):
        if self.__inherit:
            DefaultLocalChecks.apply(self)

        for server in DefaultLocalChecks.get_servers(self):
            if True is self.__check_apache2_proxy_requests:
                check = CheckProxyRequests.create('proxy_requests_' + server.get_id())
                self.apply_check(check, server)
