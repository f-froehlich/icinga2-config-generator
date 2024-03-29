#!/usr/bin/python3
# -*- coding: utf-8
from __future__ import annotations

from typing import List, Callable, Union

from icinga2confgen.Checks.Check import Check
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
from icinga2confgen.Checks.NagiosPlugins.CheckProcs import CheckProcs
from icinga2confgen.Commands.Command import Command
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Dependency.CheckDependency import CheckDependency
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.Notification.Notification import Notification
from icinga2confgen.Servers.Server import Server
from icinga2confgen.ValueChecker import ValueChecker


class LocalCheckManager:

    def __init__(self, servers: List[Server] = [], notifications: List[Notification] = []):
        self.__notifications = notifications
        self.__servers = servers
        self.__check_type = 'local'
        self.__callback_function = None
        self.__auto_apply = True
        self.__auto_applied = False

        ConfigBuilder.add_util_class(self)

    def set_callback_function(self, function: Callable[[Check], None]) -> LocalCheckManager:
        if not callable(function):
            raise Exception('Given function must be callable')
        self.__callback_function = function

        return self

    def set_auto_apply(self, enabled: bool) -> LocalCheckManager:
        ValueChecker.is_bool(enabled)
        self.__auto_apply = enabled
        return self

    def is_auto_apply(self) -> bool:
        return self.__auto_apply

    def set_auto_applied(self, applied: bool) -> LocalCheckManager:
        ValueChecker.is_bool(applied)
        self.__auto_applied = applied
        return self

    def is_auto_applied(self) -> bool:
        return self.__auto_applied

    def get_servers(self) -> List[Server]:
        return self.__servers

    def add_server(self, server: Server) -> LocalCheckManager:
        self.__servers.append(server)
        return self

    def get_notifications(self) -> List[Notification]:
        return self.__notifications

    def set_check_type(self, type: str) -> LocalCheckManager:
        if type not in ['local', 'ssh']:
            raise Exception('Check type must be "local" or "ssh"')
        self.__check_type = type
        return self

    def get_check_type(self) -> str:
        return self.__check_type

    def apply_notification_to_check(self, check: Check) -> LocalCheckManager:
        for notification in self.__notifications:
            check.add_notification(notification)

        return self

    def handle_callback(self, check: Check) -> LocalCheckManager:
        if None is not self.__callback_function:
            self.__callback_function(check)
        return self

    def apply_dependency(self, check: Check, server: Server,
                         depends_on: Union[Check, None] = None) -> LocalCheckManager:

        if None is not depends_on:
            dependency = CheckDependency.create(
                check.get_id() + '_require_' + depends_on.get_id() + '_on_' + server.get_id()) \
                .set_server(server) \
                .set_check(depends_on)
            check.add_dependency(dependency)

        return self

    def apply_check(self, check: Check, server: Server, depends_on: Union[Check, None] = None) -> LocalCheckManager:

        self.apply_notification_to_check(check)
        check.set_check_type(self.__check_type)
        check.set_generated(True)
        check.set_zone(server.get_zone())
        server.add_check(check)
        self.apply_dependency(check, server, depends_on)

        self.handle_callback(check)

        return self

    def create_running_check(self, name: str, command: str, server: Server,
                             service_groups: List[str] = []) -> Check:
        check = CheckProcs.create('running_proc_' + name + '_' + server.get_id()) \
            .set_check_type(self.__check_type) \
            .set_critical_range('1:') \
            .set_command(command) \
            .add_service_group(ServiceGroup.create(name))
        for service_group in service_groups:
            check.add_service_group(ServiceGroup.create(service_group))

        self.apply_check(check, server)

        return check

    def create_running_check_arguments(self, name: str, argument: str, server: Server,
                                       service_groups: List[str] = []) -> Check:
        check = CheckProcs.create('running_proc_' + name + '_' + server.get_id()) \
            .set_check_type(self.__check_type) \
            .set_critical_range('1:') \
            .set_argument(argument) \
            .add_service_group(ServiceGroup.create(name))
        for service_group in service_groups:
            check.add_service_group(ServiceGroup.create(service_group))

        self.apply_check(check, server)

        return check
