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

from __future__ import annotations

from typing import Union, List

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.HostGroup import HostGroup
from icinga2confgen.PackageManager.PackageManager import PackageManager
from icinga2confgen.ValueChecker import ValueChecker


class OS:

    def __init__(self, id: str):
        self.__id = id
        self.__os = None
        self.__distro = None
        self.__version = None
        self.__package_manager = []

    @staticmethod
    def create(id: str, force_create: bool = False) -> OS:
        ValueChecker.validate_id(id)

        os = None if force_create else ConfigBuilder.get_os(id)
        if None is os:
            os = OS(id)
            ConfigBuilder.add_os(id, os)

        return os

    def get_id(self) -> str:
        return self.__id

    def set_os(self, os: str) -> OS:
        ValueChecker.is_string(os)
        HostGroup.create('hg_os_' + self.__id).set_display_name(os.capitalize())
        self.__os = os
        return self

    def get_os(self) -> Union[str, None]:
        return self.__os

    def add_package_manager(self, package_manager: PackageManager) -> OS:

        if package_manager not in self.__package_manager:
            self.__package_manager.append(package_manager)

        return self

    def remove_package_manager(self, package_manager: PackageManager) -> OS:

        if package_manager in self.__package_manager:
            self.__package_manager.remove(package_manager)

        return self

    def get_package_manager(self) -> List[PackageManager]:
        return self.__package_manager

    def set_version(self, version: str) -> OS:
        self.__version = version
        return self

    def get_version(self) -> Union[str, None]:
        return self.__version

    def set_distro(self, distro: str) -> OS:
        HostGroup.create('hg_distro_' + distro).set_display_name(distro.capitalize())
        self.__distro = distro
        return self

    def get_distro(self) -> Union[str, None]:
        return self.__distro

    def validate(self):
        if None is self.__os:
            raise Exception('You have to specify OS for ' + self.get_id())
        if None is self.__version:
            raise Exception('You have to specify Version for ' + self.get_id())
        if None is self.__distro:
            raise Exception('You have to specify distro for ' + self.get_id())

    def get_config(self) -> str:
        self.validate()

        config = 'template Host "os_' + self.__id + '" {\n'
        for manager in self.__package_manager:
            config += '  import "packagemanager_' + manager.get_id() + '"\n'
        config += '  vars.os = "' + self.__os + '"\n'
        config += '  vars.version = "' + self.__version + '"\n'
        config += '  vars.distro = "' + self.__distro + '"\n'
        config += '  groups += ["hostgroup_hg_os_' + self.__id + '", "hostgroup_hg_distro_' + self.__distro + '"]\n'
        config += '}\n'

        return config
