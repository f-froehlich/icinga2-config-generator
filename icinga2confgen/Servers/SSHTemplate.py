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

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class SSHTemplate:

    def __init__(self, id):
        self.__id = id
        self.__host = None
        self.__identityfile = None
        self.__user = 'icinga'
        self.__port = 22
        self.__timeout = 30
        self.__plugin_dir = '/usr/lib/nagios/plugins/'

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)

        template = None if force_create else ConfigBuilder.get_ssh_template(id)
        if None is template:
            template = SSHTemplate(id)
            ConfigBuilder.add_ssh_template(id, template)

        return template

    def get_id(self):
        return self.__id

    def set_hostname(self, hostname):
        ValueChecker.is_string(hostname)
        self.__host = hostname
        return self

    def get_hostname(self):
        return self.__host

    def set_plugin_dir(self, plugin_dir):
        ValueChecker.is_string(plugin_dir)
        self.__host = plugin_dir
        return self

    def get_plugin_dir(self):
        return self.__host

    def set_user(self, user):
        ValueChecker.is_string(user)
        self.__user = user
        return self

    def get_user(self):
        return self.__user

    def set_identity_file(self, identity_file):
        ValueChecker.is_string(identity_file)
        self.__identityfile = identity_file
        return self

    def get_identity_file(self):
        return self.__identityfile

    def set_port(self, port):
        ValueChecker.is_number(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    def get_config(self):
        config = 'template Host "sshtemplate_' + self.__id + '" {\n'
        config += ValueMapper.get_property_default_config(self, 'SSHTemplate', 'overssh', 'command')
        config += '}\n'

        return config
