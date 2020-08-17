#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, commands, checks, ... in python
#
#  Copyright (c) 2020 Fabian Fröhlich <mail@f-froehlich.de> https://f-froehlich.de
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

from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker

class SSHTemplate:

    def __init__(self, id):
        self.__id = id
        self.__host = None
        self.__identityfile = None
        self.__user = 'icinga'
        self.__port = 22

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)

        template = ConfigBuilder.get_ssh_template(id)
        if None is template:
            id = 'ssh_template_' + id
            template = SSHTemplate(id)
            ConfigBuilder.add_vhost(id, template)

        return template

    def get_id(self):
        return self.__id

    def set_hostname(self, hostname):
        ValueChecker.is_string(hostname)
        self.__host = hostname
        return self

    def get_hostname(self):
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
        config = 'template Host "' + self.__id + '" {\n'
        config += ConfigBuilder.get_property_default_config(self, 'SSHTemplate', 'overssh', 'command')
        config += '}\n'

        return config
