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
import shutil
from pathlib import Path

from Application.Application import Application
from ValueChecker import ValueChecker


class ConfigBuilder:
    __servers = []
    __checks = []
    __templates = []
    __commands = []
    __vhosts = []
    __hostgroups = []
    __servicegroups = []
    __usergroups = []
    __ssh_templates = []
    __time_periods = []
    __notification_templates = []
    __notifications = []
    __users = []
    __downtimes = []
    __zones = []
    __os = []
    __application = Application.create()

    @staticmethod
    def replace_prefixes(string):

        for prefix in ValueChecker.get_prefixes():
            if string.startswith(prefix + '_'):
                return string.replace(prefix + '_', '', 1)
        return string

    @staticmethod
    def get_config():
        shutil.rmtree('zones.d')
        config = ConfigBuilder.__application.get_config()

        global_configs = [
            {'dir': 'checks', 'config': ConfigBuilder.__checks},
            {'dir': 'templates', 'config': ConfigBuilder.__templates},
            {'dir': 'commands', 'config': ConfigBuilder.__commands},
            {'dir': 'vhosts', 'config': ConfigBuilder.__vhosts},
            {'dir': 'groups/servicegroups', 'config': ConfigBuilder.__servicegroups},
            {'dir': 'groups/hostgroups', 'config': ConfigBuilder.__hostgroups},
            {'dir': 'groups/usergroups', 'config': ConfigBuilder.__usergroups},
            {'dir': 'users', 'config': ConfigBuilder.__users},
            {'dir': 'ssh_templates', 'config': ConfigBuilder.__ssh_templates},
            {'dir': 'time_periods', 'config': ConfigBuilder.__time_periods},
            {'dir': 'notifications/templates', 'config': ConfigBuilder.__notification_templates},
            {'dir': 'notifications/notifications', 'config': ConfigBuilder.__notifications},
            {'dir': 'ssh_templates', 'config': ConfigBuilder.__ssh_templates},
            {'dir': 'downtimes', 'config': ConfigBuilder.__downtimes},
            {'dir': 'os', 'config': ConfigBuilder.__os},
        ]

        for config in global_configs:
            dirpath = "zones.d/global-templates/" + config['dir']
            for conf in config['config']:
                Path(dirpath).mkdir(parents=True, exist_ok=True)
                with open(dirpath + '/' + ConfigBuilder.replace_prefixes(conf['id']) + '.conf', "w") as file:
                    file.write(conf['instance'].get_config())

        for conf in ConfigBuilder.__servers:
            server = conf['instance']
            zone = server.get_zone()
            dirpath = 'zones.d/' + ConfigBuilder.replace_prefixes(zone.get_id()) + '/'

            Path(dirpath).mkdir(parents=True, exist_ok=True)
            with open(dirpath + '/' + ConfigBuilder.replace_prefixes(conf['id']) + '.conf', "w") as file:
                file.write(server.get_config())

        with open('zones.d/application.conf', "w") as file:
            file.write(ConfigBuilder.__application.get_config())


    @staticmethod
    def get_property_default_config(instance, class_name, command_name, prefix):

        attributes = inspect.getmembers(instance, lambda a: not (inspect.isroutine(a)))
        properties = [a for a in attributes if (a[0].startswith('_' + class_name + '__'))]
        config = ''
        for property in properties:
            if True is property[1]:
                config += '  vars.' + property[0].replace('_' + class_name + '__', prefix + '_' + \
                                                          command_name + '_') + ' = true\n'
            elif False is property[1]:
                config += '  vars.' + property[0].replace('_' + class_name + '__', prefix + '_' + \
                                                          command_name + '_') + ' = false\n'
            elif isinstance(property[1], str):
                config += '  vars.' + property[0].replace('_' + class_name + '__', prefix + '_' + \
                                                          command_name + '_') + ' = "' + property[1] + '"\n'
            elif isinstance(property[1], int):
                config += '  vars.' + property[0].replace('_' + class_name + '__', prefix + '_' + \
                                                          command_name + '_') + ' = ' + str(property[1]) + '\n'
            elif isinstance(property[1], list):
                arr = '['
                for a in property[1]:
                    arr += '"' + a + '", '
                arr += ']'
                config += '  vars.' + property[0].replace('_' + class_name + '__', prefix + '_' + \
                                                          command_name + '_') + ' = ' + arr + '\n'

        return config

    @staticmethod
    def get_server(id):
        id = 'server_' + id
        for server in ConfigBuilder.__servers:
            if server['id'] == id:
                return server['instance']

        return None

    @staticmethod
    def add_server(id, server):
        if None is not ConfigBuilder.get_check(id):
            raise Exception('Server with id ' + id + ' already exists!')

        ConfigBuilder.__servers.append({'id': id, 'instance': server})

    @staticmethod
    def get_check(id):
        id = 'check_' + id
        for check in ConfigBuilder.__checks:
            if check['id'] == id:
                return check['instance']

        return None

    @staticmethod
    def add_check(id, check):
        if None is not ConfigBuilder.get_check(id):
            raise Exception('Check with id ' + id + ' already exists!')

        ConfigBuilder.__checks.append({'id': id, 'instance': check})

    @staticmethod
    def get_template(id):
        id = 'template_' + id
        for template in ConfigBuilder.__templates:
            if template['id'] == id:
                return template['instance']

        return None

    @staticmethod
    def add_template(id, template):
        if None is not ConfigBuilder.get_template(id):
            raise Exception('Template with id ' + id + ' already exists!')

        ConfigBuilder.__templates.append({'id': id, 'instance': template})

    @staticmethod
    def get_command(id):
        id = 'command_' + id
        for command in ConfigBuilder.__commands:
            if command['id'] == id:
                return command['instance']

        return None

    @staticmethod
    def add_command(id, command):
        if None is not ConfigBuilder.get_command(id):
            raise Exception('Command with id ' + id + ' already exists!')

        ConfigBuilder.__commands.append({'id': id, 'instance': command})

    @staticmethod
    def get_vhost(id):
        id = 'vhost_' + id
        for vhost in ConfigBuilder.__vhosts:
            if vhost['id'] == id:
                return vhost['instance']

        return None

    @staticmethod
    def add_vhost(id, vhost):
        if None is not ConfigBuilder.get_vhost(id):
            raise Exception('vHost with id ' + id + ' already exists!')

        ConfigBuilder.__vhosts.append({'id': id, 'instance': vhost})

    @staticmethod
    def get_hostgroup(id):
        id = 'hostgroup_' + id
        for group in ConfigBuilder.__hostgroups:
            if group['id'] == id:
                return group['instance']

        return None

    @staticmethod
    def add_hostgroup(id, group):
        if None is not ConfigBuilder.get_hostgroup(id):
            raise Exception('Hostgroup with id ' + id + ' already exists!')

        ConfigBuilder.__hostgroups.append({'id': id, 'instance': group})

    @staticmethod
    def get_usergroup(id):
        id = 'usergroup_' + id
        for group in ConfigBuilder.__usergroups:
            if group['id'] == id:
                return group['instance']

        return None

    @staticmethod
    def add_usergroup(id, group):
        if None is not ConfigBuilder.get_usergroup(id):
            raise Exception('Usergroup with id ' + id + ' already exists!')

        ConfigBuilder.__usergroups.append({'id': id, 'instance': group})

    @staticmethod
    def get_servicegroup(id):
        id = 'servicegroup_' + id
        for group in ConfigBuilder.__servicegroups:
            if group['id'] == id:
                return group['instance']

        return None

    @staticmethod
    def add_servicegroup(id, group):
        if None is not ConfigBuilder.get_servicegroup(id):
            raise Exception('Servicegroup with id ' + id + ' already exists!')

        ConfigBuilder.__servicegroups.append({'id': id, 'instance': group})

    @staticmethod
    def get_ssh_template(id):
        id = 'ssh_template_' + id
        for template in ConfigBuilder.__ssh_templates:
            if template['id'] == id:
                return template['instance']

        return None

    @staticmethod
    def add_ssh_template(id, group):
        if None is not ConfigBuilder.get_ssh_template(id):
            raise Exception('SSH Template with id ' + id + ' already exists!')

        ConfigBuilder.__ssh_templates.append({'id': id, 'instance': group})

    @staticmethod
    def get_time_period(id):
        id = 'time_period_' + id
        for period in ConfigBuilder.__time_periods:
            if period['id'] == id:
                return period['instance']

        return None

    @staticmethod
    def add_time_period(id, period):
        if None is not ConfigBuilder.get_time_period(id):
            raise Exception('Time Period with id ' + id + ' already exists!')

        ConfigBuilder.__time_periods.append({'id': id, 'instance': period})

    @staticmethod
    def get_notification_template(id):
        id = 'notification_' + id
        for template in ConfigBuilder.__notification_templates:
            if template['id'] == id:
                return template['instance']

        return None

    @staticmethod
    def add_notification_template(id, period):
        if None is not ConfigBuilder.get_notification_template(id):
            raise Exception('Notification Template with id ' + id + ' already exists!')

        ConfigBuilder.__notification_templates.append({'id': id, 'instance': period})

    @staticmethod
    def get_notification(id):
        id = 'notification_' + id
        for notification in ConfigBuilder.__notifications:
            if ['id'] == id:
                return notification['instance']

        return None

    @staticmethod
    def add_notification_(id, period):
        if None is not ConfigBuilder.get_notification(id):
            raise Exception('Notification with id ' + id + ' already exists!')

        ConfigBuilder.__notifications.append({'id': id, 'instance': period})

    @staticmethod
    def get_user(id):
        id = 'user_' + id
        for period in ConfigBuilder.__users:
            if period['id'] == id:
                return period['instance']

        return None

    @staticmethod
    def add_user(id, period):
        if None is not ConfigBuilder.get_user(id):
            raise Exception('user with id ' + id + ' already exists!')

        ConfigBuilder.__users.append({'id': id, 'instance': period})

    @staticmethod
    def get_downtime(id):
        id = 'downtime_' + id
        for period in ConfigBuilder.__downtimes:
            if period['id'] == id:
                return period['instance']

        return None

    @staticmethod
    def add_downtime(id, period):
        if None is not ConfigBuilder.get_downtime(id):
            raise Exception('Downtime with id ' + id + ' already exists!')

        ConfigBuilder.__downtimes.append({'id': id, 'instance': period})

    @staticmethod
    def get_application():
        return ConfigBuilder.__application

    @staticmethod
    def set_application(application):
        if not isinstance(application, Application):
            raise Exception('Can only set Application')
        ConfigBuilder.__application = application

    @staticmethod
    def get_zone(id):
        id = 'zone_' + id
        for period in ConfigBuilder.__zones:
            if period['id'] == id:
                return period['instance']

        return None

    @staticmethod
    def add_zone(id, period):
        if None is not ConfigBuilder.get_zone(id):
            raise Exception('Zone with id ' + id + ' already exists!')

        ConfigBuilder.__zones.append({'id': id, 'instance': period})
    @staticmethod
    def get_os(id):
        id = 'os_' + id
        for period in ConfigBuilder.__os:
            if period['id'] == id:
                return period['instance']

        return None

    @staticmethod
    def add_os(id, os):
        if None is not ConfigBuilder.get_os(id):
            raise Exception('os with id ' + id + ' already exists!')

        ConfigBuilder.__os.append({'id': id, 'instance': os})
