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

from __future__ import annotations

from typing import List, Union

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class Webrequest(Check):

    def __init__(self, id: str, class_name: str, command_name: str, command_name_prefix: str):
        Check.__init__(self, id, class_name, f"{command_name_prefix}_{command_name}")
        self._command_name = command_name
        self.__header = []
        self.__uri = None
        self.__domain = None
        self.__port = None
        self.__ssl = False
        self.__client_cert = None
        self.__client_key = None
        self.__timeout = 60
        self.set_check_timeout(90)
        self.add_service_group(ServiceGroup.create('webserver'))

    def set_timeout(self, timeout: int) -> Webrequest:
        ValueChecker.is_number(timeout)
        self.__timeout = timeout
        return self

    def get_timeout(self) -> int:
        return self.__timeout

    def set_header(self, header: str) -> Webrequest:
        self.__header.append(header)
        return self

    def get_header(self) -> List[str]:
        return self.__header

    def set_uri(self, uri: Union[str, None]) -> Webrequest:
        self.__uri = uri
        return self

    def get_uri(self) -> Union[str, None]:
        return self.__uri

    def set_domain(self, domain: Union[str, None]) -> Webrequest:
        self.__domain = domain
        return self

    def get_domain(self) -> str:
        return self.__domain

    def set_port(self, port: Union[int, None]) -> Webrequest:
        self.__port = port
        return self

    def get_port(self) -> Union[str, None]:
        return self.__port

    def set_ssl(self, ssl: bool) -> Webrequest:
        self.__ssl = ssl
        return self

    def get_ssl(self) -> bool:
        return self.__ssl

    def set_client_cert(self, client_cert: Union[str, None]) -> Webrequest:
        self.__client_cert = client_cert
        return self

    def get_client_cert(self) -> Union[str, None]:
        return self.__client_cert

    def set_client_key(self, client_key: Union[str, None]) -> Webrequest:
        self.__client_key = client_key
        return self

    def get_client_key(self) -> Union[str, None]:
        return self.__client_key

    def get_custom_config(self) -> str:
        return ValueMapper.get_property_default_config(self, 'Webrequest', self._command_name, 'command')

    def get_config(self) -> str:
        self.validate()
        Webrequest.validate(self)
        config = Check.get_config(self)
        return config

    def validate(self):
        pass
