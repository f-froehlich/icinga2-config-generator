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

from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.Icinga2Confgen.SSHDSecurityCommand import SSHDSecurityCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckSSHDSecurity(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckSSHDSecurity', 'sshd_security')
        self.__permit_root_login = None
        self.__public_key_auth = None
        self.__password_auth = None
        self.__permit_empty_passwords = None
        self.__challenge_response_authentication = None
        self.__fingerprint_hash = None
        self.__port = None
        self.__config = []
        self.set_check_interval('6h')
        self.add_service_group(ServiceGroup.create('security'))
        self.add_service_group(ServiceGroup.create('sshd'))
        self.add_service_group(ServiceGroup.create('sshd_security'))

    def set_permit_root_login(self, permit_root_login):
        ValueChecker.is_string(permit_root_login)
        self.__permit_root_login = permit_root_login
        return self

    def get_permit_root_login(self):
        return self.__permit_root_login

    def set_public_key_auth(self, public_key_auth):
        ValueChecker.is_string(public_key_auth)
        self.__public_key_auth = public_key_auth
        return self

    def get_public_key_auth(self):
        return self.__public_key_auth

    def set_password_auth(self, password_auth):
        ValueChecker.is_string(password_auth)
        self.__password_auth = password_auth
        return self

    def get_password_auth(self):
        return self.__password_auth

    def set_permit_empty_passwords(self, permit_empty_passwords):
        ValueChecker.is_string(permit_empty_passwords)
        self.__permit_empty_passwords = permit_empty_passwords
        return self

    def get_permit_empty_passwords(self):
        return self.__permit_empty_passwords

    def set_fingerprint_hash(self, fingerprint_hash):
        ValueChecker.is_string(fingerprint_hash)
        self.__fingerprint_hash = fingerprint_hash
        return self

    def get_fingerprint_hash(self):
        return self.__fingerprint_hash

    def set_port(self, port):
        ValueChecker.is_number(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    def set_challenge_response_authentication(self, challenge_response_authentication):
        ValueChecker.is_string(challenge_response_authentication)
        self.__challenge_response_authentication = challenge_response_authentication
        return self

    def get_challenge_response_authentication(self):
        return self.__challenge_response_authentication

    def append_config_params(self, key, value):
        ValueChecker.is_string(key)
        ValueChecker.is_string(value)
        self.__config.append(key + "=" + value)
        return self

    def remove_config_params(self, key, value):
        ValueChecker.is_string(key)
        ValueChecker.is_string(value)
        self.__config.remove(key + "=" + value)
        return self

    def get_config_params(self):
        return self.__config

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckSSHDSecurity(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('sshd_security'):
            SSHDSecurityCommand.create('sshd_security')

        return check

    def validate(self):
        pass
