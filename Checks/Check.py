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
from Groups.ServiceGroup import ServiceGroup
from Notification.ServiceNotification import ServiceNotification
from ValueChecker import ValueChecker


class Check:

    def __init__(self, id, class_name, command_name):
        self.__command_name = command_name
        self.__class_name = class_name
        self.__id = id
        self.__service_groups = []
        self.__check_type = "local"
        self.__notifications = []
        self.__allowed_check_types = ["local", "ssh"]

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)
        id = 'check_' + id
        check = ConfigBuilder.get_check(id)
        if None is check:
            check = Check(id, 'Check', 'check')
            ConfigBuilder.add_check(id, check)

        return check

    def add_service_group(self, group):
        if isinstance(group, ServiceGroup):
            self.__service_groups.append(group.get_id())
        elif isinstance(group, str):
            self.__service_groups.append('servicegroup_' + group)
        else:
            raise Exception('Can only add Servicegroup or id of Servicegroup!')

        return self

    def add_notification(self, notification):
        if isinstance(notification, ServiceNotification):
            self.__notifications.append(notification.get_id())
        elif isinstance(notification, str):
            self.__notifications.append(notification)
        else:
            raise Exception('Can only add ServiceNotification or id of ServiceNotification!')

        return self

    def get_service_group_ids(self):

        return self.__service_groups

    def get_id(self):
        return self.__id

    def set_check_type(self, type):
        if type in self.__allowed_check_types:
            self.__check_type = type
            return self
        raise Exception("Checktype must be " + ' or '.join(self.__allowed_check_types))

    def get_check_type(self):
        return self.__check_type

    def get_custom_definitions(self):
        return []

    def get_config(self):

        config = 'apply Service "' + self.get_id() + '" {\n'
        config += '  check_command = "command_' + self.__command_name + '_' + self.__check_type + '"\n'
        config += self.get_property_default_config()
        config += self.get_custom_property_config()
        config += self.get_group_config()
        config += self.get_notification_config()
        config += '  assign where host.vars.' + self.get_id() + '\n'
        config += '}\n'

        return config

    def get_group_config(self):
        config = ''
        for group in self.__service_groups:
            config += '  vars.' + group + ' = true\n'

        return config

    def get_notification_config(self):
        config = ''
        for notification in self.__notifications:
            config += '  vars.' + notification + ' = true\n'

        return config

    def get_custom_property_config(self):
        config = ''
        for line in self.get_custom_definitions():
            config += '  ' + line + '\n'

        return config

    def get_property_default_config(self):

        return ConfigBuilder.get_property_default_config(self, self.__class_name, self.__command_name, 'command')
