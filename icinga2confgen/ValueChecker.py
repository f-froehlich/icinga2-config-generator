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

class ValueChecker:

    @staticmethod
    def get_prefixes():

        return [
            'server',
            'check',
            'template',
            'command',
            'vhost',
            'servicegroup',
            'hostgroup',
            'usergroup',
            'user',
            'ssh_template',
            'time_period',
            'notification_template',
            'notification',
            'downtime',
            'zone',
            'os',
            'package_manager',
        ]

    @staticmethod
    def validate_id(id):
        prefixes = ValueChecker.get_prefixes()

        for prefix in prefixes:
            if id.startswith(prefix + '_'):
                raise Exception(prefix + '_ is a reserved Prefix. You can\'t use it!')

        if ValueMapper.canonicalize_for_id(id) != id:
            raise Exception('Id\'s can only contains letters (a-z,A-Z), numbers (0-9) and underscore (_)')

    @staticmethod
    def is_bool(id):
        if not isinstance(id, bool):
            raise Exception('Given value is not boolean!')

    @staticmethod
    def is_number(id):
        if not isinstance(id, int) and not isinstance(id, float):
            raise Exception('Given value is not a number!')

    @staticmethod
    def is_string(id):
        if not isinstance(id, str):
            raise Exception('Given value is not a string!')

    @staticmethod
    def is_array(id):
        if not isinstance(id, list):
            raise Exception('Given value is not a list!')

    @staticmethod
    def is_http_method(id):
        if id not in ['GET', 'PUT', 'POST', 'DELETE', 'HEAD', 'OPTIONS', 'TRACE', 'CONNECT', 'PATCH']:
            raise Exception('Given value is not a HTTP method!')
