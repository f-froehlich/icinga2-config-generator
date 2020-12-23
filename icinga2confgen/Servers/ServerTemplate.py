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

    def __init__(self, id):
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
    def create(id, force_create=False):
        ValueChecker.validate_id(id)

        template = None if force_create else ConfigBuilder.get_template(id)
        if None is template:
            template = ServerTemplate(id)
            ConfigBuilder.add_template(id, template)

        return template

    def get_id(self):
        return self.__id

    def set_execution_zone(self, zone):
        if isinstance(zone, Zone):
            self.__execution_zone = zone

        elif isinstance(zone, str):
            zone = ConfigBuilder.get_zone(zone)
            if None is zone:
                raise Exception('Zone does not exist yet!')
            self.__execution_zone = zone
        else:
            raise Exception('Can only add Zone or id of Zone!')

        return self

    def get_execution_zone(self):
        return self.__execution_zone

    def set_execution_endpoint(self, endpoint):
        ValueChecker.is_string(endpoint)
        self.__execution_endpoint = endpoint
        return self

    def get_execution_endpoint(self):
        return self.__execution_endpoint

    def set_ipv4(self, ip):
        ValueChecker.is_string(ip)
        self.__ipv4 = ip
        return self

    def get_ipv4(self):
        return self.__ipv4

    def set_ipv6(self, ip):
        ValueChecker.is_string(ip)
        self.__ipv6 = ip
        return self

    def get_ipv6(self):
        return self.__ipv6

    def set_ssh_template(self, ssh_template):

        if isinstance(ssh_template, SSHTemplate):
            self.__ssh_template = ssh_template

        elif isinstance(ssh_template, str):
            ssh_template = ConfigBuilder.get_ssh_template(ssh_template)
            if None is ssh_template:
                raise Exception('SSHTemplate does not exist yet!')
            self.__ssh_template = ssh_template
        else:
            raise Exception('Can only add SSHTemplate or id of SSHTemplate!')

        return self

    def get_ssh_template(self):

        return self.__ssh_template

    def set_os(self, os):

        if isinstance(os, OS):
            self.__os = os

        elif isinstance(os, str):
            os = ConfigBuilder.get_os(os)
            if None is os:
                raise Exception('OS does not exist yet!')
            self.__os = os
        else:
            raise Exception('Can only add OS or id of OS!')

        return self

    def get_os(self):

        return self.__os

    def add_check(self, check):
        if isinstance(check, Check):
            if check not in self.__checks:
                self.__checks.append(check)

        elif isinstance(check, str):
            check = ConfigBuilder.get_check(check)
            if None is check:
                raise Exception('Check does not exist yet!')
            self.add_check(check)
        else:
            raise Exception('Can only add Check or id of Check!')

        return self

    def get_check(self):

        return self.__checks

    def remove_check(self, check):
        if isinstance(check, Check):
            self.__checks.remove(check)

        elif isinstance(check, str):
            check = ConfigBuilder.get_check(check)
            self.__checks.remove(check)

        return self

    def add_template(self, template):
        if isinstance(template, ServerTemplate):
            if template not in self.__templates:
                self.__templates.append(template)

        elif isinstance(template, str):
            template = ConfigBuilder.get_template(template)
            if None is template:
                raise Exception('ServerTemplate does not exist yet!')
            self.add_template(template)
        else:
            raise Exception('Can only add ServerTemplate or id of ServerTemplate!')

        return self

    def remove_template(self, template):
        if isinstance(template, ServerTemplate):
            self.__templates.remove(template.get_id())
        elif isinstance(template, str):
            template = ConfigBuilder.get_template(template)
            self.__templates.remove(template)

        return self

    def get_templates(self):

        return self.__templates

    def add_hostgroup(self, group):
        if isinstance(group, HostGroup):
            if group not in self.__groups:
                self.__groups.append(group)
        elif isinstance(group, str):
            group = ConfigBuilder.get_hostgroup(group)
            if None is group:
                raise Exception('HostGroup does not exist yet!')
            self.add_hostgroup(group)
        else:
            raise Exception('Can only add HostGroup or id of HostGroup!')

        return self

    def get_hostgroups(self):
        return self.__groups

    def get_hostgroups_recursive(self):
        groups = self.__groups
        for template in self.__templates:
            groups += template.get_hostgroups()

        return groups

    def remove_hostgroup(self, group):
        if isinstance(group, HostGroup):
            self.__groups.remove(group)
        elif isinstance(group, str):
            group = ConfigBuilder.get_hostgroup(group)
            self.__groups.remove(group)

        return self

    def add_package_manager(self, package_manager):

        if isinstance(package_manager, PackageManager):
            if package_manager not in self.__package_manager:
                self.__package_manager.append(package_manager)

        elif isinstance(package_manager, str):
            package_manager = ConfigBuilder.get_package_manager(package_manager)
            if None is package_manager:
                raise Exception('PackageManager does not exist yet!')
            self.add_package_manager(package_manager)
        else:
            raise Exception('Can only add PackageManager or id of PackageManager!')

        return self

    def remove_package_manager(self, package_manager):

        if isinstance(package_manager, PackageManager):
            self.__package_manager.remove(package_manager)

        elif isinstance(package_manager, str):
            package_manager = ConfigBuilder.get_package_manager(package_manager)
            self.__package_manager.remove(package_manager)

        return self

    def get_package_managers(self):
        return self.__package_manager

    def get_config(self):
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
