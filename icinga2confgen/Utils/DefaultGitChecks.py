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
from icinga2confgen.Checks.Icinga2Confgen.CheckDenyTlsVersion import CheckDenyTlsVersion
from icinga2confgen.Checks.MonitoringPlugins.CheckDummy import CheckDummy
from icinga2confgen.Checks.MonitoringPlugins.CheckHttp import CheckHttp
from icinga2confgen.Groups.HostGroup import HostGroup
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
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

            for checkserver in DefaultWebserverChecks.get_checkservers(self):
                for server in DefaultWebserverChecks.get_servers(self):
                    base_id = service_baseid + '_' + ''.join(e for e in domain + server.get_id() if e.isalnum())
                    server_ip = server.get_ipv4()
                    if None is server_ip:
                        server_ip = server.get_ipv6()

                    if True is self.__validate_deny_git:
                        git_check = CheckHttp.create('web_access_deny_git_' + base_id)
                        git_check.set_ip(server_ip) \
                            .set_vhost(domain) \
                            .set_uri('/.git/') \
                            .set_ssl(True) \
                            .set_sni(DefaultWebserverChecks.get_sni(self)) \
                            .set_expect('40') \
                            .set_check_interval('6h') \
                            .set_display_name(git_check.get_display_name() + ' ' + domain)
                        self.apply_notification_to_check(git_check)

                        checkserver.add_check(git_check)

                    if True is self.__validate_deny_gitignore:
                        gitignore_check = CheckHttp.create('web_access_deny_gitignore_' + base_id)
                        gitignore_check.set_ip(server_ip) \
                            .set_vhost(domain) \
                            .set_uri('/.gitignore') \
                            .set_ssl(True) \
                            .set_sni(DefaultWebserverChecks.get_sni(self)) \
                            .set_expect('40') \
                            .set_check_interval('6h') \
                            .set_display_name(gitignore_check.get_display_name() + ' ' + domain)
                        self.apply_notification_to_check(git_check)

                        checkserver.add_check(git_check)
