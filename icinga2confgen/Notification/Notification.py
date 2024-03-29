#!/usr/bin/python3
# -*- coding: utf-8
import typing

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
from icinga2confgen.Groups.UserGroup import UserGroup
from icinga2confgen.Notification.NotificationCommand import NotificationCommand
from icinga2confgen.Notification.TimePeriod import TimePeriod
from icinga2confgen.User.User import User
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper
from typing import List, Union
T = typing.TypeVar('T', bound='Notification')


class Notification:

    def __init__(self, id: str):
        self.__id = id
        self.__interval = '1h'
        self.__command = self.get_command_config()
        self.__time_period = None
        self.__escalation = None
        self.__users = []
        self.__user_groups = []

        self.__allowed_host_types = ['DowntimeStart', 'DowntimeEnd', 'DowntimeRemoved', 'Custom', 'Acknowledgement',
                                     'Problem', 'Recovery', 'FlappingStart', 'FlappingEnd']
        self.__host_types = self.__allowed_host_types
        self.__allowed_host_states = ['Up', 'Down']
        self.__host_states = self.__allowed_host_states

        self.__allowed_service_types = ['DowntimeStart', 'DowntimeEnd', 'DowntimeRemoved', 'Custom', 'Acknowledgement',
                                        'Problem', 'Recovery', 'FlappingStart', 'FlappingEnd']
        self.__service_types = self.__allowed_service_types
        self.__allowed_service_states = ['Warning', 'Critical', 'Unknown', 'OK']
        self.__service_states = self.__allowed_service_states

    def get_command_config(self) -> NotificationCommand:
        raise Exception('You must override get_command_config')

    def user_config_function(self, user: User) -> typing.List[str]:
        raise Exception('You must override user_config_function')

    def group_config_function(self, group: UserGroup) -> List[str]:
        raise Exception('You must override group_config_function')

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        raise Exception('Cannot create Notification, use child classes instead')

    def get_id(self) -> str:
        return self.__id

    def set_interval(self, interval: str) -> T:
        self.__interval = interval
        return self

    def get_interval(self) -> str:
        return self.__interval

    def set_command(self, command: NotificationCommand) -> T:

        self.__command = command
        return self

    def get_command(self) -> NotificationCommand:
        return self.__command

    def set_time_period(self, time_period: typing.Union[TimePeriod, None]) -> T:
        self.__time_period = time_period

        return self

    def get_time_period(self) -> Union[TimePeriod, None]:
        return self.__time_period

    def set_escalation(self, begin: str, end: str) -> T:
        self.__escalation = (begin, end)

        return self

    def get_escalation(self) -> Union[typing.Tuple[str, str], None]:
        return self.__escalation

    def set_host_types(self, types: List[str]) -> T:
        for type in types:
            if type not in self.__allowed_host_types:
                raise Exception('Type ' + type + ' is not allowed for host')
        self.__host_types = types
        return self

    def get_host_types(self) -> List[str]:
        return self.__host_types

    def set_host_states(self, states: List[str]) -> T:
        for state in states:
            if state not in self.__allowed_host_states:
                raise Exception('State ' + state + ' is not allowed for host')
        self.__host_states = states
        return self

    def get_host_states(self) -> List[str]:
        return self.__host_states

    def set_service_types(self, types: List[str]) -> T:
        for type in types:
            if type not in self.__allowed_service_types:
                raise Exception('Type ' + type + ' is not allowed for service')
        self.__service_types = types
        return self

    def get_service_types(self) -> List[str]:
        return self.__service_types

    def set_service_states(self, states: List[str]) -> T:
        for state in states:
            if state not in self.__allowed_service_states:
                raise Exception('State ' + state + ' is not allowed for service')
        self.__service_states = states
        return self

    def get_service_states(self) -> List[str]:
        return self.__service_states

    def add_user(self, user: User) -> T:

        if user not in self.__users:
            self.__users.append(user)

        return self

    def remove_user(self, user: User) -> T:
        if user in self.__users:
            self.__users.remove(user)

        return self

    def get_users(self) -> List[User]:
        return self.__users

    def add_user_group(self, user_group: UserGroup) -> T:

        if user_group not in self.__user_groups:
            self.__user_groups.append(user_group)

        return self

    def remove_user_group(self, user_group: UserGroup) -> T:
        if user_group in self.__user_groups:
            self.__user_groups.remove(user_group)

        return self

    def get_user_groups(self) -> List[UserGroup]:
        return self.__user_groups

    def validate(self):
        if None is self.__command:
            raise Exception('You have to set a Command for Notification!')

        if 0 == len(self.__users) and 0 == len(self.__user_groups):
            raise Exception('You have to add a user or user group for Notification ' + self.__id)

    def get_config(self) -> str:
        self.validate()

        config = 'template Notification "notification_template_host_' + self.__id + '" {\n'
        config += '  interval = ' + self.__interval + '\n'

        if None is not self.__escalation:
            config += '  times = {\n'
            config += '    begin = ' + self.__escalation[0] + '\n'
            config += '    end = ' + self.__escalation[1] + '\n'
            config += '  }\n'

        config += ValueMapper.parse_var('command', self.__command.get_id(), value_prefix='command_host_')
        if None is not self.__time_period:
            config += ValueMapper.parse_var('period', self.__time_period.get_id(), value_prefix='time_period_')
        config += ValueMapper.parse_var('types', self.__host_types)
        config += ValueMapper.parse_var('states', self.__host_states)
        config += '}\n'
        config += 'template Notification "notification_template_service_' + self.__id + '" {\n'
        config += '  interval = ' + self.__interval + '\n'

        if None is not self.__escalation:
            config += '  times = {\n'
            config += '    begin = ' + self.__escalation[0] + '\n'
            config += '    end = ' + self.__escalation[1] + '\n'
            config += '  }\n'

        config += ValueMapper.parse_var('command', self.__command.get_id(), value_prefix='command_service_')
        if None is not self.__time_period:
            config += ValueMapper.parse_var('period', self.__time_period, value_prefix='time_period_')
        config += ValueMapper.parse_var('types', self.__service_types)
        config += ValueMapper.parse_var('states', self.__service_states)
        config += '}\n'
        config += self.apply_for_all()

        return config

    def apply_for_all(self) -> str:

        config_user = ''
        config_group = ''
        all_users = ConfigBuilder.get_instance('users')

        configured_users = []

        # configure users set in this notification
        for user in self.__users:
            if user in configured_users:
                continue

            # write config for user
            configured_users.append(user)
            user_data_config = enumerate(self.user_config_function(user))
            for key, config in user_data_config:
                notification_id = 'notification_' + self.get_id() + '_user_' + user.get_id() + '_' + str(key)
                config_user += self.get_assign_config(config, notification_id, users=[user])

        # configure groups set in this notification
        for group in self.__user_groups:
            for user in all_users:
                # do not send multiple notifications to a user and only send, if user should receive notification
                # via direct assignment or group assignment
                if user in configured_users or (user not in self.__users and group not in user.get_groups()):
                    continue

                # write config for user
                configured_users.append(user)
                user_data_config = enumerate(self.user_config_function(user))
                for key, config in user_data_config:
                    notification_id = 'notification_' + self.get_id() + '_user_' + user.get_id() + '_' + str(key)
                    config_user += self.get_assign_config(config, notification_id, users=[user])

            # write config for group
            group_data_config = enumerate(self.group_config_function(group))
            for key, config in group_data_config:
                notification_id = 'notification_' + self.get_id() + '_group_' + group.get_id() + '_' + str(key)
                config_group += self.get_assign_config(config, notification_id,
                                                       users=['group_notification_sender_' + group.get_id()])

        return config_user + config_group

    def get_assign_config(self, custom_config, notification_id, users=None, groups=None) -> str:
        config = ''
        for type in ['Host', 'Service']:
            config += 'apply Notification "' + type.lower() + '_' + notification_id + '" to ' + type + ' {\n'
            config += '  import "notification_template_' + type.lower() + '_' \
                      + Notification.get_id(self) + '"\n'
            config += ValueMapper.parse_var('user_groups', groups, value_prefix='usergroup_')
            config += ValueMapper.parse_var('users', users, value_prefix='user_')
            config += custom_config
            config += '  assign where "notification_' + self.get_id() + '" in ' \
                      + type.lower() + '.vars.notification\n'
            config += '}\n'
        return config
