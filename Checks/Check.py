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

from ConfigBuilder import ConfigBuilder
from Downtimes.DefaultScheduledDowntimes import ScheduledDowntime
from Groups.ServiceGroup import ServiceGroup
from Notification.ServiceNotification import ServiceNotification
from ValueChecker import ValueChecker


class Check:

    def __init__(self, id, class_name, command_name):
        self.__command_name = command_name
        self.__class_name = class_name
        self.__display_name = None
        self.__id = id
        self.__service_groups = []
        self.__check_type = "local"
        self.__notifications = []
        self.__downtimes = []
        self.__allowed_check_types = ["local", "ssh"]
        self.__max_check_attempts = 3
        self.__check_interval = '1m'
        self.__retry_interval = '15s'
        self.__enable_perfdata = True

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)
        id = 'check_' + id
        check = ConfigBuilder.get_check(id)
        if None is check:
            check = Check(id, 'Check', 'check')
            ConfigBuilder.add_check(id, check)

        return check

    def add_service_group(self, group):
        if isinstance(group, ServiceGroup):
            self.__service_groups.append(group.get_id())
        elif isinstance(group, str):
            if None is ConfigBuilder.get_servicegroup(group):
                raise Exception('ServiceGroup does not exist yet!')
            self.__service_groups.append('servicegroup_' + group)
        else:
            raise Exception('Can only add Servicegroup or id of Servicegroup!')

        return self

    def add_notification(self, notification):
        if isinstance(notification, ServiceNotification):
            self.__notifications.append(notification.get_id())
        elif isinstance(notification, str):
            notification = ConfigBuilder.get_notification(notification)
            if None is notification:
                raise Exception('Notification does not exist yet!')
            if False is isinstance(notification, ServiceNotification):
                raise Exception('Can only add ServiceNotification or id of ServiceNotification!')

            self.__notifications.append(notification.get_id())
        else:
            raise Exception('Can only add ServiceNotification or id of ServiceNotification!')

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

    def get_service_group_ids(self):

        return self.__service_groups

    def get_id(self):
        return self.__id

    def set_check_type(self, type):
        if type in self.__allowed_check_types:
            self.__check_type = type
            return self
        raise Exception("Checktype must be " + ' or '.join(self.__allowed_check_types))

    def get_check_type(self):
        return self.__check_type
    
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

    def get_check_interval(self):
        return self.__check_interval

    def set_enable_perfdata(self, enable_perfdata):
        ValueChecker.is_bool(enable_perfdata)
        self.__enable_perfdata = enable_perfdata
        return self

    def get_retry_interval(self):
        return self.__retry_interval
    
    def set_display_name(self, display_name):
        ValueChecker.is_string(display_name)
        self.__display_name = display_name
        return self

    def get_display_name(self):
        return self.__display_name

    def get_custom_definitions(self):
        return []

    def get_config(self):

        config = 'apply Service "' + self.get_id() + '" {\n'
        config += '  check_command = "command_' + self.__command_name + '_' + self.__check_type + '"\n'
        config += self.get_property_default_config()
        config += self.get_custom_property_config()
        config += self.get_group_config()
        config += self.get_notification_config()
        config += self.get_downtime_config()
        config += self.get_check_config()
        config += '  assign where host.vars.' + self.get_id() + '\n'
        config += '}\n'

        return config

    def get_group_config(self):
        config = ''
        for group in self.__service_groups:
            config += '  vars.' + group + ' = true\n'

        return config

    def get_notification_config(self):
        config = ''
        for notification in self.__notifications:
            config += '  vars.' + notification + ' = true\n'

        return config

    def get_check_config(self):
        config = '  max_check_attempts = ' + str(self.__max_check_attempts) + '\n'
        config += '  check_interval = ' + self.__check_interval + '\n'
        config += '  retry_interval = ' + self.__retry_interval + '\n'
        if True is self.__enable_perfdata:
            config += '  enable_perfdata = true\n'
        else:
            config += '  enable_perfdata = false\n'

        if None is not self.__display_name:
            config += '  display_name = "' + self.__display_name + '"\n'

        return config

    def get_downtime_config(self):
        config = ''
        for downtime in self.__downtimes:
            config += '  vars.' + downtime + ' = true\n'

        return config

    def get_custom_property_config(self):
        config = ''
        for line in self.get_custom_definitions():
            config += '  ' + line + '\n'

        return config

    def get_property_default_config(self):

        return ConfigBuilder.get_property_default_config(self, self.__class_name, self.__command_name, 'command')
