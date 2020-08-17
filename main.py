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

from Checks.CheckDig import CheckDig
from ConfigBuilder import ConfigBuilder
from Downtimes.ScheduledDowntime import ScheduledDowntime
from Groups.UserGroup import UserGroup
from Notification.DefaultTimePeriods import DefaultTimePeriods
from Notification.HostNotification import HostNotification
from Notification.ServiceNotification import ServiceNotification
from Servers.Server import Server
from User.User import User

g1 = UserGroup.create('gr1') \
    .set_display_name('Gruppe 1')
g2 = UserGroup.create('gr2') \
    .set_display_name('Gruppe 2')

u = User.create('user1') \
    .set_display_name('User 1') \
    .set_email('mail@f-froehlich.de') \
    .set_phone('0157') \
    .add_group(g1) \
    .add_group(g2)
tp = DefaultTimePeriods.continuously()
sn = ServiceNotification.create('nt').set_escalation('1m', '2h').set_time_period(tp).add_user(u).add_user_group(g1)
hn = HostNotification.create('hn').set_escalation('1m', '2h').set_time_period(tp).add_user(u).add_user_group(g1)
d = ScheduledDowntime.create('down1').set_author(u).set_comment('Testweise außer Betrieb').set_duration(
    '30m').add_period('tuesday', '0:00-10:00').set_fixed(False).set_type('Host')
ipv4_check = CheckDig.create('ipv4') \
    .set_record_type('A') \
    .set_question('gitlab.dev.f-froehlich.de') \
    .set_expected_address('185.228.137.102') \
    .add_notification(sn)

s1 = Server.create('froehlich_1') \
    .set_ipv4('185.228.137.102') \
    .add_check(ipv4_check) \
    .add_notification(hn).add_downtime(d)

print(ConfigBuilder.get_config())
