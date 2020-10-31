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
from icinga2confgen.Utils.DefaultGitChecks import DefaultGitChecks
from icinga2confgen.ValueChecker import ValueChecker


class DefaultWordpressChecks(DefaultWebserverChecks):

    def __init__(self, vhostconfig=[], servers=[], checkserver=[], notifications=[]):
        DefaultWebserverChecks.__init__(self, vhostconfig, servers, checkserver, notifications)
        self.__validate_deny_git = True
        self.__validate_deny_gitignore = True
        self.__validate_deny_license = True
        self.__validate_deny_readme = True
        self.__validate_deny_wp_admin = True
        self.__validate_deny_wp_login = True
        self.__inherit = True
        self.__git_checks = DefaultGitChecks(vhostconfig, servers, checkserver, notifications).set_inherit(False)

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

    def validate_deny_license(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_deny_license = enabled

        return self

    def is_validating_deny_license(self):
        return self.__validate_deny_license

    def validate_deny_readme(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_deny_readme = enabled

        return self

    def is_validating_deny_readme(self):
        return self.__validate_deny_readme

    def validate_deny_wp_admin(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_deny_wp_admin = enabled

        return self

    def is_validating_deny_wp_admin(self):
        return self.__validate_deny_wp_admin

    def validate_deny_wp_login(self, enabled):
        ValueChecker.is_bool(enabled)
        self.__validate_deny_wp_login = enabled

        return self

    def is_validating_deny_wp_login(self):
        return self.__validate_deny_wp_login

    def apply(self):
        if self.__inherit:
            DefaultWebserverChecks.apply(self)

        self.__git_checks.validate_deny_git(self.__validate_deny_git) \
            .validate_deny_gitignore(self.__validate_deny_gitignore) \
            .apply()

        for config in DefaultWordpressChecks.get_vhostconfigs(self):
            service_baseid = config[0]
            domain = config[1]

            for checkserver in DefaultWebserverChecks.get_checkservers(self):
                for server in DefaultWebserverChecks.get_servers(self):
                    base_id = service_baseid + '_' + ''.join(e for e in domain + server.get_id() if e.isalnum())
                    server_ip = server.get_ipv4()
                    if None is server_ip:
                        server_ip = server.get_ipv6()

                    if True is self.__validate_deny_license:
                        check = CheckHttp.create('web_access_deny_license_' + base_id)
                        check.set_ip(server_ip) \
                            .set_vhost(domain) \
                            .set_uri('/license.txt') \
                            .set_ssl(True) \
                            .set_sni(DefaultWebserverChecks.get_sni(self)) \
                            .set_expect('40') \
                            .set_check_interval('6h') \
                            .set_display_name(check.get_display_name() + ' ' + domain)
                        self.apply_notification_to_check(check)
                        checkserver.add_check(check)

                    if True is self.__validate_deny_readme:
                        check = CheckHttp.create('web_access_deny_readme_' + base_id)
                        check.set_ip(server_ip) \
                            .set_vhost(domain) \
                            .set_uri('/readme.html') \
                            .set_ssl(True) \
                            .set_sni(DefaultWebserverChecks.get_sni(self)) \
                            .set_expect('40') \
                            .set_check_interval('6h') \
                            .set_display_name(check.get_display_name() + ' ' + domain)
                        self.apply_notification_to_check(check)
                        checkserver.add_check(check)

                    if True is self.__validate_deny_wp_admin:
                        check = CheckHttp.create('web_access_deny_wp_admin_' + base_id)
                        check.set_ip(server_ip) \
                            .set_vhost(domain) \
                            .set_uri('/wp-admin/') \
                            .set_ssl(True) \
                            .set_sni(DefaultWebserverChecks.get_sni(self)) \
                            .set_expect('40') \
                            .set_check_interval('6h') \
                            .set_display_name(check.get_display_name() + ' ' + domain)
                        self.apply_notification_to_check(check)
                        checkserver.add_check(check)

                    if True is self.__validate_deny_wp_login:
                        check = CheckHttp.create('web_access_deny_wp_login_' + base_id)
                        check.set_ip(server_ip) \
                            .set_vhost(domain) \
                            .set_uri('/wp-login.php') \
                            .set_ssl(True) \
                            .set_sni(DefaultWebserverChecks.get_sni(self)) \
                            .set_expect('40') \
                            .set_check_interval('6h') \
                            .set_display_name(check.get_display_name() + ' ' + domain)
                        self.apply_notification_to_check(check)
                        checkserver.add_check(check)
