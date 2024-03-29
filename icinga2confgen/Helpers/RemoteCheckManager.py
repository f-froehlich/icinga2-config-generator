#!/usr/bin/python3
# -*- coding: utf-8
from __future__ import annotations

from typing import List, Union

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
from icinga2confgen.Helpers.LocalCheckManager import LocalCheckManager
from icinga2confgen.Notification.Notification import Notification
from icinga2confgen.Servers.Server import Server


class RemoteCheckManager(LocalCheckManager):

    def __init__(self, checkserver: List[Server] = [], servers: List[Server] = [],
                 notifications: List[Notification] = []):
        LocalCheckManager.__init__(self, servers=servers, notifications=notifications)
        self.__checkserver = checkserver

    def get_checkservers(self) -> List[Server]:
        return self.__checkserver

    def add_checkserver(self, checkserver: Server) -> RemoteCheckManager:
        self.__checkserver.append(checkserver)
        return self

    def apply_check(self, check: Check, server: Server, checkserver: Server,
                    depends_on: Union[Check, None] = None) -> RemoteCheckManager:
        self.apply_notification_to_check(check)
        check.set_check_type(self.get_check_type())
        check.set_generated(True)
        check.set_zone(checkserver.get_zone())
        check.set_nagios_plugindir(checkserver.get_nagios_plugindir())
        check.set_monitoring_plugindir(checkserver.get_monitoring_plugindir())
        check.set_harik_sekhon_plugindir(checkserver.get_harik_sekhon_plugindir())
        check.set_other_plugindir(checkserver.get_other_plugindir())
        check.set_claudio_kuenzler_plugindir(checkserver.get_claudio_kuenzler_plugindir())
        server.add_check(check)
        self.apply_dependency(check, server, depends_on)

        self.handle_callback(check)
