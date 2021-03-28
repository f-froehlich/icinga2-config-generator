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
from icinga2confgen.Checks.NagiosPlugins.CheckPing4 import CheckPing4
from icinga2confgen.Checks.NagiosPlugins.CheckPing6 import CheckPing6
from icinga2confgen.Helpers.RemoteCheckManager import RemoteCheckManager
from icinga2confgen.ValueChecker import ValueChecker


class SynologySNMPChecks(RemoteCheckManager):

    def __init__(self, servers=[], checkserver=[], notifications=[]):
        RemoteCheckManager.__init__(self, servers=servers, checkserver=checkserver, notifications=notifications)
        self.__check_ping = True

    def check_ping(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__check_ping = enabled

        return self

    def is_checking_ping(self):
        return self.__check_ping

    def apply(self):
        for server in self.get_servers():
            ipv4 = server.get_ipv4()
            ipv6 = server.get_ipv6()
            disc_count = server.get_custom_var('disk_count')
            volume_count = server.get_custom_var('volume_count')
            raid_count = server.get_custom_var('raid_count')

            if None is disc_count or not isinstance(disc_count, int):
                raise Exception(
                    'Require custom var "disc_count" as integer for server "{server}"'.format(server=server.get_id()))
            if None is volume_count or not isinstance(volume_count, int):
                raise Exception(
                    'Require custom var "volume_count" as integer for server "{server}"'.format(server=server.get_id()))
            if None is raid_count or not isinstance(raid_count, int):
                raise Exception(
                    'Require custom var "raid_count" as integer for server "{server}"'.format(server=server.get_id()))

            for checkserver in self.get_checkservers():
                base_id = 'synology_checks_' + server.get_id() + '_' + checkserver.get_id()

                if True is self.__check_ping:
                    if None is not ipv4:
                        check = CheckPing4.create('ping4_' + base_id)
                        check.set_address(ipv4) \
                            .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                        self.apply_check(check, server, checkserver)
                    if None is not ipv6:
                        check = CheckPing6.create('ping6_' + base_id)
                        check.set_address(ipv6) \
                            .set_display_name(check.get_display_name() + ' ' + server.get_display_name())
                        self.apply_check(check, server, checkserver)
