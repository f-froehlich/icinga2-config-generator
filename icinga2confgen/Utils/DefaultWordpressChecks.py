#!/usr/bin/python3
# -*- coding: utf-8
from __future__ import annotations

from typing import List, Tuple

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
from icinga2confgen.Groups.HostGroup import HostGroup
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.Notification.Notification import Notification
from icinga2confgen.Servers.Server import Server
from icinga2confgen.Utils.DefaultWebserverChecks import DefaultWebserverChecks
from icinga2confgen.ValueMapper import ValueMapper


class DefaultWordpressChecks(DefaultWebserverChecks):

    def __init__(self, vhostconfig: List[Tuple[str, str, str]] = [], servers: List[Server] = [],
                 checkserver: List[Server] = [], notifications: List[Notification] = []):
        DefaultWebserverChecks.__init__(self, vhostconfig, servers, checkserver, notifications)
        self.__validate_deny_license = True
        self.__validate_deny_readme = True
        self.__validate_deny_wp_admin = True
        self.__validate_deny_wp_includes = True
        self.__validate_deny_wp_content = True
        self.__validate_deny_wp_login = True
        self.__validate_deny_wp_cron = True
        self.__validate_deny_wp_load = True
        self.__validate_deny_wp_mail = True
        self.__validate_deny_wp_settings = True
        self.__validate_deny_wp_signup = True
        self.__validate_deny_wp_trackback = True
        self.__validate_deny_wp_xmlrpc = True
        self.__validate_deny_wp_config = True
        self.__validate_deny_wp_config_sample = True
        self.__validate_deny_wp_blog_header = True
        self.__validate_deny_wp_activate = True
        self.__validate_deny_wp_links_opml = True
        self.__inherit = True

    def set_inherit(self, enabled: bool) -> DefaultWordpressChecks:

        self.__inherit = enabled

        return self

    def is_inherit(self) -> bool:
        return self.__inherit

    def validate_deny_license(self, enabled: bool) -> DefaultWordpressChecks:
        
        self.__validate_deny_license = enabled

        return self

    def is_validating_deny_license(self) -> bool:
        return self.__validate_deny_license

    def validate_deny_readme(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_readme = enabled

        return self

    def is_validating_deny_readme(self) -> bool:
        return self.__validate_deny_readme

    def validate_deny_wp_admin(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_admin = enabled

        return self

    def is_validating_deny_wp_admin(self) -> bool:
        return self.__validate_deny_wp_admin

    def validate_deny_wp_includes(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_includes = enabled

        return self

    def is_validating_deny_wp_includes(self) -> bool:
        return self.__validate_deny_wp_includes

    def validate_deny_wp_content(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_content = enabled

        return self

    def is_validating_deny_wp_content(self) -> bool:
        return self.__validate_deny_wp_content

    def validate_deny_wp_login(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_login = enabled

        return self

    def is_validating_deny_wp_login(self) -> bool:
        return self.__validate_deny_wp_login

    def validate_deny_wp_cron(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_cron = enabled

        return self

    def is_validating_deny_wp_cron(self) -> bool:
        return self.__validate_deny_wp_cron

    def validate_deny_wp_load(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_load = enabled

        return self

    def is_validating_deny_wp_load(self) -> bool:
        return self.__validate_deny_wp_load

    def validate_deny_wp_mail(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_mail = enabled

        return self

    def is_validating_deny_wp_mail(self) -> bool:
        return self.__validate_deny_wp_mail

    def validate_deny_wp_settings(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_settings = enabled

        return self

    def is_validating_deny_wp_settings(self) -> bool:
        return self.__validate_deny_wp_settings

    def validate_deny_wp_signup(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_signup = enabled

        return self

    def is_validating_deny_wp_signup(self) -> bool:
        return self.__validate_deny_wp_signup

    def validate_deny_wp_trackback(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_trackback = enabled

        return self

    def is_validating_deny_wp_trackback(self) -> bool:
        return self.__validate_deny_wp_trackback

    def validate_deny_wp_xmlrpc(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_xmlrpc = enabled

        return self

    def is_validating_deny_wp_xmlrpc(self) -> bool:
        return self.__validate_deny_wp_xmlrpc

    def validate_deny_wp_config(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_config = enabled

        return self

    def is_validating_deny_wp_config(self) -> bool:
        return self.__validate_deny_wp_config

    def validate_deny_wp_config_sample(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_config_sample = enabled

        return self

    def is_validating_deny_wp_config_sample(self) -> bool:
        return self.__validate_deny_wp_config_sample

    def validate_deny_wp_blog_header(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_blog_header = enabled

        return self

    def is_validating_deny_wp_blog_header(self) -> bool:
        return self.__validate_deny_wp_blog_header

    def validate_deny_wp_activate(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_activate = enabled

        return self

    def is_validating_deny_wp_activate(self) -> bool:
        return self.__validate_deny_wp_activate

    def validate_deny_wp_links_opml(self, enabled: bool) -> DefaultWordpressChecks:

        self.__validate_deny_wp_links_opml = enabled

        return self

    def is_validating_deny_wp_links_opml(self) -> bool:
        return self.__validate_deny_wp_links_opml

    def create_wp_check(self, name, service_baseid, base_id, server, checkserver, domain, uri):

        if None is server.get_ipv4() and None is server.get_ipv6():
            raise Exception('It is required to set the ipv4 or ipv6 on the server with id "' +
                            server.get_id() + '", before you can apply this checks!')

        default_access_checks = self.get_default_access_check(service_baseid, server, domain)
        if None is not server.get_ipv4():
            check = CheckHttp.create('web_access_deny_' + name + '_ipv4_' + base_id)
            check.set_ip(server.get_ipv4()) \
                .set_vhost(domain) \
                .set_uri(uri) \
                .set_ssl(True) \
                .set_sni(DefaultWebserverChecks.get_sni(self)) \
                .set_expect('40') \
                .set_check_interval('15m') \
                .set_display_name(check.get_display_name() + ' ' + domain) \
                .add_service_group(ServiceGroup.create('wordpress'))

            self.apply_check(check, server, checkserver, default_access_checks['ipv4'])

        if None is not server.get_ipv6():
            check = CheckHttp.create('web_access_deny_' + name + '_ipv6_' + base_id)
            check.set_ip(server.get_ipv6()) \
                .set_ipv6(True) \
                .set_vhost(domain) \
                .set_uri(uri) \
                .set_ssl(True) \
                .set_sni(DefaultWebserverChecks.get_sni(self)) \
                .set_expect('40') \
                .set_check_interval('15m') \
                .set_display_name(check.get_display_name() + ' ' + domain) \
                .add_service_group(ServiceGroup.create('wordpress'))

            self.apply_check(check, server, checkserver, default_access_checks['ipv6'])

    def apply(self):
        if self.__inherit:
            DefaultWebserverChecks.apply(self)

        for config in DefaultWordpressChecks.get_vhostconfigs(self):
            service_baseid = config[0]
            domain = config[1]

            for server in DefaultWebserverChecks.get_servers(self):
                for checkserver in DefaultWebserverChecks.get_checkservers(self):
                    server.add_hostgroup(HostGroup.create('wordpress'))
                    base_id = service_baseid + '_' + server.get_id() + '_' + ValueMapper.canonicalize_for_id(
                        domain) + '_' + checkserver.get_id()

                    if True is self.__validate_deny_license:
                        self.create_wp_check('license', service_baseid, base_id, server, checkserver, domain,
                                             '/license.txt')
                    if True is self.__validate_deny_readme:
                        self.create_wp_check('readme', service_baseid, base_id, server, checkserver, domain,
                                             '/readme.html')
                    if True is self.__validate_deny_wp_admin:
                        self.create_wp_check('wp_admin', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-admin/')
                    if True is self.__validate_deny_wp_content:
                        self.create_wp_check('wp_includes', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-includes/')
                    if True is self.__validate_deny_wp_content:
                        self.create_wp_check('wp_content', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-content/')
                    if True is self.__validate_deny_wp_login:
                        self.create_wp_check('wp_login', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-login.php')
                    if True is self.__validate_deny_wp_cron:
                        self.create_wp_check('wp_cron', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-cron.php')
                    if True is self.__validate_deny_wp_load:
                        self.create_wp_check('wp_load', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-load.php')
                    if True is self.__validate_deny_wp_mail:
                        self.create_wp_check('wp_mail', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-mail.php')
                    if True is self.__validate_deny_wp_signup:
                        self.create_wp_check('wp_signup', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-signup.php')
                    if True is self.__validate_deny_wp_trackback:
                        self.create_wp_check('wp_trackback', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-trackback.php')
                    if True is self.__validate_deny_wp_xmlrpc:
                        self.create_wp_check('wp_xmlrpc', service_baseid, base_id, server, checkserver, domain,
                                             '/xmlrpc.php')
                    if True is self.__validate_deny_wp_config:
                        self.create_wp_check('wp_config', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-config.php')
                    if True is self.__validate_deny_wp_config_sample:
                        self.create_wp_check('wp_config_sample', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-config-sample.php')
                    if True is self.__validate_deny_wp_blog_header:
                        self.create_wp_check('wp_blog_header', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-blog-header.php')
                    if True is self.__validate_deny_wp_activate:
                        self.create_wp_check('wp_activate', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-activate.php')
                    if True is self.__validate_deny_wp_links_opml:
                        self.create_wp_check('wp_links_opml', service_baseid, base_id, server, checkserver, domain,
                                             '/wp-links-opml.php')
