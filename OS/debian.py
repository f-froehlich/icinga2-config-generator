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
from PackageManager.PackageManager import apt

os_debian_2_0 = OS.create('debian_2_0').set_distro('debian').set_version('2.0').set_os('Debian GNU/Linux 2.0 (hamm)').set_package_manager(apt)
os_debian_2_1 = OS.create('debian_2_1').set_distro('debian').set_version('2.1').set_os('Debian GNU/Linux 2.1 (slink)').set_package_manager(apt)
os_debian_2_2 = OS.create('debian_2_2').set_distro('debian').set_version('2.2').set_os('Debian GNU/Linux 2.2 (potato)').set_package_manager(apt)
os_debian_3_0 = OS.create('debian_3_0').set_distro('debian').set_version('3.0').set_os('Debian GNU/Linux 3.0 (woody)').set_package_manager(apt)
os_debian_3_1 = OS.create('debian_3_1').set_distro('debian').set_version('3.1').set_os('Debian GNU/Linux 3.1 (sarge)').set_package_manager(apt)
os_debian_4_0 = OS.create('debian_4_0').set_distro('debian').set_version('4.0').set_os('Debian GNU/Linux 4.0 (etch)').set_package_manager(apt)
os_debian_5_0 = OS.create('debian_5_0').set_distro('debian').set_version('5.0').set_os('Debian GNU/Linux 5.0 (lenny)').set_package_manager(apt)
os_debian_6_0 = OS.create('debian_6_0').set_distro('debian').set_version('6.0').set_os('Debian 6.0 (squeeze)').set_package_manager(apt)
os_debian_7   = OS.create('debian_7')  .set_distro('debian').set_version('7')  .set_os('Debian 7 (wheezy)').set_package_manager(apt)
os_debian_8   = OS.create('debian_8')  .set_distro('debian').set_version('8')  .set_os('Debian 8 (jessie)').set_package_manager(apt)
os_debian_9   = OS.create('debian_9')  .set_distro('debian').set_version('9')  .set_os('Debian 9 (stretch)').set_package_manager(apt)
os_debian_10  = OS.create('debian_10') .set_distro('debian').set_version('10') .set_os('Debian 10 (buster)').set_package_manager(apt)
