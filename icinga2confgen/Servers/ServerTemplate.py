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

from icinga2confgen.Checks.Check import Check
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.HostGroup import HostGroup
from icinga2confgen.Helpers.Checkable import Checkable
from icinga2confgen.Helpers.CustomVars import CustomVars
from icinga2confgen.Helpers.PluginDirs import PluginDirs
from icinga2confgen.Helpers.ScriptDirs import ScriptDirs
from icinga2confgen.OS.OS import OS
from icinga2confgen.PackageManager.PackageManager import PackageManager
from icinga2confgen.Servers.SSHTemplate import SSHTemplate
from icinga2confgen.Servers.Zone import Zone
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class ServerTemplate(PluginDirs, ScriptDirs, Checkable, CustomVars):

    def __init__(self, id: str):
        CustomVars.__init__(self)
        PluginDirs.__init__(self)
        ScriptDirs.__init__(self)
        Checkable.__init__(self, is_check=False)
        self.__id = id
        self.__ipv4 = None
        self.__ipv6 = None
        self.__display_name = None
        self.__ssh_template = None
        self.__os = None
        self.__checks = []
        self.__templates = []
        self.__groups = []
        self.__package_manager = []
        self.__execution_zone = Zone.create('master')
        self.__execution_endpoint = None

    @staticmethod
    def create(id: str, force_create: bool = False) -> ServerTemplate:
        ValueChecker.validate_id(id)

        template = None if force_create else ConfigBuilder.get_template(id)
        if None is template:
            template = ServerTemplate(id)
            ConfigBuilder.add_template(id, template)

        return template

    def get_id(self) -> str:
        return self.__id

    def set_execution_zone(self, zone: Zone) -> ServerTemplate:
        self.__execution_zone = zone

        return self

    def get_execution_zone(self) -> Zone:
        return self.__execution_zone

    def set_execution_endpoint(self, endpoint: Union[str, None]) -> ServerTemplate:
        self.__execution_endpoint = endpoint
        return self

    def get_execution_endpoint(self) -> Union[str, None]:
        return self.__execution_endpoint

    def set_ipv4(self, ip: Union[str, None]) -> ServerTemplate:
        self.__ipv4 = ip
        return self

    def get_ipv4(self) -> Union[str, None]:
        return self.__ipv4

    def set_ipv6(self, ip: Union[str, None]) -> ServerTemplate:
        ValueChecker.is_string(ip)
        self.__ipv6 = ip
        return self

    def get_ipv6(self) -> Union[str, None]:
        return self.__ipv6

    def set_ssh_template(self, ssh_template: Union[SSHTemplate, None]) -> ServerTemplate:

        self.__ssh_template = ssh_template

        return self

    def get_ssh_template(self) -> Union[SSHTemplate, None]:

        return self.__ssh_template

    def set_os(self, os: Union[OS, None]) -> ServerTemplate:
        self.__os = os

        return self

    def get_os(self) -> Union[OS, None]:

        return self.__os

    def add_check(self, check: Check) -> ServerTemplate:
        if check not in self.__checks:
            self.__checks.append(check)

        return self

    def get_checks(self) -> List[Check]:

        return self.__checks

    def get_all_checks(self) -> List[Check]:
        checks = self.get_checks()
        for template in self.get_templates():
            checks += template.get_all_checks()

        return checks

    def remove_check(self, check: Check):
        if check in self.__checks:
            self.__checks.remove(check)

        return self

    def add_template(self, template: ServerTemplate) -> ServerTemplate:
        if template not in self.__templates:
            self.__templates.append(template)

        return self

    def remove_template(self, template: ServerTemplate) -> ServerTemplate:
        if template in self.__templates:
            self.__templates.remove(template.get_id())

        return self

    def get_templates(self) -> List[ServerTemplate]:

        return self.__templates

    def add_hostgroup(self, group: HostGroup) -> ServerTemplate:
        if group not in self.__groups:
            self.__groups.append(group)

        return self

    def get_hostgroups(self) -> List[HostGroup]:
        return self.__groups

    def get_hostgroups_recursive(self) -> List[HostGroup]:
        groups = self.__groups
        for template in self.__templates:
            groups += template.get_hostgroups_recursive()

        return groups

    def remove_hostgroup(self, group: HostGroup) -> ServerTemplate:
        if group in self.__groups:
            self.__groups.remove(group)

        return self

    def add_package_manager(self, package_manager: PackageManager) -> ServerTemplate:

        if package_manager not in self.__package_manager:
            self.__package_manager.append(package_manager)

        return self

    def remove_package_manager(self, package_manager: PackageManager) -> ServerTemplate:

        if package_manager in self.__package_manager:
            self.__package_manager.remove(package_manager)

        return self

    def get_package_managers(self) -> List[PackageManager]:
        return self.__package_manager


    def get_package_manager_recursive(self) -> List[PackageManager]:
        package_managers = self.__package_manager
        for template in self.__templates:
            package_managers += template.get_package_manager_recursive()

        return package_managers

    def get_config(self) -> str:
        config = 'template Host "servertemplate_' + self.__id + '" {\n'

        for template in self.__templates:
            config += '  import "servertemplate_' + template.get_id() + '"\n'

        if None is not self.__ssh_template:
            config += '  import "sshtemplate_' + self.__ssh_template.get_id() + '"\n'

        if None is not self.__os:
            config += '  import "os_' + self.__os.get_id() + '"\n'

        for manager in self.__package_manager:
            config += '  import "packagemanager_' + manager.get_id() + '"\n'

        config += Checkable.get_config(self)
        config += ValueMapper.parse_var('address', self.__ipv4)
        config += ValueMapper.parse_var('address6', self.__ipv6)
        config += ValueMapper.parse_var('vars.checks', self.__checks)
        config += ValueMapper.parse_var('vars.groups', self.__groups, value_prefix='hostgroup_')
        config += PluginDirs.get_config(self)
        config += ScriptDirs.get_config(self)
        config += CustomVars.get_config(self)

        config += '  check_command = "hostalive"\n'
        config += '  zone = "' + self.__execution_zone.get_id() + '"\n'
        config += ValueMapper.parse_var('vars.endpoint_name', self.__execution_endpoint)
        config += '}\n'

        return config
