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
from icinga2confgen.Helpers.LocalCheckManager import LocalCheckManager


class RemoteCheckManager(LocalCheckManager):

    def __init__(self, checkserver=[], servers=[], notifications=[]):
        LocalCheckManager.__init__(self, servers=servers, notifications=notifications)
        self.__checkserver = checkserver

    def get_checkservers(self):
        return self.__checkserver

    def add_checkserver(self, checkserver):
        self.__checkserver.append(checkserver)

    def apply_check(self, check, depends_on=None):
        self.apply_notification_to_check(check)
        check.set_check_type(self.get_check_type())
        for checkserver in self.__checkserver:
            checkserver.add_check(check)
            self.apply_dependency(check, checkserver, depends_on)

        self.handle_callback(check)
