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
import inspect


class ValueMapper:

    @staticmethod
    def get_property_default_config(instance, class_name, command_name, prefix):

        attributes = inspect.getmembers(instance, lambda a: not (inspect.isroutine(a)))
        properties = [a for a in attributes if (a[0].startswith('_' + class_name + '__'))]
        config = ''
        for property in properties:
            if None is property[1]:
                continue
            config += '  vars.' + property[0].replace(
                '_' + class_name + '__',
                prefix + '_' + command_name + '_'
            ) + ' = ' + ValueMapper.parse_value_for_var(property[1]) + '\n'

        return config

    @staticmethod
    def parse_var(key, value, ignore_none_value=True, value_prefix=''):
        if ignore_none_value and None is value:
            return ''
        if isinstance(value, list):
            if 0 == len(value):
                return ''
            return '  ' + key + ' += ' + ValueMapper.parse_value_for_var(value, value_prefix) + '\n'

        return '  ' + key + ' = ' + ValueMapper.parse_value_for_var(value, value_prefix) + '\n'

    @staticmethod
    def parse_value_for_var(value, value_prefix=''):
        if True is value:
            return 'true'
        elif False is value:
            return 'false'

        elif isinstance(value, str):
            return '"' + value_prefix + value + '"'

        elif isinstance(value, int):
            return str(value)

        elif isinstance(value, list):
            arr = '[\n'
            for a in value:
                arr += '    ' + ValueMapper.parse_value_for_var(a, value_prefix) + ',\n'
            arr += '  ]'
            return arr
        elif callable(getattr(value, 'get_id', None)):
            return ValueMapper.parse_value_for_var(value_prefix + value.get_id())

        raise Exception('Cannot parse value ' + value)

    @staticmethod
    def canonicalize_for_id(raw):
        allowed_chars = ['.', '_', '-']
        return ''.join(e for e in raw if e.isalnum() or e in allowed_chars)
