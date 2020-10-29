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
import requests


class CheckPageContent:

    def __init__(self, ok_content, warning_content, critical_content, uri, domain, port, ssl, header, clinet_cert,
                 client_key):

        self.__client_key = client_key
        self.__clinet_cert = clinet_cert
        self.__header = header
        self.__ssl = ssl
        self.__port = port
        self.__domain = domain
        self.__uri = uri
        self.__critical_content = critical_content
        self.__warning_content = warning_content
        self.__ok_content = ok_content

    def main(self):

        content = self.get_page_content()
        self.parse_page_content(content)

    def parse_page_content(self, content):
        for e in self.__critical_content:
            if e in content:
                print("CRITICAL: Found critical content '" + e + "' in response")
                sys.exit(2)

        for e in self.__warning_content:
            if e in content:
                print("WARNING: Found warning content '" + e + "' in response")
                sys.exit(1)

        for e in self.__ok_content:
            if e in content:
                print("OK: Found content '" + e + "' in response")
                sys.exit(0)

        if 0 == len(self.__ok_content):
            print("UNKNOWN: No expected content match. Pleas specify at least one ok result.")
            sys.exit(3)

        print("CRITICAL: No expected content match.")
        sys.exit(2)

    def get_page_content(self):
        proto = 'https' if self.__ssl else 'http'
        default_port = 443 if self.__ssl else 80
        port = self.__port if None != self.__port else default_port

        headers = self.get_header()
        cert = self.get_client_cert_config()

        r = requests.get(proto + '://' + self.__domain + ':' + str(port) + self.__uri, headers=headers, cert=cert)
        r.encoding = 'utf-8'
        return r.text

    def get_header(self):
        headers = {}
        for header in self.__header:
            header_config = header.split("=")
            if 2 != len(header_config):
                raise Exception(
                    "Header must have the following format: NAME=VALUE. Invalid header '" + header + "' given.")

            headers[header_config[0]] = header_config[1]
        return headers

    def get_client_cert_config(self):
        cert = None
        if None is not self.__client_key and None is not self.__clinet_cert:
            cert = (self.__clinet_cert, self.__client_key)
        elif None is not self.__client_key and None is self.__clinet_cert:
            raise Exception('If you specify a client certificate key, you have to specify a client certificate file.')
        elif None is self.__client_key and None is not self.__clinet_cert:
            raise Exception('If you specify a client certificate, you have to specify a client certificate key file.')
        return cert


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check Page Content')

    parser.add_argument('-w', '--warning-content', dest='warningcontent', action='append', default=[],
                        help='Warning content. Return warning state if at least one matched and no Critical content match')
    parser.add_argument('-c', '--critical-content', dest='criticalcontent', action='append', default=[],
                        help='Critical content. Return critical state if at least one matched')
    parser.add_argument('-o', '--ok-content', dest='okcontent', action='append', default=[],
                        help='OK content. Return OK state if at least one matched and no warning or critical content match')
    parser.add_argument('-H', '--header', dest='header', action='append', default=[],
                        help='Header for request. Format: NAME=VALUE')
    parser.add_argument('-u', '--uri', dest='uri', type=str, help='URI to fetch', default='/')
    parser.add_argument('-d', '--domain', dest='domain', type=str, help='Domain to fetch', required=True)
    parser.add_argument('-p', '--port', dest='port', type=int, help='Port to fetch')
    parser.add_argument('-s', '--ssl', dest='ssl', help='Use https', action='store_true')
    parser.add_argument('--client-cert', dest='clientcert', type=str, help='Path to client certificate')
    parser.add_argument('--client-key', dest='clientkey', type=str, help='Path to client certificate key file')

    args = parser.parse_args()
    CheckPageContent(
        ok_content=args.okcontent,
        warning_content=args.warningcontent,
        critical_content=args.criticalcontent,
        uri=args.uri,
        domain=args.domain,
        port=args.port,
        ssl=args.ssl,
        header=args.header,
        client_key=args.clientkey,
        clinet_cert=args.clientcert,
    ).main()
