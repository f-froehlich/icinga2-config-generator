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
from Groups.Group import Group
from ValueChecker import ValueChecker


class HostGroup(Group):

    def __init__(self, id):
        Group.__init__(self, id, 'host')

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)
        hostgroup = ConfigBuilder.get_hostgroup(id)
        if None is hostgroup:
            id = 'hostgroup_' + id
            hostgroup = HostGroup(id)
            ConfigBuilder.add_hostgroup(id, hostgroup)

        return hostgroup
