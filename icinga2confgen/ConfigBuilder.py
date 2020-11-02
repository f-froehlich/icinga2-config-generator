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

import shutil
from pathlib import Path

from tqdm import tqdm

from icinga2confgen.Application.Application import Application
from icinga2confgen.ValueChecker import ValueChecker


class ConfigBuilder:
    __servers = []
    __checks = []
    __templates = []
    __commands = []
    __notification_commands = []
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
    __package_manager = []
    __application = Application.create()
    __pbar = tqdm(desc="Configuring", unit=' Configs')
    __check_for_existence = True

    @staticmethod
    def set_check_for_existence(enabled):
        ConfigBuilder.__check_for_existence = enabled

    @staticmethod
    def replace_prefixes(string):

        for prefix in ValueChecker.get_prefixes():
            if string.startswith(prefix + '_'):
                return string.replace(prefix + '_', '', 1)
        return string

    @staticmethod
    def get_config():
        ConfigBuilder.__pbar.close()

        shutil.rmtree('zones.d', ignore_errors=True)

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
            {'dir': 'notifications/commands', 'config': ConfigBuilder.__notification_commands},
            {'dir': 'downtimes', 'config': ConfigBuilder.__downtimes},
            {'dir': 'os', 'config': ConfigBuilder.__os},
            {'dir': 'package_manager', 'config': ConfigBuilder.__package_manager},
        ]

        total = len(ConfigBuilder.__servers)
        for config in global_configs:
            total += len(config['config'])

        pbar = tqdm(total=total, desc="Writing config", unit=' Configs')

        for config in global_configs:
            dirpath = "zones.d/global-templates/" + config['dir']
            for conf in config['config']:
                Path(dirpath).mkdir(parents=True, exist_ok=True)
                with open(dirpath + '/' + ConfigBuilder.replace_prefixes(conf['id']) + '.conf', "w") as file:
                    file.write(conf['instance'].get_config())
                pbar.update(1)

        for conf in ConfigBuilder.__servers:
            server = conf['instance']
            zone = server.get_zone()
            dirpath = 'zones.d/' + ConfigBuilder.replace_prefixes(zone.get_id()) + '/'

            Path(dirpath).mkdir(parents=True, exist_ok=True)
            with open(dirpath + '/' + ConfigBuilder.replace_prefixes(conf['id']) + '.conf', "w") as file:
                file.write(server.get_config())
            pbar.update(1)

        with open('zones.d/application.conf', "w") as file:
            file.write(ConfigBuilder.__application.get_config())
            pbar.update(1)

        pbar.close()

    @staticmethod
    def get_hosts_with_hostgroup(group):
        servers_with_group = []
        for server in ConfigBuilder.__servers:
            if group in server.get_hostgroups():
                servers_with_group.append(server)

        return servers_with_group

    @staticmethod
    def get_checks_from_server(server):
        all_checks = server.get_checks()
        for template in server.get_templates():
            all_checks += ConfigBuilder.get_checks_from_server(template)

        return all_checks

    @staticmethod
    def get_instance(type):

        config = {
            'server': ConfigBuilder.__servers,
            'checks': ConfigBuilder.__checks,
            'templates': ConfigBuilder.__templates,
            'commands': ConfigBuilder.__commands,
            'vhosts': ConfigBuilder.__vhosts,
            'servicegroups': ConfigBuilder.__servicegroups,
            'hostgroups': ConfigBuilder.__hostgroups,
            'usergroups': ConfigBuilder.__usergroups,
            'users': ConfigBuilder.__users,
            'sshtemplates': ConfigBuilder.__ssh_templates,
            'time_periods': ConfigBuilder.__time_periods,
            'notification_templates': ConfigBuilder.__notification_templates,
            'notification_commands': ConfigBuilder.__notification_commands,
            'notifications': ConfigBuilder.__notifications,
            'downtimes': ConfigBuilder.__downtimes,
            'os': ConfigBuilder.__os,
            'package_manager': ConfigBuilder.__package_manager
        }

        instances_config = config[type]
        instances = []

        for config in instances_config:
            instances.append(config['instance'])

        return instances

    @staticmethod
    def get_server(id):
        for server in ConfigBuilder.__servers:
            if server['id'] == id:
                return server['instance']

        return None

    @staticmethod
    def add_server(id, server):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_check(id):
            raise Exception('Server with id ' + id + ' already exists!')

        ConfigBuilder.__servers.append({'id': id, 'instance': server})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_check(id):

        for check in ConfigBuilder.__checks:
            if check['id'] == id:
                return check['instance']

        return None

    @staticmethod
    def add_check(id, check):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_check(id):
            raise Exception('Check with id ' + id + ' already exists!')

        ConfigBuilder.__checks.append({'id': id, 'instance': check})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_template(id):
        for template in ConfigBuilder.__templates:
            if template['id'] == id:
                return template['instance']

        return None

    @staticmethod
    def add_template(id, template):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_template(id):
            raise Exception('Template with id ' + id + ' already exists!')

        ConfigBuilder.__templates.append({'id': id, 'instance': template})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_command(id):
        for command in ConfigBuilder.__commands:
            if command['id'] == id:
                return command['instance']

        return None

    @staticmethod
    def add_command(id, command):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_command(id):
            raise Exception('Command with id ' + id + ' already exists!')

        ConfigBuilder.__commands.append({'id': id, 'instance': command})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_notification_command(id):
        for notification_command in ConfigBuilder.__notification_commands:
            if notification_command['id'] == id:
                return notification_command['instance']

        return None

    @staticmethod
    def add_notification_command(id, notification_command):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_notification_command(id):
            raise Exception('NotificationCommand with id ' + id + ' already exists!')

        ConfigBuilder.__notification_commands.append({'id': id, 'instance': notification_command})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_vhost(id):
        for vhost in ConfigBuilder.__vhosts:
            if vhost['id'] == id:
                return vhost['instance']

        return None

    @staticmethod
    def add_vhost(id, vhost):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_vhost(id):
            raise Exception('vHost with id ' + id + ' already exists!')

        ConfigBuilder.__vhosts.append({'id': id, 'instance': vhost})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_hostgroup(id):
        for group in ConfigBuilder.__hostgroups:
            if group['id'] == id:
                return group['instance']

        return None

    @staticmethod
    def add_hostgroup(id, group):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_hostgroup(id):
            raise Exception('Hostgroup with id ' + id + ' already exists!')

        ConfigBuilder.__hostgroups.append({'id': id, 'instance': group})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_usergroup(id):
        for group in ConfigBuilder.__usergroups:
            if group['id'] == id:
                return group['instance']

        return None

    @staticmethod
    def add_usergroup(id, group):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_usergroup(id):
            raise Exception('Usergroup with id ' + id + ' already exists!')

        ConfigBuilder.__usergroups.append({'id': id, 'instance': group})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_servicegroup(id):
        for group in ConfigBuilder.__servicegroups:
            if group['id'] == id:
                return group['instance']

        return None

    @staticmethod
    def add_servicegroup(id, group):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_servicegroup(id):
            raise Exception('Servicegroup with id ' + id + ' already exists!')

        ConfigBuilder.__servicegroups.append({'id': id, 'instance': group})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_ssh_template(id):
        for template in ConfigBuilder.__ssh_templates:
            if template['id'] == id:
                return template['instance']

        return None

    @staticmethod
    def add_ssh_template(id, group):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_ssh_template(id):
            raise Exception('SSH Template with id ' + id + ' already exists!')

        ConfigBuilder.__ssh_templates.append({'id': id, 'instance': group})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_time_period(id):
        for period in ConfigBuilder.__time_periods:
            if period['id'] == id:
                return period['instance']

        return None

    @staticmethod
    def add_time_period(id, period):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_time_period(id):
            raise Exception('Time Period with id ' + id + ' already exists!')

        ConfigBuilder.__time_periods.append({'id': id, 'instance': period})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_notification_template(id):
        for template in ConfigBuilder.__notification_templates:
            if template['id'] == id:
                return template['instance']

        return None

    @staticmethod
    def add_notification_template(id, period):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_notification_template(id):
            raise Exception('Notification Template with id ' + id + ' already exists!')

        ConfigBuilder.__notification_templates.append({'id': id, 'instance': period})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_notification(id):
        id = 'notification_' + id
        for notification in ConfigBuilder.__notifications:
            if ['id'] == id:
                return notification['instance']

        return None

    @staticmethod
    def add_notification(id, period):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_notification(id):
            raise Exception('Notification with id ' + id + ' already exists!')

        ConfigBuilder.__notifications.append({'id': id, 'instance': period})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_user(id):
        for user in ConfigBuilder.__users:
            if user['id'] == id:
                return user['instance']

        return None

    @staticmethod
    def add_user(id, user):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_user(id):
            raise Exception('user with id ' + id + ' already exists!')

        ConfigBuilder.__users.append({'id': id, 'instance': user})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_downtime(id):
        for period in ConfigBuilder.__downtimes:
            if period['id'] == id:
                return period['instance']

        return None

    @staticmethod
    def add_downtime(id, period):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_downtime(id):
            raise Exception('Downtime with id ' + id + ' already exists!')

        ConfigBuilder.__downtimes.append({'id': id, 'instance': period})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_application():
        return ConfigBuilder.__application

    @staticmethod
    def set_application(application):
        if not isinstance(application, Application):
            raise Exception('Can only set Application')

        ConfigBuilder.__application = application
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_zone(id):
        for period in ConfigBuilder.__zones:
            if period['id'] == id:
                return period['instance']

        return None

    @staticmethod
    def add_zone(id, period):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_zone(id):
            raise Exception('Zone with id ' + id + ' already exists!')

        ConfigBuilder.__zones.append({'id': id, 'instance': period})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_os(id):
        for period in ConfigBuilder.__os:
            if period['id'] == id:
                return period['instance']

        return None

    @staticmethod
    def add_os(id, os):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_os(id):
            raise Exception('os with id ' + id + ' already exists!')

        ConfigBuilder.__os.append({'id': id, 'instance': os})
        ConfigBuilder.__pbar.update(1)

    @staticmethod
    def get_package_manager(id):
        for period in ConfigBuilder.__package_manager:
            if period['id'] == id:
                return period['instance']

        return None

    @staticmethod
    def add_package_manager(id, package_manager):
        if ConfigBuilder.__check_for_existence and None is not ConfigBuilder.get_package_manager(id):
            raise Exception('package_manager with id ' + id + ' already exists!')

        ConfigBuilder.__package_manager.append({'id': id, 'instance': package_manager})
        ConfigBuilder.__pbar.update(1)
