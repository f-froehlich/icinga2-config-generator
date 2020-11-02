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

from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.Utils.DefaultLocalChecks import DefaultLocalChecks
from icinga2confgen.ValueChecker import ValueChecker


class DefaultLocalMailserverChecks(DefaultLocalChecks):

    def __init__(self, servers=[], notifications=[], sudoers=[], additional_users=[]):
        DefaultLocalChecks.__init__(self, servers, notifications, sudoers, additional_users)
        self.__check_amavisd_running = True
        self.__check_dovecot_running = True
        self.__check_postgrey_running = True
        self.__check_opendkim_running = True
        self.__inherit = True
        DefaultLocalChecks.check_freshclam_running(self, True)
        DefaultLocalChecks.check_clamd_running(self, True)
        DefaultLocalChecks.check_postfix_running(self, True)

    def set_inherit(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__inherit = enabled

        return self

    def is_inherit(self):
        return self.__inherit

    def check_amavisd_running(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__check_amavisd_running = enabled

        return self

    def is_checking_amavisd_running(self):
        return self.__check_amavisd_running

    def check_dovecot_running(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__check_dovecot_running = enabled

        return self

    def is_checking_dovecot_running(self):
        return self.__check_dovecot_running

    def check_postgrey_running(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__check_postgrey_running = enabled

        return self

    def is_checking_postgrey_running(self):
        return self.__check_postgrey_running

    def check_opendkim_running(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__check_opendkim_running = enabled

        return self

    def is_checking_opendkim_running(self):
        return self.__check_opendkim_running

    def apply(self):
        if self.__inherit:
            DefaultLocalChecks.apply(self)

        for server in DefaultLocalChecks.get_server(self):
            if True is self.__check_amavisd_running:
                check = self.create_running_check_arguments('amavisd', 'amavisd', server)
                check.add_service_group(ServiceGroup.create('mail'))

            if True is self.__check_dovecot_running:
                check = self.create_running_check('dovecot', 'dovecot', server)
                check.add_service_group(ServiceGroup.create('mail'))

            if True is self.__check_postgrey_running:
                check = self.create_running_check('postgrey', 'postgrey', server)
                check.add_service_group(ServiceGroup.create('mail'))

            if True is self.__check_opendkim_running:
                check = self.create_running_check('opendkim', 'opendkim', server)
                check.add_service_group(ServiceGroup.create('mail'))

            # force checking if enabled and not inherited
            if True is DefaultLocalChecks.is_checking_postfix_running(self) and not self.__inherit:
                check = self.create_running_check_arguments('postfix', 'postfix', server)
                check.add_service_group(ServiceGroup.create('mail'))

            if True is DefaultLocalChecks.is_checking_freshclam_running(self) and not self.__inherit:
                check = self.create_running_check('freshclam', 'freshclam', server)
                check.add_service_group(ServiceGroup.create('security'))
                check.add_service_group(ServiceGroup.create('antivirus'))

            if True is DefaultLocalChecks.is_checking_clamd_running(self) and not self.__inherit:
                check = self.create_running_check('clamd', 'clamd', server)
                check.add_service_group(ServiceGroup.create('security'))
                check.add_service_group(ServiceGroup.create('antivirus'))
