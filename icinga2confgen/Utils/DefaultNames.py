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


def get_default_group_name(id):
    default_names = {
        'apache': 'Apache',
        'apt': 'APT',
        'breeze': 'Breeze',
        'certificate_check': 'X.509 certificate',
        'clamd': 'Clamd',
        'cron': 'Cron',
        'database': 'Database',
        'deny_insecure_TLSv1_0_webserver': 'Deny insecure TLS 1.0 webserver',
        'deny_insecure_TLSv1_0_unchecked': 'Deny insecure TLS 1.0 unchecked',
        'deny_insecure_TLSv1_1_webserver': 'Deny insecure TLS 1.1 webserver',
        'deny_insecure_TLSv1_1_unchecked': 'Deny insecure TLS 1.1 unchecked',
        'deny_secure_TLSv1_2_webserver': 'Deny secure TLS 1.2 wevserver',
        'deny_secure_TLSv1_3_webserver': 'Deny secure TLS 1.3 wevserver',
        'dhcp': 'DHCP',
        'dig': 'dig',
        'disk': 'Disk',
        'dns': 'DNS',
        'dnssec': 'DNSSEC',
        'docker': 'Docker',
        'dummy': 'Dummy',
        'existing_user': 'Existing users',
        'file_age': 'File age',
        'firewall': 'Firewall',
        'flexlm': 'Flexlm',
        'ftp': 'FTP',
        'group_members': 'Group members',
        'hpjd': 'HP JD',
        'http_redirect': 'Http to https redirect',
        'http_redirect_unchecked': 'Http to https redirect unchecked',
        'icmp': 'ICMP',
        'ifstatus': 'Interface status',
        'imap': 'IMAP',
        'insecure_webserver': 'Insecure webserver',
        'insecure_TLSv1_0_Webserver': 'Insecure TLS v1.0 webserver',
        'insecure_TLSv1_1_Webserver': 'Insecure TLS v1.1 webserver',
        'ircd': 'IRCD',
        'jabber': 'Jabber',
        'ldap': 'LDAP',
        'load': 'Load',
        'log': 'Log',
        'mail': 'Mail',
        'mailq': 'Mail queue',
        'missing_http_redirect_check': 'Missing http to https redirect check',
        'mrt_gtraf': 'MRT graf',
        'mysql': 'MySQL',
        'network': 'Network',
        'nginx': 'NGINX',
        'nntp': 'NNTP',
        'no_certificate_check': 'No X.509 Certificate check',
        'ntp': 'NTP',
        'ns_client': 'NS Client',
        'path_exists': 'Path exists',
        'php_fpm': 'PHP FPM',
        'postgres': 'PostgreSQL',
        'ping': 'Ping',
        'pop': 'POP',
        'procs': 'Procs',
        'radius': 'RADIUS',
        'rpc': 'RPC',
        'rsyslogd': 'rsyslogd',
        'secure_webserver': 'Secure Webserver',
        'secure_TLSv1_2_unchecked': 'Secure TLS 1.2 unchecked',
        'secure_TLSv1_3_unchecked': 'Secure TLS 1.3 unchecked',
        'secure_TLSv1_2_webserver': 'Secure TLS 1.2 Webserver',
        'secure_TLSv1_3_webserver': 'Secure TLS 1.3 Webserver',
        'security': 'Security',
        'sensors': 'Sensors',
        'smart': 'SMART',
        'smtp': 'SMTP',
        'snmp': 'SNMP',
        'sshd': 'SSHD',
        'sshd_security': 'SSHD security',
        'sudoers': 'Sudoers',
        'swap': 'SWAP',
        'system_health': 'System health',
        'tcp': 'TCP',
        'tls': 'TLS',
        'tls_1_check': 'TLS v1.0 Check',
        'tls_1_1_check': 'TLS v1.1 Check',
        'tls_1_2_check': 'TLS v1.2 Check',
        'tls_1_3_check': 'TLS v1.3 Check',
        'tomcat': 'Apache Tomcat',
        'udp': 'UDP',
        'ufw': 'UFW',
        'ups': 'UPS',
        'updates': 'Updates',
        'uptime': 'Uptime',
        'user': 'User',
        'yum': 'YUM',
        'wave': 'Wave',
        'webserver': 'Webserver',
    }

    return default_names.get(id, id.replace('_', ' '))
