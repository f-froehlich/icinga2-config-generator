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

from typing import Union

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Helpers.PluginDirs import PluginDirs
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class SSHTemplate(PluginDirs):

    def __init__(self, id: str):
        PluginDirs.__init__(self)
        self.__id = id
        self.__host = None
        self.__identityfile = None
        self.__user = 'icinga'
        self.__port = 22
        self.__timeout = 30

    @staticmethod
    def create(id: str, force_create: bool = False) -> SSHTemplate:
        ValueChecker.validate_id(id)

        template = None if force_create else ConfigBuilder.get_ssh_template(id)
        if None is template:
            template = SSHTemplate(id)
            ConfigBuilder.add_ssh_template(id, template)

        return template

    def get_id(self) -> str:
        return self.__id

    def set_hostname(self, hostname: str) -> SSHTemplate:
        self.__host = hostname
        return self

    def get_hostname(self) -> Union[str, None]:
        return self.__host

    def set_user(self, user: str) -> SSHTemplate:
        self.__user = user
        return self

    def get_user(self) -> str:
        return self.__user

    def set_identity_file(self, identity_file: str) -> SSHTemplate:
        self.__identityfile = identity_file
        return self

    def get_identity_file(self) -> Union[str, None]:
        return self.__identityfile

    def set_port(self, port: int) -> SSHTemplate:
        self.__port = port
        return self

    def get_port(self) -> int:
        return self.__port

    def validate(self):
        if None is self.__host:
            raise Exception('You have to specify the host in SSHTemplate on ' + self.__id)

    def get_config(self) -> str:
        self.validate()

        config = 'template Host "sshtemplate_' + self.__id + '" {\n'
        config += ValueMapper.get_property_default_config(self, 'SSHTemplate', 'overssh', 'command')
        config += ValueMapper.parse_var('vars.command_overssh_nagios_plugin_dir', self.get_nagios_plugindir())
        config += ValueMapper.parse_var('vars.command_overssh_monitoring_plugin_dir', self.get_monitoring_plugindir())
        config += ValueMapper.parse_var('vars.command_overssh_harik_sekhon_plugin_dir',
                                        self.get_harik_sekhon_plugindir())
        config += '}\n'

        return config
