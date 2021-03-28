#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, commands, checks, ... in python
#
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
from __future__ import annotations

from icinga2confgen.Downtimes.ScheduledDowntime import ScheduledDowntime
from icinga2confgen.User.User import User


class DefaultScheduledDowntimes:

    @staticmethod
    def weekday_nine_to_five(id: str = 'mo_fr_9_17', comment: str = 'Mo-Fr, 9am - 5pm') -> ScheduledDowntime:
        return ScheduledDowntime.create(id) \
            .set_comment(comment) \
            .set_author(User.create('admin')) \
            .add_period("monday", "09:00-17:00") \
            .add_period("tuesday", "09:00-17:00") \
            .add_period("wednesday", "09:00-17:00") \
            .add_period("thursday", "09:00-17:00") \
            .add_period("friday", "09:00-17:00")

    @staticmethod
    def weekend(id: str = 'weekend', comment: str = 'Weekend') -> ScheduledDowntime:
        return ScheduledDowntime.create(id) \
            .set_comment(comment) \
            .set_author(User.create('admin')) \
            .add_period("saturday", "00:00-24:00") \
            .add_period("sunday", "00:00-24:00")

    @staticmethod
    def weekday_backup(id: str = 'weekday_backup', comment: str = 'Weekday backup') -> ScheduledDowntime:
        return ScheduledDowntime.create(id) \
            .set_comment(comment) \
            .set_author(User.create('admin')) \
            .add_period("monday", "00:00-3:00") \
            .add_period("tuesday", "00:00-3:00") \
            .add_period("wednesday", "00:00-3:00") \
            .add_period("thursday", "00:00-3:00") \
            .add_period("friday", "00:00-3:00")

    @staticmethod
    def daily_backup(id: str = 'daily_backup', comment: str = 'Daily backup') -> ScheduledDowntime:
        return ScheduledDowntime.create(id) \
            .set_comment(comment) \
            .set_author(User.create('admin')) \
            .add_period("monday", "00:00-3:00") \
            .add_period("tuesday", "00:00-3:00") \
            .add_period("wednesday", "00:00-3:00") \
            .add_period("thursday", "00:00-3:00") \
            .add_period("friday", "00:00-3:00") \
            .add_period("saturday", "00:00-3:00") \
            .add_period("sunday", "00:00-3:00")

    @staticmethod
    def continuously(id: str = '24_7', comment: str = '24/7') -> ScheduledDowntime:
        return ScheduledDowntime.create(id) \
            .set_comment(comment) \
            .set_author(User.create('admin')) \
            .add_period("monday", "00:00-24:00") \
            .add_period("tuesday", "00:00-24:00") \
            .add_period("wednesday", "00:00-24:00") \
            .add_period("thursday", "00:00-24:00") \
            .add_period("friday", "00:00-24:00") \
            .add_period("saturday", "00:00-24:00") \
            .add_period("sunday", "00:00-24:00")
