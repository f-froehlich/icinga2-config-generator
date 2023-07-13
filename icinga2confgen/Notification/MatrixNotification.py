#!/usr/bin/python3
# -*- coding: utf-8
from __future__ import annotations

from typing import List, Union

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.UserGroup import UserGroup
from icinga2confgen.Notification.MatrixNotificationCommand import MatrixNotificationCommand
from icinga2confgen.Notification.Notification import Notification
from icinga2confgen.User.User import User
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


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


class MatrixNotification(Notification):

    def __init__(self, id: str):
        Notification.__init__(self, id)
        self.__header = []
        self.__uri = None
        self.__domain = None
        self.__port = None
        self.__ssl = False
        self.__client_cert = None
        self.__client_key = None
        self.__timeout = 60
        self.__message_template_short = None
        self.__message_template_additional = None

    def set_timeout(self, timeout: int) -> MatrixNotification:
        ValueChecker.is_number(timeout)
        self.__timeout = timeout
        return self

    def get_timeout(self) -> int:
        return self.__timeout

    def set_header(self, header: str) -> MatrixNotification:
        self.__header.append(header)
        return self

    def get_header(self) -> List[str]:
        return self.__header

    def set_uri(self, uri: Union[str, None]) -> MatrixNotification:
        self.__uri = uri
        return self

    def get_uri(self) -> Union[str, None]:
        return self.__uri

    def set_domain(self, domain: Union[str, None]) -> MatrixNotification:
        self.__domain = domain
        return self

    def get_domain(self) -> str:
        return self.__domain

    def set_port(self, port: Union[int, None]) -> MatrixNotification:
        self.__port = port
        return self

    def get_port(self) -> Union[str, None]:
        return self.__port

    def set_ssl(self, ssl: bool) -> MatrixNotification:
        self.__ssl = ssl
        return self

    def get_ssl(self) -> bool:
        return self.__ssl

    def set_client_cert(self, client_cert: Union[str, None]) -> MatrixNotification:
        self.__client_cert = client_cert
        return self

    def get_client_cert(self) -> Union[str, None]:
        return self.__client_cert

    def set_client_key(self, client_key: Union[str, None]) -> MatrixNotification:
        self.__client_key = client_key
        return self

    def get_client_key(self) -> Union[str, None]:
        return self.__client_key


    def set_message_template_short(self, message_template_short:  Union[str, None]) -> AWSSESNotification:
        self.__message_template_short = message_template_short

        return self

    def get_message_template_short(self) ->  Union[str, None]:
        return self.__message_template_short

    def set_message_template_additional(self, message_template_additional:  Union[str, None]) -> AWSSESNotification:
        self.__message_template_additional = message_template_additional

        return self

    def get_message_template_additional(self) ->  Union[str, None]:
        return self.__message_template_additional

    @staticmethod
    def create(id: str, force_create: bool = False) -> MatrixNotification:
        ValueChecker.validate_id(id)

        notification = None if force_create else ConfigBuilder.get_notification(id)
        if None is notification:
            notification = MatrixNotification(id)
            ConfigBuilder.add_notification(id, notification)

        return notification

    def get_command_config(self) -> MatrixNotificationCommand:
        return MatrixNotificationCommand.create('matrix')

    def matrix_config_function(self, users: List[str]) -> List[str]:

        if None is self.__domain:
            raise Exception('Domain not set in ' + self.get_id())

        if None is self.__uri:
            raise Exception('URI not set in ' + self.get_id())


        config = [
            ValueMapper.parse_var('vars.notification_matrix_users', users) + '\n' +
            ValueMapper.parse_var('vars.notification_matrix_header', self.__header) + '\n' +
            ValueMapper.parse_var('vars.notification_matrix_uri', self.__uri) + '\n' +
            ValueMapper.parse_var('vars.notification_matrix_domain', self.__domain) + '\n' +
            ValueMapper.parse_var('vars.notification_matrix_port', self.__port) + '\n' +
            ValueMapper.parse_var('vars.notification_matrix_ssl', self.__ssl) + '\n' +
            ValueMapper.parse_var('vars.notification_matrix_client_cert', self.__client_cert) + '\n' +
            ValueMapper.parse_var('vars.notification_matrix_client_key', self.__client_key) + '\n' +
            ValueMapper.parse_var('vars.notification_matrix_timeout', self.__timeout) + '\n' +
            ValueMapper.parse_var('vars.notification_matrix_message_template_short',
                                  self.__message_template_short) + '\n' +
            ValueMapper.parse_var('vars.notification_matrix_message_template_additional',
                                  self.__message_template_additional) + '\n'
        ]
        return config

    def user_config_function(self, user: User) -> List[str]:
        if 0 == len(user.get_matrix_users()):
            return []

        return self.matrix_config_function(user.get_matrix_users())

    def group_config_function(self, group: UserGroup) -> List[str]:
        if 0 == len(group.get_matrix_users()):
            return []

        return self.matrix_config_function(group.get_matrix_users())

