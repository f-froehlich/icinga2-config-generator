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

from icinga2confgen.ValueChecker import ValueChecker


class Application:

    def __init__(self):
        self.__enable_notifications = True
        self.__enable_event_handlers = True
        self.__enable_flapping = True
        self.__enable_host_checks = True
        self.__enable_service_checks = True
        self.__enable_perfdata = True
        self.__vars = []
        self.__environment = ''

    @staticmethod
    def create():
        return Application()

    def set_enable_notifications(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__enable_notifications = enabled
        return self

    def get_enable_notifications(self):
        return self.__enable_notifications

    def set_enable_event_handlers(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__enable_event_handlers = enabled
        return self

    def get_enable_event_handlers(self):
        return self.__enable_event_handlers

    def set_enable_flapping(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__enable_flapping = enabled
        return self

    def get_enable_flapping(self):
        return self.__enable_flapping

    def set_enable_host_checks(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__enable_host_checks = enabled
        return self

    def get_enable_host_checks(self):
        return self.__enable_host_checks

    def set_enable_service_checks(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__enable_service_checks = enabled
        return self

    def get_enable_service_checks(self):
        return self.__enable_service_checks

    def set_enable_perfdata(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__enable_perfdata = enabled
        return self

    def get_enable_perfdata(self):
        return self.__enable_perfdata

    def set_environment(self, env):
        ValueChecker.is_string(env)
        self.__environment = env
        return self

    def get_environment(self):
        return self.__environment

    def add_var(self, key, value):
        ValueChecker.is_string(key)
        ValueChecker.is_string(value)
        self.__vars.append((key, value))
        return self

    def get_config(self):
        config = 'object IcingaApplication "app" {\n'

        if True is self.__enable_notifications:
            config += '  enable_notifications = true\n'
        else:
            config += '  enable_notifications = false\n'

        if True is self.__enable_event_handlers:
            config += '  enable_event_handlers = true\n'
        else:
            config += '  enable_event_handlers = false\n'

        if True is self.__enable_flapping:
            config += '  enable_flapping = true\n'
        else:
            config += '  enable_flapping = false\n'

        if True is self.__enable_host_checks:
            config += '  enable_host_checks = true\n'
        else:
            config += '  enable_host_checks = false\n'

        if True is self.__enable_service_checks:
            config += '  enable_service_checks = true\n'
        else:
            config += '  enable_service_checks = false\n'

        if True is self.__enable_perfdata:
            config += '  enable_perfdata = true\n'
        else:
            config += '  enable_perfdata = false\n'

        config += '  environment = "' + self.__environment + '"\n'

        for var in self.__vars:
            if isinstance(var[1], str):
                config += '  vars.' + var[0] + ' = "' + var[1] + '"\n'
            elif isinstance(var[1], bool) and var[1]:
                config += '  vars.' + var[0] + ' = true\n'
            elif isinstance(var[1], bool) and not var[1]:
                config += '  vars.' + var[0] + ' = false\n'
            elif isinstance(var[1], float) or isinstance(var[1], int):
                config += '  vars.' + var[0] + ' = ' + str(var[1]) + '\n'

            else:
                raise Exception('Value of given var "' + var[0] + '" is currently not supported.')

        config += '}\n'

        return config
