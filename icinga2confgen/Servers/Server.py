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

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Servers.ServerTemplate import ServerTemplate
from icinga2confgen.ValueChecker import ValueChecker


class Server(ServerTemplate):

    def __init__(self, id: str):
        ServerTemplate.__init__(self, id)
        self.__id = id

    def get_id(self) -> str:
        return self.__id

    @staticmethod
    def create(id: str, force_create: bool = False) -> Server:
        ValueChecker.validate_id(id)

        server = None if force_create else ConfigBuilder.get_server(id)
        if None is server:
            server = Server(id)
            ConfigBuilder.add_server(id, server)

        return server

    def get_config(self) -> str:
        config = ServerTemplate.get_config(self)
        config += 'object Host "' + self.get_id() + '" {\n'
        config += '  import "servertemplate_' + ServerTemplate.get_id(self) + '"\n'
        config += '}\n'

        return config
