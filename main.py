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

from Checks.CheckSSH import CheckSSH
from ConfigBuilder import ConfigBuilder
from Servers.Server import Server

s = Server.create('localhost') \
    .set_ipv4('127.0.0.1') \
    .add_check(CheckSSH.create('local').set_hostname('f-froehlich.de').set_port(10))

s2 = Server.create('froehlich') \
    .set_ipv4('185.228.137.102') \
    .add_check(CheckSSH.create('remote').set_hostname('jenkins.dev.f-froehlich.de').set_port(10))

print(ConfigBuilder.get_config())
