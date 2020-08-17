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

from ConfigBuilder import ConfigBuilder
from Notification.NotificationTemplate import NotificationTemplate
from ValueChecker import ValueChecker


class ServiceNotification(NotificationTemplate):

    def __init__(self, id):
        self.__id = id
        self.__allowed_types = ['DowntimeStart', 'DowntimeEnd', 'DowntimeRemoved', 'Custom', 'Acknowledgement',
                                'Problem', 'Recovery', 'FlappingStart', 'FlappingEnd']
        self.__allowed_states = ['Warning', 'Critical', 'Unknown', 'OK']
        NotificationTemplate.__init__(self, 'template_' + id)

    def get_allowed_states(self):
        return self.__allowed_states

    def get_allowed_types(self):
        return self.__allowed_types

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)

        notification = ConfigBuilder.get_notification_template(id)
        if None is notification:
            id = 'notification_' + id
            notification = ServiceNotification(id)
            ConfigBuilder.add_notification_template(id, notification)

        return notification

    def get_id(self):
        return self.__id

    def get_config(self):
        config = NotificationTemplate.get_config(self)
        config += 'apply Notification "' + self.__id + '" to Service {\n'
        config += '  import "' + NotificationTemplate.get_id(self) + '"\n'
        config += '  assign where service.vars.' + self.__id + ' == true\n'
        config += '}\n'

        return config
