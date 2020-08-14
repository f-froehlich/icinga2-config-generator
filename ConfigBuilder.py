#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, commands, checks, ... in python
#
#  Copyright (c) 2020 Fabian Fröhlich <mail@f-froehlich.de> https://f-froehlich.de
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

    @staticmethod
    def get_config():
        config = ""
        for template in ConfigBuilder.__templates:
            config += template['instance'].get_config()

        for command in ConfigBuilder.__commands:
            config += command['instance'].get_config()

        for check in ConfigBuilder.__checks:
            config += check['instance'].get_config()

        for vhost in ConfigBuilder.__vhosts:
            config += vhost['instance'].get_config()

        for server in ConfigBuilder.__servers:
            config += server['instance'].get_config()

        for group in ConfigBuilder.__hostgroups:
            config += group['instance'].get_config()

        for group in ConfigBuilder.__servicegroups:
            config += group['instance'].get_config()

        for group in ConfigBuilder.__usergroups:
            config += group['instance'].get_config()

        return config

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
    def validate_id(id):
        # TODO

        return True

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
