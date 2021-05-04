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
from typing import Union

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueMapper import ValueMapper

T = typing.TypeVar('T', bound='CheckSNMP')


class CheckSNMP(Check):

    def __init__(self: T, id: str, class_name: str, var_name: str):
        Check.__init__(self, id, class_name, var_name)
        self.__username: Union[str, None] = None
        self.__password: Union[str, None] = None
        self.__host: Union[str, None] = None
        self.__version: Union[str, None] = '3'
        self.__community: Union[str, None] = None
        self.__timeout: int = 30
        self.set_timeout(self.__timeout)
        self.add_service_group(ServiceGroup.create('snmp'))

    def set_username(self: T, username: str) -> T:
        self.__username = username
        return self

    def get_username(self: T) -> Union[str, None]:
        return self.__username

    def set_password(self: T, password: str) -> T:
        self.__password = password
        return self

    def get_password(self: T) -> Union[str, None]:
        return self.__password

    def set_version(self: T, version: str) -> T:
        if version not in ['1', '2c', '3']:
            raise Exception('Version must be 1, 2c or 3')

        self.__version = version
        return self

    def get_version(self: T) -> Union[str, None]:
        return self.__version

    def set_community(self: T, community: str) -> T:

        self.__community = community
        return self

    def get_community(self: T) -> Union[str, None]:
        return self.__community

    def set_host(self: T, host: str) -> T:
        self.__host = host
        return self

    def get_host(self: T) -> Union[str, None]:
        return self.__host

    def set_timeout(self: T, timeout: int) -> T:
        self.__timeout = timeout
        self.set_check_timeout(timeout + 1)
        return self

    def get_timeout(self: T) -> int:
        return self.__timeout

    def validate(self: T):
        if None is self.__host:
            raise Exception('Host must be set on ' + self.get_id())
        if '3' == self.__version or None is self.__version:
            if None is self.__username:
                raise Exception('Username must be set on ' + self.get_id())
            if None is self.__password:
                raise Exception('Password must be set on ' + self.get_id())
        elif '2c' == self.__version:
            if None is self.__community:
                raise Exception('Community must be set on ' + self.get_id())

    def get_custom_config(self: T) -> str:
        return ValueMapper.get_property_default_config(self, 'CheckSNMP', 'snmp', 'command')
