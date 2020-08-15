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
from Utils.DomainCheck import DomainCheck

#
# s = Server.create('localhost') \
#     .set_ipv4('127.0.0.1') \
#     .add_check(CheckDisk.create('local').set_path('/'))
#

# s = Server.create('froehlich') \
#     .set_ipv4('185.228.137.102') \
#     .add_check(CheckDisk.create('remote').set_path('/'))

# s1 = Server.create('froehlich_1') \
#     .set_ipv4('185.228.137.102')
# s2 = Server.create('froehlich_2') \
#     .set_ipv4('185.228.137.102')
# s3 = Server.create('froehlich_3') \
#     .set_ipv4('185.228.137.102')

server = DomainCheck(
    [
        ('f-froehlich.de', '185.228.137.102', None, True),
        ('dev.f-froehlich.de', '185.228.137.102', None, True),
        ('gitlab.dev.f-froehlich.de', '185.228.137.102', None, True),
        ('nexus.dev.f-froehlich.de', '185.228.137.102', None, True),
        ('jenkins.dev.f-froehlich.de', '185.228.137.102', None, True),
    ]
)

server.apply()

print(ConfigBuilder.get_config())
