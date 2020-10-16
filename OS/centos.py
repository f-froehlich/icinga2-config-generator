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
from OS.OS import OS
from PackageManager.PackageManager import yum

os_centos_1 = OS.create('centos_1').set_distro('centos').set_version('1').set_os('CentOS Linux 1 (Core)').set_package_manager(yum)
os_centos_2 = OS.create('centos_2').set_distro('centos').set_version('2').set_os('CentOS Linux 2 (Core)').set_package_manager(yum)
os_centos_3 = OS.create('centos_3').set_distro('centos').set_version('3').set_os('CentOS Linux 3 (Core)').set_package_manager(yum)
os_centos_4 = OS.create('centos_4').set_distro('centos').set_version('4').set_os('CentOS Linux 4 (Core)').set_package_manager(yum)
os_centos_5 = OS.create('centos_5').set_distro('centos').set_version('5').set_os('CentOS Linux 5 (Core)').set_package_manager(yum)
os_centos_6 = OS.create('centos_6').set_distro('centos').set_version('6').set_os('CentOS Linux 6 (Core)').set_package_manager(yum)
os_centos_7 = OS.create('centos_7').set_distro('centos').set_version('7').set_os('CentOS Linux 7 (Core)').set_package_manager(yum)
os_centos_8 = OS.create('centos_8').set_distro('centos').set_version('8').set_os('CentOS Linux 8 (Core)').set_package_manager(yum)
