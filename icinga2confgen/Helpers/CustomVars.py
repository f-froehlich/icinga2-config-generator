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

from icinga2confgen.ValueMapper import ValueMapper


class CustomVars:

    def __init__(self):
        self.__custom_vars = []

    def add_custom_var(self, key, value):
        # todo check allowed values
        # todo check key
        self.__custom_vars.append({'key': key, 'value': value})
        return self

    def remove_custom_var(self, key):
        vars = self.__custom_vars
        self.__custom_vars = []
        for var in vars:
            if var['key'] != key:
                self.__custom_vars.append(var)
        return self

    def get_custom_var(self, key):
        for var in self.__custom_vars:
            if var['key'] == key:
                return var['value']

        last_value = None

        for template in self.get_templates():
            if None is not template and callable(getattr(template, 'get_custom_var', None)):
                new_value = template.get_custom_var(key)
                if None is not new_value:
                    last_value = new_value

        return last_value

    def get_custom_vars(self):
        vars = []

        for template in self.get_templates():
            if None is not template and callable(getattr(template, 'get_custom_vars', None)):
                new_vars = template.get_custom_vars()
                for new_var in new_vars:
                    for var in vars:
                        if new_var['key'] == var['key']:
                            vars.remove(var)
                    vars.append(new_var)

        for new_var in self.__custom_vars:
            for var in vars:
                if new_var['key'] == var['key']:
                    vars.remove(var)
            vars.append(new_var)

        return vars

    def get_config(self):
        config = ''

        for custom_var in self.__custom_vars:
            config += ValueMapper.parse_var('vars.' + custom_var['key'], custom_var['value'])

        return config

    def get_templates(self):
        return []
