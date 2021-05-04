#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, commands, checks, ... in python
#
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
from __future__ import annotations

import typing
from ctypes import Union
from typing import List, Tuple

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.User.User import User
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper

T = typing.TypeVar('T', bound='ScheduledDowntime')


class ScheduledDowntime:

    def __init__(self: T, id: str):
        self.__id = id
        self.__comment: Union[str, None] = None
        self.__author: Union[User, None] = None
        self.__fixed: bool = False
        self.__duration: Union[str, None] = None
        self.__child_options: Union[str, None] = None
        self.__ranges: List[Tuple[str, str]] = []

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)

        period = None if force_create else ConfigBuilder.get_downtime(id)
        if None is period:
            period = ScheduledDowntime(id)
            ConfigBuilder.add_downtime(id, period)

        return period

    def get_id(self: T) -> str:
        return self.__id

    def set_comment(self: T, comment: str) -> T:
        self.__comment = comment
        return self

    def get_comment(self: T) -> Union[str, None]:
        return self.__comment

    def set_duration(self: T, duration: str) -> T:
        self.__duration = duration
        return self

    def get_duration(self: T) -> Union[str, None]:
        return self.__duration

    def set_author(self: T, author: Union[User, str]) -> T:

        if isinstance(author, User):
            self.__author = author

        elif isinstance(author, str):
            author = ConfigBuilder.get_user(author)
            if None is author:
                raise Exception('User does not exist yet!')
            self.__author = author
        else:
            raise Exception('Can only add User or id of User!')

        return self

    def get_author(self: T) -> Union[User, None]:
        return self.__author

    def set_child_options(self: T, child_options: str) -> T:
        if child_options not in ['DowntimeNoChildren', 'DowntimeTriggeredChildren', 'DowntimeNonTriggeredChildren']:
            raise Exception(
                'child_options must be DowntimeNoChildren, DowntimeTriggeredChildren or DowntimeNonTriggeredChildren')
        self.__child_options = child_options
        return self

    def get_child_options(self: T) -> Union[str, None]:
        return self.__child_options

    def set_fixed(self: T, fixed: bool) -> T:
        self.__fixed = fixed
        return self

    def get_fixed(self: T) -> bool:
        return self.__fixed

    def add_period(self: T, day: str, range: str) -> T:
        self.__ranges.append((day, range))
        return self

    def remove_period(self: T, day: str, range: str) -> T:
        if (day, range) in self.__ranges:
            self.__ranges.remove((day, range))
        return self

    def get_periods(self: T) -> List[Tuple[str, str]]:
        return self.__ranges

    def validate(self: T):
        if None is self.__author:
            raise Exception('Author must be set for Downtime ' + self.__id)
        if None is self.__comment:
            raise Exception('Comment must be set for Downtime ' + self.__id)

    def get_config(self: T) -> str:
        self.validate()
        config = ''
        for type in ['Host', 'Service']:

            config += 'apply ScheduledDowntime "downtime_' + self.__id + '" to ' + type + '{\n'
            config += ValueMapper.parse_var('comment', self.__comment)
            config += ValueMapper.parse_var('author', self.__author)
            config += ValueMapper.parse_var('child_options', self.__child_options)
            config += ValueMapper.parse_var('fixed', self.__fixed)
            if None is not self.__duration:
                config += '  duration = ' + self.__duration + '\n'

            if 0 < len(self.__ranges):
                config += '  ranges = {\n'
                for range in self.__ranges:
                    config += '    "' + range[0] + '" = "' + range[1] + '"\n'
                config += '  }\n'

            config += '  assign where "downtime_' + self.__id + '" in ' + type.lower() + '.vars.downtime\n'
            config += '}\n'

        return config
