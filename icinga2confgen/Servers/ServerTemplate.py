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
from icinga2confgen.Downtimes.ScheduledDowntime import ScheduledDowntime
from icinga2confgen.Groups.HostGroup import HostGroup
from icinga2confgen.Notification.Notification import Notification
from icinga2confgen.OS.OS import OS
from icinga2confgen.PackageManager.PackageManager import PackageManager
from icinga2confgen.Servers.SSHTemplate import SSHTemplate
from icinga2confgen.Servers.VHost import VHost
from icinga2confgen.Servers.Zone import Zone
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class ServerTemplate:

    def __init__(self, id):
        self.__id = id
        self.__ipv4 = None
        self.__ipv6 = None
        self.__display_name = None
        self.__ssh_template = None
        self.__os = None
        self.__checks = []
        self.__vhosts = []
        self.__templates = []
        self.__custom_vars = []
        self.__groups = []
        self.__notifications = []
        self.__downtimes = []
        self.__package_manager = []
        self.__plugin_dir = '/usr/lib/nagios/plugins/'
        self.__max_check_attempts = 3
        self.__check_interval = '1m'
        self.__retry_interval = '15s'
        self.__enable_perfdata = True
        self.__execution_zone = Zone.create('master')

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

    def set_plugindir(self, dir):
        ValueChecker.is_string(dir)
        self.__plugin_dir = dir
        return self

    def get_plugindir(self):
        return self.__plugin_dir

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
        return self.__plugin_dir

    def set_max_check_attempts(self, max_check_attempts):
        ValueChecker.is_number(max_check_attempts)
        self.__max_check_attempts = max_check_attempts
        return self

    def get_max_check_attempts(self):
        return self.__max_check_attempts

    def set_check_interval(self, check_interval):
        ValueChecker.is_string(check_interval)
        self.__check_interval = check_interval
        return self

    def get_check_interval(self):
        return self.__check_interval

    def set_retry_interval(self, retry_interval):
        ValueChecker.is_string(retry_interval)
        self.__retry_interval = retry_interval
        return self

    def get_retry_interval(self):
        return self.__retry_interval

    def set_enable_perfdata(self, enable_perfdata):
        ValueChecker.is_bool(enable_perfdata)
        self.__enable_perfdata = enable_perfdata
        return self

    def get_enable_perfdata(self):
        return self.__enable_perfdata

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

    def get_display_name(self):
        return self.__display_name

    def set_display_name(self, name):
        ValueChecker.is_string(name)
        self.__display_name = name
        return self

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

    def add_downtime(self, downtime):
        if isinstance(downtime, ScheduledDowntime):
            self.__downtimes.append(downtime)
        elif isinstance(downtime, str):
            downtime = ConfigBuilder.get_downtime(downtime)
            if None is downtime:
                raise Exception('Downtime does not exist yet!')
            self.__downtimes.append(downtime)
        else:
            raise Exception('Can only add Downtime or id of Downtime!')

        return self

    def remove_downtime(self, downtime):
        if isinstance(downtime, ScheduledDowntime):
            self.__downtimes.remove(downtime.get_id())
        elif isinstance(downtime, str):
            self.__downtimes.remove('downtime_' + downtime)

        return self

    def get_ssh_template(self):
        return self.__ssh_template

    def add_notification(self, notification):
        if isinstance(notification, Notification):
            self.__notifications.append(notification)
        elif isinstance(notification, str):
            notification = ConfigBuilder.get_notification(notification)
            if None is notification:
                raise Exception('Notification does not exist yet!')

            self.__notifications.append(notification)
        else:
            raise Exception('Can only add Notification or id of Notification!')

        return self

    def remove_notification(self, notification):

        if isinstance(notification, HostNotification):
            self.__notifications.remove(notification)

        elif isinstance(notification, str):
            notification = ConfigBuilder.get_notification(notification)
            self.__notifications.remove(notification)

        return self

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

    def add_checks(self):

        return self.__checks

    def remove_check(self, check):
        if isinstance(check, Check):
            self.__checks.remove(check)

        elif isinstance(check, str):
            check = ConfigBuilder.get_check(check)
            self.__checks.remove(check)

        return self

    def get_check_ids(self):

        return self.__checks

    def add_vhost(self, vhost):
        if isinstance(vhost, VHost):
            if vhost not in self.__vhosts:
                self.__vhosts.append(vhost)

        elif isinstance(vhost, str):
            vhost = ConfigBuilder.get_vhost(vhost)
            if None is vhost:
                raise Exception('VHost does not exist yet')

            self.add_vhost(vhost)

        else:
            raise Exception('Can only add VHost or id of VHost!')

        return self

    def remove_vhost(self, vhost):
        if isinstance(vhost, VHost):
            self.__vhosts.remove(vhost)

        elif isinstance(vhost, str):
            vhost = ConfigBuilder.get_vhost(vhost)
            self.__vhosts.remove(vhost)

        return self

    def get_vhost_ids(self):

        return self.__vhosts

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
            raise Exception('Can only add Hostgroup or id of Hostgroup!')

        return self

    def get_hostgroups(self):
        return self.__groups

    def remove_hostgroup(self, group):
        if isinstance(group, HostGroup):
            self.__groups.remove(group)
        elif isinstance(group, str):
            group = ConfigBuilder.get_hostgroup(group)
            self.__groups.remove(group)
        else:
            raise Exception('Can only add Hostgroup or id of Hostgroup!')

        return self

    def add_custom_var(self, key, value):
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

        for template in self.__templates:
            if None is not template:
                new_value = template.get_custom_var(key)
                if None is not new_value:
                    last_value = new_value

        return last_value

    def append_package_manager(self, package_manager):

        if isinstance(package_manager, PackageManager):
            if package_manager not in self.__package_manager:
                self.__package_manager.append(package_manager)

        elif isinstance(package_manager, str):
            package_manager = ConfigBuilder.get_package_manager(package_manager)
            if None is package_manager:
                raise Exception('PackageManager does not exist yet!')
            self.append_package_manager(package_manager)
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

    def get_config(self):
        config = 'template Host "servertemplate_' + self.__id + '" {\n'

        for template in self.__templates:
            config += '  import "servertemplate_' + template.get_id() + '"\n'

        for vhost in self.__vhosts:
            config += '  import "vhost_' + vhost.get_id() + '"\n'

        if None is not self.__ssh_template:
            config += '  import "sshtemplate_' + self.__ssh_template.get_id() + '"\n'

        if None is not self.__os:
            config += '  import "os_' + self.__os.get_id() + '"\n'

        for manager in self.__package_manager:
            config += '  import "packagemanager_' + manager.get_id() + '"\n'

        config += '  check_interval = ' + self.__check_interval + '\n'
        config += '  retry_interval = ' + self.__retry_interval + '\n'
        config += ValueMapper.parse_var('vars.notification', self.__notifications, value_prefix='notification_')
        config += ValueMapper.parse_var('vars.downtime', self.__downtimes, value_prefix='downtime_')
        config += ValueMapper.parse_var('address', self.__ipv4)
        config += ValueMapper.parse_var('address6', self.__ipv6)
        config += ValueMapper.parse_var('display_name', self.__display_name)
        config += ValueMapper.parse_var('max_check_attempts', self.__max_check_attempts)
        config += ValueMapper.parse_var('enable_perfdata', self.__enable_perfdata)
        config += ValueMapper.parse_var('vars.plugin_dir', self.__plugin_dir)
        config += ValueMapper.parse_var('vars.checks', self.__checks, value_prefix='check_')
        config += ValueMapper.parse_var('groups', self.__groups, value_prefix='hostgroup_')

        for custom_var in self.__custom_vars:
            config += '  vars.' + custom_var['key'] + ' = ' + ValueMapper.parse_value_for_var(
                custom_var['value']) + '\n'

        config += '  check_command = "hostalive"\n'
        config += '  zone = "' + self.__execution_zone.get_id() + '"\n'
        config += '}\n'

        return config
