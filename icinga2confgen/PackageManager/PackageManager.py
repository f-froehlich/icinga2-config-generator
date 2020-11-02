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
from icinga2confgen.ValueChecker import ValueChecker


class PackageManager:

    def __init__(self, id):
        self.__id = id
        self.__manager = None

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)

        pm = None if force_create else ConfigBuilder.get_package_manager(id)
        if None is pm:
            pm = PackageManager(id)
            ConfigBuilder.add_package_manager(id, pm)

        return pm

    def get_id(self):
        return self.__id

    def set_manager(self, manager):
        ValueChecker.is_string(manager)
        self.__manager = manager
        return self

    def get_manager(self):
        return self.__manager

    def validate(self):
        if None is self.__manager:
            raise Exception('You have to specify Manager for ' + self.get_id())

    def get_config(self):
        self.validate()

        config = 'template Host "packagemanager_' + self.__id + '" {\n'
        config += '  vars.package_manager += ["' + self.__id + '"]\n'
        config += '}\n'

        return config


def apt(): return PackageManager.create('apt').set_manager('apt')


def yum(): return PackageManager.create('yum').set_manager('yum')


def apk(): return PackageManager.create('apk').set_manager('apk')


def rpm(): return PackageManager.create('rpm').set_manager('rpm')


def dpkg(): return PackageManager.create('dpkg').set_manager('dpkg')
