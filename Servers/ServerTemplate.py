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

from Checks.Check import Check
from ConfigBuilder import ConfigBuilder
from Groups.HostGroup import HostGroup
from Servers.SSHTemplate import SSHTemplate
from Servers.VHost import VHost
from ValueChecker import ValueChecker


class ServerTemplate:

    def __init__(self, id):
        self.__id = id
        self.__ipv4 = None
        self.__ipv6 = None
        self.__name = None
        self.__display_name = None
        self.__description = None
        self.__state = None
        self.__state_id = None
        self.__state_type = None
        self.__check_attempt = None
        self.__max_check_attempts = None
        self.__last_state = None
        self.__last_state_id = None
        self.__last_state_type = None
        self.__last_state_change = None
        self.__downtime_depth = None
        self.__duration_sec = None
        self.__latency = None
        self.__execution_time = None
        self.__output = None
        self.__perfdata = None
        self.__last_check = None
        self.__check_source = None
        self.__num_services = None
        self.__num_services_ok = None
        self.__num_services_warning = None
        self.__num_services_unknown = None
        self.__num_services_critical = None
        self.__ssh_template = None
        self.__checks = []
        self.__vhosts = []
        self.__templates = []
        self.__custom_vars = []
        self.__groups = []

    @staticmethod
    def create(id):
        ConfigBuilder.validate_id(id)

        template = ConfigBuilder.get_template(id)
        if None is template:
            id = 'template_' + id
            template = ServerTemplate(id)
            ConfigBuilder.add_template(id, template)

        return template

    def get_id(self):
        return self.__id

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
            self.__ssh_template = ssh_template
        else:
            raise Exception('Can only add Check or id of Check!')

        return self

    def get_ssh_template(self):
        return self.__ssh_template

    def set_state(self, state):
        ValueChecker.check_state(state)
        self.__state = state
        return self

    def get_state(self):
        return self.__state

    def set_state_id(self, state_id):
        ValueChecker.check_state_id(state_id)
        self.__state_id = state_id
        return self

    def get_state_id(self):
        return self.__state_id

    def set_state_type(self, state_type):
        ValueChecker.check_state_id(state_type)
        self.__state_type = state_type
        return self

    def get_state_type(self):
        return self.__state_type

    def set_check_attempt(self, check_attempt):
        ValueChecker.is_number(check_attempt)
        self.__check_attempt = check_attempt
        return self

    def get_check_attempt(self):
        return self.__check_attempt

    def set_max_check_attempts(self, max_check_attempts):
        ValueChecker.is_number(max_check_attempts)
        self.__max_check_attempts = max_check_attempts
        return self

    def get_max_check_attempts(self):
        return self.__max_check_attempts

    def set_last_state(self, last_state):
        ValueChecker.check_state(last_state)
        self.__last_state = last_state
        return self

    def get_last_state(self):
        return self.__last_state

    def set_last_state_id(self, last_state_id):
        ValueChecker.check_state_id(last_state_id)
        self.__last_state_id = last_state_id
        return self

    def get_last_state_id(self):
        return self.__last_state_id

    def set_last_state_type(self, last_state_type):
        ValueChecker.check_state_type(last_state_type)
        self.__last_state_type = last_state_type
        return self

    def get_last_state_type(self):
        return self.__last_state_type

    def set_last_state_change(self, last_state_change):
        ValueChecker.check_timestamp(last_state_change)
        self.__last_state_change = last_state_change
        return self

    def get_last_state_change(self):
        return self.__last_state_change

    def set_downtime_depth(self, downtime_depth):
        ValueChecker.is_number(downtime_depth)
        self.__downtime_depth = downtime_depth
        return self

    def get_downtime_depth(self):
        return self.__downtime_depth

    def set_duration_sec(self, duration_sec):
        ValueChecker.is_number(duration_sec)
        self.__duration_sec = duration_sec
        return self

    def get_duration_sec(self):
        return self.__duration_sec

    def set_latency(self, latency):
        ValueChecker.check_latency(latency)
        self.__latency = latency
        return self

    def get_latency(self):
        return self.__latency

    def set_execution_time(self, execution_time):
        ValueChecker.is_number(execution_time)
        self.__execution_time = execution_time
        return self

    def get_execution_time(self):
        return self.__execution_time

    def set_output(self, output):
        ValueChecker.is_string(output)
        self.__output = output
        return self

    def get_output(self):
        return self.__output

    def set_perfdata(self, perfdata):
        ValueChecker.check_perfdata(perfdata)
        self.__perfdata = perfdata
        return self

    def get_perfdata(self):
        return self.__perfdata

    def set_last_check(self, last_check):
        ValueChecker.check_timestamp(last_check)
        self.__last_check = last_check
        return self

    def get_last_check(self):
        return self.__last_check

    def set_check_source(self, check_source):
        ValueChecker.is_string(check_source)  # todo right?
        self.__check_source = check_source
        return self

    def get_check_source(self):
        return self.__check_source

    def set_num_services(self, num_services):
        ValueChecker.is_number(num_services)
        self.__num_services = num_services
        return self

    def get_num_services(self):
        return self.__num_services

    def set_num_services_ok(self, num_services_ok):
        ValueChecker.is_number(num_services_ok)
        self.__num_services_ok = num_services_ok
        return self

    def get_num_services_ok(self):
        return self.__num_services_ok

    def set_num_services_warning(self, num_services_warning):
        ValueChecker.is_number(num_services_warning)
        self.__num_services_warning = num_services_warning
        return self

    def get_num_services_warning(self):
        return self.__num_services_warning

    def set_num_services_unknown(self, num_services_unknown):
        ValueChecker.is_number(num_services_unknown)
        self.__num_services_unknown = num_services_unknown
        return self

    def get_num_services_unknown(self):
        return self.__num_services_unknown

    def set_num_services_critical(self, num_services_critical):
        ValueChecker.is_number(num_services_critical)
        self.__num_services_critical = num_services_critical
        return self

    def add_check(self, check):
        if isinstance(check, Check):
            self.__checks.append(check.get_id())

        elif isinstance(check, str):
            self.__checks.append(check)  # todo check if Check exist
        else:
            raise Exception('Can only add Check or id of Check!')

        return self

    def get_check_ids(self):

        return self.__checks

    def add_vhost(self, vhost):
        if isinstance(vhost, VHost):
            self.__vhosts.append(vhost.get_id())

        elif isinstance(vhost, str):
            vhost = ConfigBuilder.get_vhost(vhost)
            if None is vhost:
                raise Exception('VHost does not exist yet')

            self.__vhosts.append(vhost.get_id())

        else:
            raise Exception('Can only add VHost or id of VHost!')

        return self

    def get_vhost_ids(self):

        return self.__vhosts

    def add_template(self, template):
        if isinstance(template, ServerTemplate):
            self.__templates.append(template.get_id())
        elif isinstance(template, str):
            self.__templates.append('template_' + template)
        else:
            raise Exception('Can only add Template or id of Template!')

        return self

    def get_template_ids(self):

        return self.__templates

    def add_hostgroup(self, group):
        if isinstance(group, HostGroup):
            self.__groups.append(group.get_id())
        elif isinstance(group, str):
            self.__groups.append('hostgroup_' + group)
        else:
            raise Exception('Can only add Hostgroup or id of Hostgroup!')

        return self

    def get_hostgroup_ids(self):

        return self.__groups

    def add_custom_var(self, key, value):

        return self.__custom_vars.append({'key': key, 'value': value})

    def get_config(self):
        config = 'template Host "' + self.__id + '" {\n'

        for template in self.__templates:
            config += '  import "' + template + '"\n'

        for vhost in self.__vhosts:
            config += '  import "' + vhost + '"\n'

        if None is not self.__ssh_template:
            config += '  import "' + self.__ssh_template + '"\n'

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

        if None is not self.__state_id:
            config += '  state_id = "' + self.__state_id + '"\n'

        if None is not self.__state_type:
            config += '  state_type = "' + self.__state_type + '"\n'

        if None is not self.__check_attempt:
            config += '  check_attempt = "' + self.__check_attempt + '"\n'

        if None is not self.__max_check_attempts:
            config += '  max_check_attempts = "' + self.__max_check_attempts + '"\n'

        if None is not self.__last_state:
            config += '  __last_state = "' + self.__last_state + '"\n'

        if None is not self.__last_state_id:
            config += '  __last_state_id = "' + self.__last_state_id + '"\n'

        if None is not self.__last_state_type:
            config += '  __last_state_type = "' + self.__last_state_type + '"\n'

        if None is not self.__last_state_change:
            config += '  __last_state_change = "' + self.__last_state_change + '"\n'

        if None is not self.__duration_sec:
            config += '  __duration_sec = "' + self.__duration_sec + '"\n'

        if None is not self.__latency:
            config += '  __latency = "' + self.__latency + '"\n'

        if None is not self.__execution_time:
            config += '  __execution_time = "' + self.__execution_time + '"\n'

        if None is not self.__output:
            config += '  __output = "' + self.__output + '"\n'

        if None is not self.__perfdata:
            config += '  __perfdata = "' + self.__perfdata + '"\n'

        if None is not self.__last_check:
            config += '  __last_check = "' + self.__last_check + '"\n'

        if None is not self.__check_source:
            config += '  __check_source = "' + self.__check_source + '"\n'

        if None is not self.__num_services:
            config += '  __num_services = "' + self.__num_services + '"\n'

        if None is not self.__num_services_ok:
            config += '  __num_services_ok = "' + self.__num_services_ok + '"\n'

        if None is not self.__num_services_warning:
            config += '  __num_services_warning = "' + self.__num_services_warning + '"\n'

        if None is not self.__num_services_unknown:
            config += '  __num_services_unknown = "' + self.__num_services_unknown + '"\n'

        if None is not self.__num_services_critical:
            config += '  __num_services_critical = "' + self.__num_services_critical + '"\n'

        for check in self.__checks:
            config += '  vars.' + check + ' = true\n'

        for group in self.__groups:
            config += '  vars.' + group + ' = true\n'

        for custom_var in self.__custom_vars:
            config += '  vars.' + custom_var['key'] + ' = ' + custom_var['value'] + '\n'

        config += '  check_command = "hostalive"\n'
        config += '}\n'

        return config
