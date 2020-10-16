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
from PackageManager.PackageManager import *

os_ubuntu_4_10 =  OS.create('ubuntu_4_10') .set_distro('ubuntu').set_version('4.10') .set_os('Ubuntu 4.10 STS (Warty Warthog)').set_package_manager(apt)
os_ubuntu_5_04 =  OS.create('ubuntu_5_04') .set_distro('ubuntu').set_version('5.04') .set_os('Ubuntu 5.04 STS (Hoary Hedgehog)').set_package_manager(apt)
os_ubuntu_5_10 =  OS.create('ubuntu_5_10') .set_distro('ubuntu').set_version('5.10') .set_os('Ubuntu 5.10 STS (Breezy Badger)').set_package_manager(apt)
os_ubuntu_6_06 =  OS.create('ubuntu_6_06') .set_distro('ubuntu').set_version('6.06') .set_os('Ubuntu 6.06 LTS (Dapper Drake)').set_package_manager(apt)
os_ubuntu_6_10 =  OS.create('ubuntu_6_10') .set_distro('ubuntu').set_version('6.10') .set_os('Ubuntu 6.10 STS (Edgy Eft)').set_package_manager(apt)
os_ubuntu_7_04 =  OS.create('ubuntu_7_04') .set_distro('ubuntu').set_version('7.04') .set_os('Ubuntu 7.04 STS (Feisty Fawn)').set_package_manager(apt)
os_ubuntu_7_10 =  OS.create('ubuntu_7_10') .set_distro('ubuntu').set_version('7.10') .set_os('Ubuntu 7.10 STS (Gutsy Gibbon)').set_package_manager(apt)
os_ubuntu_8_04 =  OS.create('ubuntu_8_04') .set_distro('ubuntu').set_version('8.04') .set_os('Ubuntu 8.04 LTS (Hardy Heron)').set_package_manager(apt)
os_ubuntu_8_10 =  OS.create('ubuntu_8_10') .set_distro('ubuntu').set_version('8.10') .set_os('Ubuntu 8.10 STS (Intrepid Ibex)').set_package_manager(apt)
os_ubuntu_9_04 =  OS.create('ubuntu_9_04') .set_distro('ubuntu').set_version('9.04') .set_os('Ubuntu 9.04 STS (Jaunty Jackalope)').set_package_manager(apt)
os_ubuntu_9_10 =  OS.create('ubuntu_9_10') .set_distro('ubuntu').set_version('9.10') .set_os('Ubuntu 9.10 STS (Karmic Koala)').set_package_manager(apt)
os_ubuntu_10_04 = OS.create('ubuntu_10_04').set_distro('ubuntu').set_version('10.04').set_os('Ubuntu 10.04 LTS (Lucid Lynx)').set_package_manager(apt)
os_ubuntu_10_10 = OS.create('ubuntu_10_10').set_distro('ubuntu').set_version('10.10').set_os('Ubuntu 10.10 STS (Maverick Meerkat)').set_package_manager(apt)
os_ubuntu_11_04 = OS.create('ubuntu_11_04').set_distro('ubuntu').set_version('11.04').set_os('Ubuntu 11.04 STS (Natty Narwhal)').set_package_manager(apt)
os_ubuntu_11_10 = OS.create('ubuntu_11_10').set_distro('ubuntu').set_version('11.10').set_os('Ubuntu 11.10 STS (Oneiric Ocelot)').set_package_manager(apt)
os_ubuntu_12_04 = OS.create('ubuntu_12_04').set_distro('ubuntu').set_version('12.04').set_os('Ubuntu 12.04 LTS (Precise Pangolin)').set_package_manager(apt)
os_ubuntu_12_10 = OS.create('ubuntu_12_10').set_distro('ubuntu').set_version('12.10').set_os('Ubuntu 12.10 STS (Quantal Quetzal)').set_package_manager(apt)
os_ubuntu_13_04 = OS.create('ubuntu_13_04').set_distro('ubuntu').set_version('13.04').set_os('Ubuntu 13.04 STS (Raring Ringtail)').set_package_manager(apt)
os_ubuntu_13_10 = OS.create('ubuntu_13_10').set_distro('ubuntu').set_version('13.10').set_os('Ubuntu 13.10 STS (Saucy Salamander)').set_package_manager(apt)
os_ubuntu_14_04 = OS.create('ubuntu_14_04').set_distro('ubuntu').set_version('14.04').set_os('Ubuntu 14.04 LTS (Trusty Tahr)').set_package_manager(apt)
os_ubuntu_14_10 = OS.create('ubuntu_14_10').set_distro('ubuntu').set_version('14.10').set_os('Ubuntu 14.10 STS (Utopic Unicorn)').set_package_manager(apt)
os_ubuntu_15_04 = OS.create('ubuntu_15_04').set_distro('ubuntu').set_version('15.04').set_os('Ubuntu 15.04 STS (Vivid Vervet)').set_package_manager(apt)
os_ubuntu_15_10 = OS.create('ubuntu_15_10').set_distro('ubuntu').set_version('15.10').set_os('Ubuntu 15.10 STS (Wily Werewolf)').set_package_manager(apt)
os_ubuntu_16_04 = OS.create('ubuntu_16_04').set_distro('ubuntu').set_version('16.04').set_os('Ubuntu 16.04 LTS (Xenial Xerus)').set_package_manager(apt)
os_ubuntu_16_10 = OS.create('ubuntu_16_10').set_distro('ubuntu').set_version('16.10').set_os('Ubuntu 16.10 STS (Yakkety Yak)').set_package_manager(apt)
os_ubuntu_17_04 = OS.create('ubuntu_17_04').set_distro('ubuntu').set_version('17.04').set_os('Ubuntu 17.04 STS (Zesty Zapus)').set_package_manager(apt)
os_ubuntu_17_10 = OS.create('ubuntu_17_10').set_distro('ubuntu').set_version('17.10').set_os('Ubuntu 17.10 STS (Artful Aardvark)').set_package_manager(apt)
os_ubuntu_18_04 = OS.create('ubuntu_18_04').set_distro('ubuntu').set_version('18.04').set_os('Ubuntu 18.04 LTS (Bionic Beaver)').set_package_manager(apt)
os_ubuntu_18_10 = OS.create('ubuntu_18_10').set_distro('ubuntu').set_version('18.10').set_os('Ubuntu 18.10 STS (Cosmic Cuttlefish)').set_package_manager(apt)
os_ubuntu_19_04 = OS.create('ubuntu_19_04').set_distro('ubuntu').set_version('19.04').set_os('Ubuntu 19.04 STS (Disco Dingo)').set_package_manager(apt)
os_ubuntu_19_10 = OS.create('ubuntu_19_10').set_distro('ubuntu').set_version('19.10').set_os('Ubuntu 19.10 STS (Eoan Ermine)').set_package_manager(apt)
os_ubuntu_20_04 = OS.create('ubuntu_20_04').set_distro('ubuntu').set_version('20.04').set_os('Ubuntu 20.04 LTS (Focal Fossa)').set_package_manager(apt)
os_ubuntu_20_10 = OS.create('ubuntu_20_10').set_distro('ubuntu').set_version('20.10').set_os('Ubuntu 20.10 STS (Groovy Gorilla)').set_package_manager(apt)
