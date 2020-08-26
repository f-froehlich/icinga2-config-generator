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

# g1 = UserGroup.create('gr1') \
#     .set_display_name('Gruppe 1')
# g2 = UserGroup.create('gr2') \
#     .set_display_name('Gruppe 2')
#
# u = User.create('user1') \
#     .set_display_name('User 1') \
#     .set_email('mail@f-froehlich.de') \
#     .set_phone('0157') \
#     .add_group(g1) \
#     .add_group(g2)
# tp = DefaultTimePeriods.continuously()
# mn = MailNotificationCommand.create('mail')
# sn = ServiceNotification.create('nt').set_escalation('1m', '2h').set_time_period(tp).add_user(u).add_user_group(
#     g1).set_command(mn)
# hn = HostNotification.create('hn').set_escalation('1m', '2h').set_time_period(tp).add_user(u).add_user_group(
#     g1).set_command(mn)
# d = ScheduledDowntime.create('down1').set_author(u).set_comment('Testweise außer Betrieb').set_duration(
#     '30m').add_period('tuesday', '0:00-10:00').set_fixed(False).set_type('Host')
# ipv4_check = CheckDig.create('ipv4_za') \
#     .set_record_type('A') \
#     .set_question('gitlab.dev.f-froehlich.de') \
#     .set_expected_address('185.228.137.102') \
#     .add_notification(sn)
#
# s1 = Server.create('froehlich_1_za') \
#     .set_ipv4('185.228.137.102') \
#     .add_check(ipv4_check) \
#     .add_notification(hn)
# s2 = Server.create('froehlich_2_za') \
#     .set_ipv4('185.228.137.102') \
#     .add_check(ipv4_check) \
#     .add_notification(hn)
# s3 = Server.create('froehlich_3_za') \
#     .set_ipv4('185.228.137.102') \
#     .add_check(ipv4_check) \
#     .add_notification(hn)
# s4 = Server.create('froehlich_4_za') \
#     .set_ipv4('185.228.137.102') \
#     .add_check(ipv4_check) \
#     .add_notification(hn)
# s5 = Server.create('froehlich_5_za') \
#     .set_ipv4('185.228.137.102') \
#     .add_check(ipv4_check) \
#     .add_notification(hn)
#
#
#
# webserver = Webserver(
#     vhostconfig=[
#         ('f-froehlich.de', '/', []),
#         ('gitlab.dev.f-froehlich.de', '/users/sign_in', []),
#         ('jenkins.dev.f-froehlich.de', '/login', []),
#         ('nexus.dev.f-froehlich.de', '/', [])
#     ],
#     servers=[s1, s2, s3, s4, s5]
# )
#
# webserver.apply()

domain_check = DomainCheck(
    [
        ('f-froehlich.de', '185.228.137.102', None, True),
        ('ns1.f-froehlich.de', '185.228.137.102', None, True),
        ('ns2.f-froehlich.de', '185.228.137.102', None, True),
        ('mx.f-froehlich.de', '185.228.137.102', None, True),
        ('imap.f-froehlich.de', '185.228.137.102', None, True),
        ('smtp.f-froehlich.de', '185.228.137.102', None, True),
        ('dev.f-froehlich.de', '185.228.137.102', None, True),
        ('gitlab.dev.f-froehlich.de', '185.228.137.102', None, True),
        ('nexus.dev.f-froehlich.de', '185.228.137.102', None, True),
        ('jenkins.dev.f-froehlich.de', '185.228.137.102', None, True),
        ('munin.monitor.intern.f-froehlich.de', '192.168.0.10', None, True),
        ('icinga.monitor.intern.f-froehlich.de', '192.168.0.10', None, True),
        ('gateway.intern.f-froehlich.de', '192.168.0.1', None, True),
    ]
)

domain_check.apply()

ConfigBuilder.get_config()
