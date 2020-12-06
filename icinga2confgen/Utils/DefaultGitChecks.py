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
from icinga2confgen.Checks.NagiosPlugins.CheckHttp import CheckHttp
from icinga2confgen.Utils.DefaultWebserverChecks import DefaultWebserverChecks
from icinga2confgen.ValueChecker import ValueChecker


class DefaultGitChecks(DefaultWebserverChecks):

    def __init__(self, vhostconfig=[], servers=[], checkserver=[], notifications=[]):
        DefaultWebserverChecks.__init__(self, vhostconfig, servers, checkserver, notifications)
        self.__validate_deny_git = True
        self.__validate_deny_gitignore = True
        self.__inherit = True

    def set_inherit(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__inherit = enabled

        return self

    def is_inherit(self):
        return self.__inherit

    def validate_deny_git(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_deny_git = enabled

        return self

    def is_validating_deny_git(self):
        return self.__validate_deny_git

    def validate_deny_gitignore(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_deny_gitignore = enabled

        return self

    def is_validating_deny_gitignore(self):
        return self.__validate_deny_gitignore

    def apply(self):
        if self.__inherit:
            DefaultWebserverChecks.apply(self)

        for config in DefaultWebserverChecks.get_vhostconfigs(self):
            service_baseid = config[0]
            domain = config[1]

            for server in DefaultWebserverChecks.get_servers(self):
                base_id = service_baseid

                if True is self.__validate_deny_git:
                    self.create_git_check('gitdir', service_baseid, base_id, domain, server, '/.git/')

                if True is self.__validate_deny_gitignore:
                    self.create_git_check('gitignore', service_baseid, base_id, domain, server, '/.gitignore')

    def create_git_check(self, name, base_id, service_baseid, domain, server, uri):

        if None is server.get_ipv4() and None is server.get_ipv6():
            raise Exception('It is required to set the ipv4 or ipv6 on the server with id "' +
                            server.get_id() + '", before you can apply this checks!')

        default_access_checks = self.get_default_access_check(service_baseid, server, domain)
        if None is not server.get_ipv4():
            git_check = CheckHttp.create('web_access_deny_' + name + '_ipv4_' + base_id)
            git_check.set_ip(server.get_ipv4()) \
                .set_vhost(domain) \
                .set_uri(uri) \
                .set_ssl(True) \
                .set_sni(DefaultWebserverChecks.get_sni(self)) \
                .set_expect('40') \
                .set_check_interval('15m') \
                .set_display_name(git_check.get_display_name() + ' ' + domain)
            self.apply_check(git_check, default_access_checks['ipv4'])

        if None is not server.get_ipv6():
            git_check = CheckHttp.create('web_access_deny_' + name + '_ipv6_' + base_id)
            git_check.set_ip(server.get_ipv6()) \
                .set_vhost(domain) \
                .set_uri(uri) \
                .set_ssl(True) \
                .set_sni(DefaultWebserverChecks.get_sni(self)) \
                .set_expect('40') \
                .set_check_interval('15m') \
                .set_display_name(git_check.get_display_name() + ' ' + domain)
            self.apply_check(git_check, default_access_checks['ipv4'])
