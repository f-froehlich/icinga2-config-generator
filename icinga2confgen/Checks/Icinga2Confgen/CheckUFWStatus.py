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
from icinga2confgen.Commands.Icinga2Confgen.UFWStatusCommand import UFWStatusCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckUFWStatus(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckUFWStatus', 'ufw_status')
        self.__status = None
        self.__warninactive = None
        self.__logging = None
        self.__loggingpolicy = None
        self.__incoming = None
        self.__outgoing = None
        self.__routing = None
        self.__rule = []
        self.set_check_interval('6h')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('ufw'))
        self.add_service_group(ServiceGroup.create('firewall'))

    def set_status(self, status):
        ValueChecker.is_string(status)
        self.__status = status
        return self

    def get_status(self):
        return self.__status

    def set_warninactive(self, warninactive):
        ValueChecker.is_bool(warninactive)
        self.__warninactive = 'on' if warninactive else 'off'
        return self

    def get_warninactive(self):
        return True if 'on' == self.__warninactive else False

    def set_logging(self, logging):
        ValueChecker.is_string(logging)
        self.__logging = logging
        return self

    def get_logging(self):
        return self.__logging

    def set_incoming(self, incoming):
        ValueChecker.is_string(incoming)
        self.__incoming = incoming
        return self

    def get_incoming(self):
        return self.__incoming

    def set_outgoing(self, outgoing):
        ValueChecker.is_string(outgoing)
        self.__outgoing = outgoing
        return self

    def get_outgoing(self):
        return self.__outgoing

    def set_routing(self, routing):
        ValueChecker.is_string(routing)
        self.__routing = routing
        return self

    def get_routing(self):
        return self.__routing

    def add_rule(self, policy_from, policy_to, policy_action):
        ValueChecker.is_string(policy_from)
        ValueChecker.is_string(policy_to)
        ValueChecker.is_string(policy_action)
        self.__rule.append(policy_from + "," + policy_to + ',' + policy_action)
        return self

    def remove_rule(self, policy_from, policy_to, policy_action):
        ValueChecker.is_string(policy_from)
        ValueChecker.is_string(policy_to)
        ValueChecker.is_string(policy_action)
        self.__rule.remove(policy_from + "," + policy_to + ',' + policy_action)
        return self

    def get_rule(self):
        return self.__rule

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckUFWStatus(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('ufw_status'):
            UFWStatusCommand.create('ufw_status')

        return check

    def validate(self):
        pass
