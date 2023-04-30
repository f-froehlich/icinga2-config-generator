#!/usr/bin/python3
# -*- coding: utf-8
import typing

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.MonitoringPlugins.SSHDSecurityCommand import SSHDSecurityCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker

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

T = typing.TypeVar('T', bound='CheckSSHDSecurity')


class CheckSSHDSecurity(Check):

    def __init__(self, id: str):
        Check.__init__(self, id, 'CheckSSHDSecurity', 'monitoring_plugins_sshd_security')
        self.__permit_root_login = None
        self.__public_key_auth = None
        self.__password_auth = None
        self.__permit_empty_passwords = None
        self.__challenge_response_authentication = None
        self.__fingerprint_hash = None
        self.__port = None
        self.__config = []
        self.set_check_interval('15m')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('sshd'))
        self.add_service_group(ServiceGroup.create('sshd_security'))

    def set_permit_root_login(self, permit_root_login: typing.Union[str, None]) -> T:
        self.__permit_root_login = permit_root_login
        return self

    def get_permit_root_login(self) -> typing.Union[str, None]:
        return self.__permit_root_login

    def set_public_key_auth(self, public_key_auth: typing.Union[str, None]) -> T:
        self.__public_key_auth = public_key_auth
        return self

    def get_public_key_auth(self) -> typing.Union[str, None]:
        return self.__public_key_auth

    def set_password_auth(self, password_auth: typing.Union[str, None]) -> T:
        self.__password_auth = password_auth
        return self

    def get_password_auth(self) -> typing.Union[str, None]:
        return self.__password_auth

    def set_permit_empty_passwords(self, permit_empty_passwords: typing.Union[str, None]) -> T:
        self.__permit_empty_passwords = permit_empty_passwords
        return self

    def get_permit_empty_passwords(self) -> typing.Union[str, None]:
        return self.__permit_empty_passwords

    def set_fingerprint_hash(self, fingerprint_hash: typing.Union[str, None]) -> T:
        self.__fingerprint_hash = fingerprint_hash
        return self

    def get_fingerprint_hash(self) -> typing.Union[str, None]:
        return self.__fingerprint_hash

    def set_port(self, port: typing.Union[int, None]) -> T:
        self.__port = port
        return self

    def get_port(self) -> typing.Union[str, None]:
        return self.__port

    def set_challenge_response_authentication(self, challenge_response_authentication: typing.Union[str, None]) -> T:
        self.__challenge_response_authentication = challenge_response_authentication
        return self

    def get_challenge_response_authentication(self) -> typing.Union[str, None]:
        return self.__challenge_response_authentication

    def append_config_params(self, key: str, value: typing.Union[str, int]) -> T:
        config = key + "=" + str(value)
        if config not in self.__config:
            self.__config.append(config)
        return self

    def remove_config_params(self, key: str, value: typing.Union[str, int]) -> T:
        config = key + "=" + str(value)
        if config in self.__config:
            self.__config.remove(config)
        return self

    def get_config_params(self) -> typing.List[str]:
        return self.__config

    @staticmethod
    def create(id: str, force_create: bool = False) -> T:
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckSSHDSecurity(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckSSHDSecurity):
            raise Exception('Id must be for an instance of CheckSSHDSecurity but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_sshd_security'):
            SSHDSecurityCommand.create('monitoring_plugins_sshd_security')

        return check

    def validate(self):
        pass
