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

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.User.User import User
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class ScheduledDowntime:

    def __init__(self, id):
        self.__id = id
        self.__comment = None
        self.__author = None
        self.__fixed = False
        self.__duration = None
        self.__child_options = None
        self.__ranges = []
        self.__type = None

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)

        period = None if force_create else ConfigBuilder.get_downtime(id)
        if None is period:
            period = ScheduledDowntime(id)
            ConfigBuilder.add_downtime(id, period)

        return period

    def get_id(self):
        return self.__id

    def set_comment(self, comment):
        ValueChecker.is_string(comment)
        self.__comment = comment
        return self

    def get_comment(self):
        return self.__comment

    def set_duration(self, duration):
        ValueChecker.is_string(duration)
        self.__duration = duration
        return self

    def get_duration(self):
        return self.__duration

    def set_author(self, author):

        if isinstance(author, User):
            self.__author = author.get_id()

        elif isinstance(author, str):
            if None is ConfigBuilder.get_user(author):
                raise Exception('User does not exist yet!')
            self.__author = author
        else:
            raise Exception('Can only add User or id of User!')

        return self

    def get_author(self):
        return self.__author

    def set_type(self, type):
        if type not in ['Service', 'Host']:
            raise Exception('Type must be Host or Service')
        self.__type = type
        return self

    def get_type(self):
        return self.__type

    def set_child_options(self, child_options):
        if child_options not in ['DowntimeNoChildren', 'DowntimeTriggeredChildren', 'DowntimeNonTriggeredChildren']:
            raise Exception(
                'child_options must be DowntimeNoChildren, DowntimeTriggeredChildren or DowntimeNonTriggeredChildren')
        self.__child_options = child_options
        return self

    def get_child_options(self):
        return self.__child_options

    def set_fixed(self, fixed):
        ValueChecker.is_bool(fixed)
        self.__fixed = fixed
        return self

    def get_fixed(self):
        return self.__fixed

    def add_period(self, day, range):
        ValueChecker.is_string(day)
        ValueChecker.is_string(range)
        self.__ranges.append((day, range))
        return self

    def remove_period(self, day, range):
        ValueChecker.is_string(day)
        ValueChecker.is_string(range)
        self.__ranges.remove((day, range))
        return self

    def validate(self):
        if None is self.__type:
            raise Exception('Type must be set for Downtime ' + self.__id)
        if None is self.__author:
            raise Exception('Author must be set for Downtime ' + self.__id)
        if None is self.__comment:
            raise Exception('Comment must be set for Downtime ' + self.__id)

    def get_config(self):

        config = 'apply ScheduledDowntime "downtime_' + self.__id + '" to ' + self.__type + '{\n'
        config += ValueMapper.parse_var('comment', self.__comment)
        config += ValueMapper.parse_var('author', self.__author)
        if None is not self.__duration and 'Service' == self.__type:
            # todo prüfen
            config += '  duration = "' + self.__duration + '"\n'
        if None is not self.__child_options:
            config += '  child_options = "' + self.__child_options + '"\n'

        config += ValueMapper.parse_var('fixed', self.__fixed)

        config += '  ranges = {\n'
        for range in self.__ranges:
            config += '    "' + range[0] + '" = "' + range[1] + '"\n'
        config += '  }\n'

        config += '  assign where "downtime_' + self.__id + '" in ' + self.__type.lower() + '.vars.' + self.__id + '\n'
        config += '}\n'

        return config
