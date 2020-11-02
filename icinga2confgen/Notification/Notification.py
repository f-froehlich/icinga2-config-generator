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
from icinga2confgen.Groups.UserGroup import UserGroup
from icinga2confgen.Notification.NotificationCommand import NotificationCommand
from icinga2confgen.Notification.TimePeriod import TimePeriod
from icinga2confgen.User.User import User
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class Notification:

    def __init__(self, id):
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

    def get_command_config(self):
        raise Exception('You must override get_command_config')

    @staticmethod
    def create(id, force_create=False):
        raise Exception('Cannot create Notification, use child classes instead')

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
            command = ConfigBuilder.get_notification_command(command)
            if None is command:
                raise Exception('NotificationCommand does not exist yet!')
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

    def set_host_types(self, types):
        for type in types:
            if type not in self.__allowed_host_types:
                raise Exception('Type ' + type + ' is not allowed for host')
        self.__host_types = types
        return self

    def get_host_types(self):
        return self.__host_types

    def set_host_states(self, states):
        for state in states:
            if state not in self.__allowed_host_states:
                raise Exception('State ' + state + ' is not allowed for host')
        self.__host_states = states
        return self

    def get_host_states(self):
        return self.__host_states

    def set_service_types(self, types):
        for type in types:
            if type not in self.__allowed_service_types:
                raise Exception('Type ' + type + ' is not allowed for service')
        self.__service_types = types
        return self

    def get_service_types(self):
        return self.__service_types

    def set_service_states(self, states):
        for state in states:
            if state not in self.__allowed_service_states:
                raise Exception('State ' + state + ' is not allowed for service')
        self.__service_states = states
        return self

    def get_service_states(self):
        return self.__service_states

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

        config = 'template Notification "notification_template_host_' + self.__id + '" {\n'
        config += '  interval = ' + self.__interval + '\n'

        if None is not self.__escalation:
            config += '  times = {\n'
            config += '    begin = ' + self.__escalation[0] + '\n'
            config += '    end = ' + self.__escalation[1] + '\n'
            config += '  }\n'

        config += ValueMapper.parse_var('command', self.__command, value_prefix='command_host_')
        config += ValueMapper.parse_var('period', self.__time_period, value_prefix='time_period_')
        config += ValueMapper.parse_var('user_groups', self.__user_groups, value_prefix='usergroup_')
        config += ValueMapper.parse_var('users', self.__users, value_prefix='user_')
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

        config += ValueMapper.parse_var('command', self.__command, value_prefix='command_service_')
        config += ValueMapper.parse_var('period', self.__time_period, value_prefix='time_period_')
        config += ValueMapper.parse_var('user_groups', self.__user_groups, value_prefix='usergroup_')
        config += ValueMapper.parse_var('users', self.__users, value_prefix='user_')
        config += ValueMapper.parse_var('types', self.__service_types)
        config += ValueMapper.parse_var('states', self.__service_states)
        config += '}\n'

        return config

    def apply_for_all_emails(self):

        config = ''
        all_users = ConfigBuilder.get_instance('users')
        for group in self.get_user_groups():
            added_user = []
            for user in all_users:
                if user in added_user:
                    continue

                added_user.append(user)
                added_emails = []
                groups_of_user = user.get_groups()
                if group in groups_of_user:
                    for email in user.get_email():
                        if email in added_emails:
                            continue

                        added_emails.append(email)
                        cemail = ValueMapper.canonicalize_for_id(email.replace('@', '_'))
                        for type in ['Service', 'Host']:
                            notification_id = 'notification_' + type.lower() + '_' + self.get_id() + '_' \
                                              + user.get_id() + '_' + cemail
                            config += 'apply Notification "' + notification_id + '" to ' + type + ' {\n'
                            config += '  import "notification_template_' + type.lower() + '_' \
                                      + Notification.get_id(self) + '"\n'
                            config += '  vars.email = "' + email + '"\n'
                            config += '  assign where "notification_' + self.get_id() + '" in ' \
                                      + type.lower() + '.vars.notification\n'
                            config += '}\n'

        return config
