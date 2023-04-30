#!/usr/bin/python3
# -*- coding: utf-8
import typing

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.MonitoringPlugins.UFWStatusCommand import UFWStatusCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

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

T = typing.TypeVar('T', bound='CheckUFWStatus')


class CheckUFWStatus(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckUFWStatus', 'monitoring_plugins_ufw_status')
        self.__status = None
        self.__warninactive = None
        self.__logging = None
        self.__loggingpolicy = None
        self.__incoming = None
        self.__outgoing = None
        self.__routing = None
        self.__rule = []
        self.set_check_interval('15m')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('ufw'))
        self.add_service_group(ServiceGroup.create('firewall'))

    def set_status(self, status: typing.Union[str, None]) -> T:
        self.__status = status
        return self

    def get_status(self) -> typing.Union[str, None]:
        return self.__status

    def set_warninactive(self, warninactive: bool) -> T:
        self.__warninactive = 'on' if warninactive else 'off'
        return self

    def get_warninactive(self) -> bool:
        return True if 'on' == self.__warninactive else False

    def set_logging(self, logging: typing.Union[str, None]) -> T:
        self.__logging = logging
        return self

    def get_logging(self) -> typing.Union[str, None]:
        return self.__logging

    def set_incoming(self, incoming: typing.Union[str, None]) -> T:
        self.__incoming = incoming
        return self

    def get_incoming(self) -> typing.Union[str, None]:
        return self.__incoming

    def set_outgoing(self, outgoing: typing.Union[str, None]) -> T:
        self.__outgoing = outgoing
        return self

    def get_outgoing(self) -> typing.Union[str, None]:
        return self.__outgoing

    def set_routing(self, routing: typing.Union[str, None]) -> T:
        self.__routing = routing
        return self

    def get_routing(self) -> typing.Union[str, None]:
        return self.__routing

    def add_rule(self, policy_from: str, policy_to: str, policy_action: str) -> T:
        rule = policy_from + "," + policy_to + ',' + policy_action
        if rule not in self.__rule:
            self.__rule.append(rule)
        return self

    def remove_rule(self, policy_from: str, policy_to: str, policy_action: str) -> T:
        rule = policy_from + "," + policy_to + ',' + policy_action
        if rule in self.__rule:
            self.__rule.remove(rule)
        return self

    def get_rule(self) -> typing.List[str]:
        return self.__rule

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckUFWStatus(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckUFWStatus):
            raise Exception('Id must be for an instance of CheckUFWStatus but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_ufw_status'):
            UFWStatusCommand.create('monitoring_plugins_ufw_status')

        return check

    def validate(self):
        pass
