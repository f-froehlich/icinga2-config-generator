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

from ConfigBuilder import ConfigBuilder
from Groups.UserGroup import UserGroup
from ValueChecker import ValueChecker


class User:

    def __init__(self, id):
        self.__id = id
        self.__display_name = None
        self.__enable_notifications = True
        self.__states = ['OK', 'Warning', 'Critical', 'Unknown', 'Down']
        self.__allowed_states = ['OK', 'Warning', 'Critical', 'Unknown', 'Down']
        self.__types = [
            'Problem', 'Acknowledgement', 'Recovery', 'Custom', 'FlappingStart',
            'FlappingEnd', 'DowntimeStart', 'DowntimeEnd', 'DowntimeRemoved'
        ]
        self.__allowed_types = [
            'Problem', 'Acknowledgement', 'Recovery', 'Custom', 'FlappingStart',
            'FlappingEnd', 'DowntimeStart', 'DowntimeEnd', 'DowntimeRemoved'
        ]
        self.__phone = None
        self.__email = None
        self.__groups = []

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)

        user = ConfigBuilder.get_user(id)
        if None is user:
            id = 'user_' + id
            user = User(id)
            ConfigBuilder.add_user(id, user)

        return user

    def get_id(self):
        return self.__id

    def set_display_name(self, display_name):
        ValueChecker.is_string(display_name)
        self.__display_name = display_name
        return self

    def get_display_name(self):
        return self.__display_name

    def set_email(self, email):
        ValueChecker.is_string(email)
        self.__email = email
        return self

    def get_email(self):
        return self.__email

    def set_phone(self, phone):
        ValueChecker.is_string(phone)
        self.__phone = phone
        return self

    def get_phone(self):
        return self.__phone

    def set_types(self, types):
        for type in types:
            if type not in self.__allowed_types:
                raise Exception('Type ' + type + ' is not allowed')
        self.__types = types
        return self

    def get_types(self):
        return self.__types

    def set_states(self, states):
        for state in states:
            if state not in self.__allowed_states:
                raise Exception('State ' + state + ' is not allowed')
        self.__states = states
        return self

    def get_states(self):
        return self.__states

    def add_group(self, group):

        if isinstance(group, UserGroup):
            self.__groups.append(group.get_id())

        elif isinstance(group, str):
            if None is ConfigBuilder.get_usergroup(group):
                raise Exception('UserGroup does not exist yet!')
            self.__groups.append(group)
        else:
            raise Exception('Can only add UserGroup or id of UserGroup!')

        return self

    def set_enable_notifications(self, enable_notifications):
        ValueChecker.is_bool(enable_notifications)
        self.__enable_notifications = enable_notifications
        return self

    def get_enable_notifications(self):
        return self.__enable_notifications

    def get_config(self):
        config = 'object User "' + self.__id + '" {\n'
        config += '  email = "' + self.__email + '"\n'

        if None is not self.__phone:
            config += '  vars.phone = "' + self.__phone + '"\n'

        if None is not self.__display_name:
            config += '  display_name = "' + self.__display_name + '"\n'

        if True is self.__enable_notifications:
            config += '  enable_notifications = true\n'
        else:
            config += '  enable_notifications = false\n'

        for group in self.__groups:
            config += '  groups += [ "' + group + '" ]\n'

        config += '  states = []\n'
        for state in self.__states:
            config += '  states += [ "' + state + '" ]\n'

        config += '  types = []\n'
        for type in self.__types:
            config += '  types += [ "' + type + '" ]\n'

        config += '}\n'

        return config
