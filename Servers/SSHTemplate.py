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


# TODO
class SSHTemplate:

    def __init__(self, id):
        self.__id = id
        self.__hostname = None

    @staticmethod
    def create(id):
        ConfigBuilder.validate_id(id)

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
        self.__hostname = hostname
        return self

    def get_hostname(self):
        return self.__hostname

    def get_config(self):
        config = 'template Service "' + self.__id + '" {\n'
        config += ConfigBuilder.get_property_default_config(self, 'SSHTemplate', 'ssh', 'ssh')
        config += '}\n'

        return config
