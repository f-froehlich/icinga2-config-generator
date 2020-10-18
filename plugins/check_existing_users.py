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

import argparse
import sys
import subprocess

class GroupMembers:

    def __init__(self, uid_min, uid_max, users, shell_filter):
        self.__users = users
        self.__uid_min = uid_min
        self.__uid_max = uid_max
        self.__shell_filter = shell_filter
        self.__current_members = self.get_current_members()

    def main(self):

        not_existing_users = []
        exist_on_server_but_shouldnt = []
        current_usernames = []
        for current in self.__current_members:
            current_usernames.append(current['username'])
            if current['username'] not in self.__users:
                exist_on_server_but_shouldnt.append(current['username'])

        for user in self.__users:
            if user not in current_usernames:
                not_existing_users.append(user)

        if 0 != len(exist_on_server_but_shouldnt):
            print(
                "CRITICAL: There are some users, which are not expected! Not expected users: " + ", ".join(
                    exist_on_server_but_shouldnt))
            sys.exit(2)

        if 0 != len(not_existing_users):
            print(
                "WARNING: There are some users not on Server, which are expected! Expected additional users: " + ", ".join(
                    not_existing_users))
            sys.exit(1)

        print("OK")
        sys.exit(0)

    def get_current_members(self):

        out = subprocess.Popen(['cat', '/etc/passwd'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        stdout, stderr = out.communicate()

        if 0 is not out.returncode:
            stderr = stderr.decode("utf-8")
            print('UNKNOWN: ' + stderr)
            sys.exit(3)

        stdout = stdout.decode("utf-8")

        parsed_users = []
        for config in stdout.split("\n"):
            config = config.split(":")

            if 7 != len(config):
                continue

            if -1 < self.__uid_min and int(config[2]) < self.__uid_min:
                continue

            if -1 < self.__uid_max < int(config[2]):
                continue

            if config[6] in self.__shell_filter:
                continue

            parsed_users.append({
                "username": config[0],
                "uid": int(config[2]),
                "gid": int(config[3]),
                "home": config[5],
                "shell": config[6],
            })

        return parsed_users


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check Users on the system')

    parser.add_argument('-m', '--uid-min', dest='minuid', default=-1, type=int, help='Minimum userid')
    parser.add_argument('-M', '--uid-max', dest='maxuid', default=-1, type=int, help='Maximum userid')
    parser.add_argument('-u', '--user', dest='users', action='append', default=[],
                        help='Normal not sudoer user. USERNAME')
    parser.add_argument('-S', '--filter-shell', dest='shellfilter', action='append', default=[],
                        help='Excluded list of shells')

    args = parser.parse_args()
    GroupMembers(
        uid_min=args.minuid,
        uid_max=args.maxuid,
        users=args.users,
        shell_filter=args.shellfilter
    ).main()
