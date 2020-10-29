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

from icinga2confgen.Commands.MonitoringPlugins.NotificationCommand import NotificationCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.UserGroup import UserGroup
from icinga2confgen.Notification.TimePeriod import TimePeriod
from icinga2confgen.User.User import User
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class NotificationTemplate:

    def __init__(self, id):
        self.__id = id
        self.__interval = '30m'
        self.__command = None
        self.__time_period = None
        self.__escalation = None
        self.__users = []
        self.__user_groups = []
        self.__states = self.get_allowed_states()
        self.__allowed_states = self.get_allowed_states()
        self.__types = self.get_allowed_types()
        self.__allowed_types = self.get_allowed_types()

    def get_allowed_states(self):
        raise Exception('You must override get_allowed_states')

    def get_allowed_types(self):
        raise Exception('You must override get_allowed_types')

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)

        notification = None if force_create else ConfigBuilder.get_notification_template(id)
        if None is notification:
            notification = NotificationTemplate(id)
            ConfigBuilder.add_notification_template(id, notification)

        return notification

    def get_id(self):
        return self.__id

    def set_interval(self, interval):
        ValueChecker.is_string(interval)
        self.__interval = interval
        return self

    def get_interval(self):
        return self.__interval

    def set_command(self, command):
        if isinstance(command, NotificationCommand):
            self.__command = command.get_id()
        elif isinstance(command, str):
            command = None if force_create else ConfigBuilder.get_command(command)
            if None is command:
                raise Exception('NotificationCommand does not exist yet!')
            if not isinstance(command, NotificationCommand):
                raise Exception('You can only set a NotificationCommand as command for Notification!')
            self.__command = command.get_id()
        return self

    def get_command(self):
        return self.__command

    def set_time_period(self, time_period):
        if isinstance(time_period, TimePeriod):
            self.__time_period = time_period.get_id()

        elif isinstance(time_period, str):
            if None is ConfigBuilder.get_time_period(time_period):
                raise Exception('Time Period does not exist yet!')
            self.__time_period = time_period
        else:
            raise Exception('Can only add Time Period or id of Time Period!')
        return self

    def get_time_period(self):
        return self.__time_period

    def set_escalation(self, begin, end):
        ValueChecker.is_string(begin)
        ValueChecker.is_string(end)
        self.__escalation = (begin, end)

        return self

    def get_escalation(self):
        return self.__escalation

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

    def add_user(self, user):
        if isinstance(user, User):
            if user not in self.__users:
                self.__users.append(user)

        elif isinstance(user, str):
            user = ConfigBuilder.get_user(user)
            if None is user:
                raise Exception('User does not exist yet!')
            self.add_user(user)
        else:
            raise Exception('Can only add User or id of User!')
        return self

    def remove_user(self, user):
        if isinstance(user, User):
            self.__users.remove(user)

        elif isinstance(user, str):
            user = ConfigBuilder.get_user(user)
            self.__users.remove(user)

        return self

    def get_users(self):
        return self.__users

    def add_user_group(self, user_group):
        if isinstance(user_group, UserGroup):
            if user_group not in self.__user_groups:
                self.__user_groups.append(user_group)

        elif isinstance(user_group, str):
            user_group = ConfigBuilder.get_usergroup(user_group)
            if None is user_group:
                raise Exception('UserGroup does not exist yet!')
            self.add_user_group(user_group)
        else:
            raise Exception('Can only add UserGroup or id of UserGroup!')
        return self

    def remove_user_group(self, user_group):
        if isinstance(user_group, UserGroup):
            self.__user_groups.remove(user_group)

        elif isinstance(user_group, str):
            user_group = ConfigBuilder.get_usergroup(user_group)
            self.__user_groups.remove(user_group)

        return self

    def get_user_groups(self):
        return self.__user_groups

    def validate(self):
        if None is self.__command:
            raise Exception('You have to set a Command for Notification!')

        if 0 == len(self.__users) and 0 == len(self.__user_groups):
            raise Exception('You have to add a user or user group for Notification ' + self.__id)

    def get_config(self):
        self.validate()

        config = 'template Notification "notification_template_' + self.__id + '" {\n'
        config += '  interval = ' + self.__interval + '\n'

        if None is not self.__escalation:
            config += '  times = {\n'
            config += '    begin = ' + self.__escalation[0] + '\n'
            config += '    end = ' + self.__escalation[1] + '\n'
            config += '  }\n'

        config += ValueMapper.parse_var('command', self.__command, value_prefix='command_')
        config += ValueMapper.parse_var('period', self.__time_period, value_prefix='time_period_')
        config += ValueMapper.parse_var('user_groups', self.__user_groups, value_prefix='usergroup_')
        config += ValueMapper.parse_var('users', self.__users, value_prefix='user_')
        config += ValueMapper.parse_var('types', self.__types)
        config += ValueMapper.parse_var('states', self.__states)
        config += '}\n'

        return config
