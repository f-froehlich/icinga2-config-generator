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

from Checks.Check import Check
from ConfigBuilder import ConfigBuilder
from Downtimes.ScheduledDowntime import ScheduledDowntime
from Groups.HostGroup import HostGroup
from Notification.HostNotification import HostNotification
from Servers.SSHTemplate import SSHTemplate
from Servers.VHost import VHost
from ValueChecker import ValueChecker
from OS.OS import OS


class ServerTemplate:

    def __init__(self, id):
        self.__id = id
        self.__ipv4 = None
        self.__ipv6 = None
        self.__name = None
        self.__display_name = None
        self.__description = None
        self.__ssh_template = None
        self.__os = None
        self.__checks = []
        self.__vhosts = []
        self.__templates = []
        self.__custom_vars = []
        self.__groups = []
        self.__notifications = []
        self.__downtimes = []
        self.__plugin_dir = '/usr/lib/nagios/plugins/'
        self.__max_check_attempts = 3
        self.__check_interval = '1m'
        self.__retry_interval = '15s'
        self.__enable_perfdata = True

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)

        template = ConfigBuilder.get_template(id)
        if None is template:
            id = 'template_' + id
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

    def set_name(self, name):
        ValueChecker.is_string(name)
        self.__name = name
        return self

    def get_display_name(self):
        return self.__display_name

    def set_display_name(self, name):
        ValueChecker.is_string(name)
        self.__display_name = name
        return self

    def set_description(self, description):
        ValueChecker.is_string(description)
        self.__description = description
        return self

    def get_description(self):
        return self.__description

    def set_ssh_template(self, ssh_template):

        if isinstance(ssh_template, SSHTemplate):
            self.__ssh_template = ssh_template.get_id()

        elif isinstance(ssh_template, str):
            if None is ConfigBuilder.get_ssh_template(ssh_template):
                raise Exception('SSHTemplate does not exist yet!')
            self.__ssh_template = ssh_template
        else:
            raise Exception('Can only add SSHTemplate or id of SSHTemplate!')

        return self
    
    
    def set_os(self, os):

        if isinstance(os, OS):
            self.__os = os.get_id()

        elif isinstance(os, str):
            if None is ConfigBuilder.get_os(os):
                raise Exception('OS does not exist yet!')
            self.__os = os
        else:
            raise Exception('Can only add OS or id of OS!')

        return self

    def add_downtime(self, downtime):
        if isinstance(downtime, ScheduledDowntime):
            self.__downtimes.append(downtime.get_id())
        elif isinstance(downtime, str):
            if None is ConfigBuilder.get_downtime(downtime):
                raise Exception('Downtime does not exist yet!')
            self.__downtimes.append(downtime)
        else:
            raise Exception('Can only add Downtime or id of Downtime!')

        return self

    def get_ssh_template(self):
        return self.__ssh_template

    def add_notification(self, notification):

        if isinstance(notification, HostNotification):
            self.__notifications.append(notification.get_id())

        elif isinstance(notification, str):

            notification = ConfigBuilder.get_notification(notification)
            if None is notification:
                raise Exception('Notification not exist yet!')
            elif not isinstance(notification, HostNotification):
                raise Exception('Given Notification is not a HostNotification!')

            self.__notifications.append(notification)
        else:
            raise Exception('Can only add HostNotification or id of HostNotification!')

        return self

    def add_check(self, check):
        if isinstance(check, Check):
            self.__checks.append(check.get_id())

        elif isinstance(check, str):

            if None is ConfigBuilder.get_check(check):
                raise Exception('Check does not exist yet!')
            self.__checks.append(check)
        else:
            raise Exception('Can only add Check or id of Check!')

        return self

    def get_check_ids(self):

        return self.__checks

    def add_vhost(self, vhost):
        if isinstance(vhost, VHost):
            self.__vhosts.append(vhost.get_id())

        elif isinstance(vhost, str):
            if None is ConfigBuilder.get_vhost(vhost):
                raise Exception('VHost does not exist yet')

            self.__vhosts.append(vhost)

        else:
            raise Exception('Can only add VHost or id of VHost!')

        return self

    def get_vhost_ids(self):

        return self.__vhosts

    def add_template(self, template):
        if isinstance(template, ServerTemplate):
            self.__templates.append(template.get_id())
        elif isinstance(template, str):
            if None is ConfigBuilder.get_template(template):
                raise Exception('ServerTemplate does not exist yet!')
            self.__templates.append('template_' + template)
        else:
            raise Exception('Can only add ServerTemplate or id of ServerTemplate!')

        return self

    def get_template_ids(self):

        return self.__templates

    def add_hostgroup(self, group):
        if isinstance(group, HostGroup):
            self.__groups.append(group.get_id())
        elif isinstance(group, str):
            if None is ConfigBuilder.get_hostgroup(group):
                raise Exception('HostGroup does not exist yet!')
            self.__groups.append('hostgroup_' + group)
        else:
            raise Exception('Can only add Hostgroup or id of Hostgroup!')

        return self

    def get_hostgroup_ids(self):

        return self.__groups

    def add_custom_var(self, key, value):
        self.__custom_vars.append({'key': key, 'value': value})
        return self

    def get_custom_var(self, key):

        for var in self.__custom_vars:
            if var['key'] == key:
                return var['value']

        last_value = None

        for template_id in self.__templates:
            template = ConfigBuilder.get_template(template_id.replace('template_', ''))
            if None is not template:
                new_value = template.get_custom_var(key)
                if None is not new_value:
                    last_value = new_value

        return last_value

    def get_config(self):
        config = 'template Host "' + self.__id + '" {\n'

        for template in self.__templates:
            config += '  import "' + template + '"\n'

        for vhost in self.__vhosts:
            config += '  import "' + vhost + '"\n'

        for notification in self.__notifications:
            config += '  vars.' + notification + ' = true\n'

        for downtime in self.__downtimes:
            config += '  vars.' + downtime + ' = true\n'

        if None is not self.__ssh_template:
            config += '  import "' + self.__ssh_template + '"\n'

        if None is not self.__os:
            config += '  import "' + self.__os + '"\n'

        if None is not self.__ipv4:
            config += '  address = "' + self.__ipv4 + '"\n'
            config += '  vars.address = "' + self.__ipv4 + '"\n'

        if None is not self.__ipv6:
            config += '  address6 = "' + self.__ipv6 + '"\n'
            config += '  vars.address6 = "' + self.__ipv6 + '"\n'

        if None is not self.__name:
            config += '  name = "' + self.__name + '"\n'

        if None is not self.__display_name:
            config += '  display_name = "' + self.__display_name + '"\n'

        if None is not self.__description:
            config += '  description = "' + self.__description + '"\n'

        config += '  max_check_attempts = ' + str(self.__max_check_attempts) + '\n'
        config += '  check_interval = ' + self.__check_interval + '\n'
        config += '  retry_interval = ' + self.__retry_interval + '\n'
        if True is self.__enable_perfdata:
            config += '  enable_perfdata = true\n'
        else:
            config += '  enable_perfdata = false\n'

        config += '  vars.plugin_dir = "' + self.__plugin_dir + '"\n'

        for check in self.__checks:
            config += '  vars.' + check + ' = true\n'

        for group in self.__groups:
            config += '  vars.' + group + ' = true\n'

        for custom_var in self.__custom_vars:
            # todo check for string, int, bool
            config += '  vars.' + custom_var['key'] + ' = "' + custom_var['value'] + '"\n'

        config += '  check_command = "hostalive"\n'
        config += '}\n'

        return config
